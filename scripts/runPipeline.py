"""Run the full curriculum pipeline for one stage.

Usage:
    python scripts/runPipeline.py stage00
    python scripts/runPipeline.py stage00 --start-at alternate_cleaningCatalogue
    python scripts/runPipeline.py stage01 --only perClassEvaluation
    python scripts/runPipeline.py stage00 --dry-run

Executes the notebook chain in dependency order, setting ACTIVE_STAGE in every
stage-aware notebook first:

    catalogueBCorrection -> catalogueMerging -> curriculumCatalogueSelection
    -> alternate_bubbleStratt -> [MANUAL CLEANING of badBubbles.txt]
    -> alternate_cleaningCatalogue -> alternate_sanityCheck
    -> galaxyMaskGeneration -> patchMaker -> trainingDataAugmentation
    -> predictions (training) -> perClassEvaluation

At the manual-cleaning step the script pauses so you can inspect the
stratification map and update data/processed/metadata/badBubbles.txt; press
Enter to continue, or pass --no-pause to skip the stop (e.g. when badBubbles.txt
is already up to date). In a non-interactive shell the script exits there -
resume with --start-at alternate_cleaningCatalogue.

Each notebook runs with notebooks/ as its working directory (so their relative
../data paths work) and is saved in place with its outputs, exactly as if run
by hand. The script stops at the first failing step.

Run this with the same Python environment you use for the notebooks
(it needs tensorflow plus nbformat/nbclient: pip install nbformat nbclient).
"""

import argparse
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTEBOOKS = REPO / "notebooks"

STAGES = [f"stage{i:02d}" for i in range(6)]

MANUAL_CLEANING = "MANUAL_CLEANING"

# (notebook name, is stage-aware) in dependency order
PIPELINE = [
    ("catalogueBCorrection", False),          # fix catalogue B -> jwst_bubble_properties_B_fixed.txt
    ("catalogueMerging", False),              # -> mergedCatalogue.txt
    ("curriculumCatalogueSelection", True),   # stage catalogue + segregatedMergedCatalogue.txt
    ("alternate_bubbleStratt", True),         # stratification map figure
    (MANUAL_CLEANING, False),                 # human step: update badBubbles.txt
    ("alternate_cleaningCatalogue", False),   # -> cleanedSegregatedMergedCatalogue.txt
    ("alternate_sanityCheck", True),          # cleaned catalogue map figure
    ("galaxyMaskGeneration", False),          # -> ngc628NormMask.npy
    ("patchMaker", False),                    # -> X/Y + patchMetadata.csv with spatial split
    ("trainingDataAugmentation", False),      # -> XtrainAug/YtrainAug/Xval/Yval
    ("predictions", True),                    # training -> {stage}bubble_unet.keras
    ("perClassEvaluation", True),             # -> {stage}perClassEval.csv + figures
]

NOTEBOOK_NAMES = [name for name, _ in PIPELINE if name != MANUAL_CLEANING]

STAGE_LINE = re.compile(r'^(\s*)ACTIVE_STAGE\s*=\s*["\']stage\d+["\']', re.MULTILINE)


def set_active_stage(nb, stage):
    """Rewrite the ACTIVE_STAGE assignment in a loaded notebook. Returns hit count."""
    hits = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        new_src, n = STAGE_LINE.subn(rf'\1ACTIVE_STAGE = "{stage}"', cell.source)
        if n:
            cell.source = new_src
            hits += n
    return hits


def manual_cleaning_gate(args, step_no, n_steps):
    label = f"[{step_no}/{n_steps}] MANUAL CLEANING"
    if args.no_pause:
        print(f"{label} - skipped (--no-pause)")
        return
    if args.dry_run:
        print(f"{label} - pause here to update badBubbles.txt")
        return
    print(f"{label}")
    print("    Inspect the stratification map (outputs/figures/"
          f"{args.stage}SegregatedMergedCatalogueMap.png)")
    print("    and update data/processed/metadata/badBubbles.txt if needed.")
    if not sys.stdin.isatty():
        print("    Non-interactive shell: stopping here. Resume with:")
        print(f"    python scripts/runPipeline.py {args.stage} --start-at alternate_cleaningCatalogue")
        sys.exit(0)
    input("    Press Enter to continue... ")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("stage", choices=STAGES)
    parser.add_argument("--start-at", metavar="NOTEBOOK", choices=NOTEBOOK_NAMES,
                        help="resume the chain from this notebook")
    parser.add_argument("--only", metavar="NOTEBOOK", choices=NOTEBOOK_NAMES,
                        help="run a single notebook instead of the whole chain")
    parser.add_argument("--no-pause", action="store_true",
                        help="do not stop at the manual-cleaning step "
                             "(badBubbles.txt is already up to date)")
    parser.add_argument("--kernel", default=None,
                        help="jupyter kernel name (default: whatever each notebook declares)")
    parser.add_argument("--dry-run", action="store_true",
                        help="set ACTIVE_STAGE and list the steps without executing")
    args = parser.parse_args()

    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError as e:
        sys.exit(f"missing dependency ({e.name}): pip install nbformat nbclient")

    val_regions = REPO / "data/processed/metadata/valRegions.csv"
    if not val_regions.exists():
        sys.exit(f"{val_regions} not found - the spatial split needs it")

    steps = list(PIPELINE)
    if args.only:
        steps = [s for s in steps if s[0] == args.only]
    elif args.start_at:
        names = [name for name, _ in PIPELINE]
        steps = steps[names.index(args.start_at):]

    print(f"pipeline for {args.stage}: {len(steps)} step(s)")
    t_total = time.time()

    for step_no, (name, stage_aware) in enumerate(steps, 1):
        if name == MANUAL_CLEANING:
            manual_cleaning_gate(args, step_no, len(steps))
            continue

        path = NOTEBOOKS / f"{name}.ipynb"
        nb = nbformat.read(path, as_version=4)

        if stage_aware:
            hits = set_active_stage(nb, args.stage)
            if hits == 0:
                sys.exit(f"{name}: expected an ACTIVE_STAGE assignment but found none")
            nbformat.write(nb, path)

        label = f"[{step_no}/{len(steps)}] {name}" + (f" (ACTIVE_STAGE={args.stage})" if stage_aware else "")
        if args.dry_run:
            print(f"{label} - dry run, not executed")
            continue

        print(f"{label} ...", flush=True)
        t0 = time.time()
        client = NotebookClient(
            nb,
            timeout=None,
            kernel_name=args.kernel or nb.metadata.get("kernelspec", {}).get("name", "python3"),
            resources={"metadata": {"path": str(NOTEBOOKS)}},
        )
        try:
            client.execute()
        finally:
            nbformat.write(nb, path)  # keep outputs even on failure, for debugging
        print(f"    done in {time.time() - t0:.0f}s")

    if not args.dry_run:
        print(f"\n{args.stage} pipeline complete in {(time.time() - t_total) / 60:.1f} min")
        print(f"  model:      outputs/models/{args.stage}bubble_unet.keras")
        print(f"  evaluation: outputs/predictions/{args.stage}perClassEval.csv")


if __name__ == "__main__":
    main()
