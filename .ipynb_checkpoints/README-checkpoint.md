# bubble_rcnn


masters-thesis/
│
├── data/
│   ├── raw/
│   │   ├── fits/
│   │   │   └── ngc628_f770w.fits
│   │   ├── catalog/
│   │   │   └── jwst_bubble_properties.txt
│   │
│   ├── processed/
│   │   ├── images/
│   │   │   └── ngc628_f770w_norm.npy
│   │   ├── masks/
│   │   │   └── ngc628_mask.npy
│   │   ├── metadata/
│   │   │   └── pixel_scale.json
│   │
│   ├── patches/
│   │   ├── train/
│   │   │   ├── images/
│   │   │   └── masks/
│   │   ├── val/
│   │   │   ├── images/
│   │   │   └── masks/
│   │   └── test/
│   │       ├── images/
│   │       └── masks/
│
├── notebooks/
│   └── data_processing.ipynb
│
├── src/
│   ├── data/
│   │   ├── fits_loader.py
│   │   ├── wcs_utils.py
│   │   ├── mask_generator.py
│   │   └── patch_extractor.py
│   │
│   ├── models/
│   │   └── unet.py
│   │
│   ├── training/
│   │   └── train.py
│   │
│   └── utils/
│       └── visualization.py
│
├── outputs/
│   ├── figures/
│   ├── predictions/
│   └── logs/
│
├── thesis/
│   └── latex/
│
└── README.md