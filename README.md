# bubble_rcnn

```bash
├── data
│   ├── patches
│   │   ├── test
│   │   │   ├── images
│   │   │   ├── masks
│   │   ├── train
│   │   │   ├── images
│   │   │   ├── masks
│   │   ├── val
│   │   │   ├── images
│   │   │   ├── masks
│   ├── processed
│   │   ├── images
│   │   │   ├── imngc628_f770w_norm.npy
│   │   ├── masks
│   │   │   ├── ngc628_f770w_norm.npy
│   │   │   ├── ngc628_superbubble_mask.npy
│   │   ├── metadata
│   │   ├── patches
│   │   │   ├── X.npy
│   │   │   ├── Y.npy
│   ├── raw
│   │   ├── catalogue
│   │   │   ├── jwst_bubble_properties_A.txt
│   │   │   ├── ngc1566pixel.txt
│   │   ├── fits
│   │   │   ├── jw02107-c1007_t007_miri_f1130w_i2d_NGC1566_cropped.fits.fits
│   │   │   ├── jw02107-o039_t018_miri_f770w_i2d.fits
├── notebooks
│   ├── data
│   │   ├── processed
│   │   │   ├── patches
│   ├── catalogueABC-verification.ipynb
│   ├── catalogueadjuctment_alternate.ipynb
│   ├── crop_ngc1566.ipynb
│   ├── data_cleaningABC.ipynb
│   ├── data_cleaning.ipynb
│   ├── data_processing_v0.ipynb
│   ├── data_processing.ipynb
│   ├── ngc1566on-training2.ipynb
│   ├── patch_maker.ipynb
│   ├── predictions.ipynb
├── outputs
│   ├── figures
│   │   │   ├── catalogueA
│   │   │   │   ├── overlay_tiny.png
│   │   │   │   ├── overlay_small.png
│   │   │   │   ├── overlay_medium.png
│   │   │   │   ├── overlay_large.png
│   │   │   │   ├── overlay_giants.png
│   │   │   │   ├── overlay_edgeLarge.png
│   │   │   │   ├── distributions
│   │   │   │   │   ├── avg_radius_distribution_categories_A.png
│   │   │   │   │   ├── avg_radius_distribution_linear_A.png
│   │   │   │   │   ├── avg_radius_distribution_log_A.png
│   │   │   ├── catalogueB
│   │   │   │   ├── overlay_tiny.png
│   │   │   │   ├── overlay_small.png
│   │   │   │   ├── overlay_medium.png
│   │   │   │   ├── overlay_large.png
│   │   │   │   ├── overlay_giants.png
│   │   │   │   ├── overlay_edgeLarge.png
│   │   │   │   ├── distributions
│   │   │   │   │   ├── avg_radius_distribution_categories_A.png
│   │   │   │   │   ├── avg_radius_distribution_linear_A.png
│   │   │   │   │   ├── avg_radius_distribution_log_A.png
│   │   │   ├── catalogueC
│   │   │   │   ├── overlay_tiny.png
│   │   │   │   ├── overlay_small.png
│   │   │   │   ├── overlay_medium.png
│   │   │   │   ├── overlay_large.png
│   │   │   │   ├── overlay_giants.png
│   │   │   │   ├── overlay_edgeLarge.png
│   │   │   │   ├── distributions
│   │   │   │   │   ├── avg_radius_distribution_categories_A.png
│   │   │   │   │   ├── avg_radius_distribution_linear_A.png
│   │   │   │   │   ├── avg_radius_distribution_log_A.png
│   │   │   ├── **/*.png
│   ├── logs
│   │   ├── catalogueA_stratification.txt
│   │   ├── catalogueB_stratification.txt
│   │   ├── catalogueC_stratification.txt
│   ├── predictions
│   │   │   ├── all_bubbles_overlay.png
├── src
│   ├── data
│   ├── models
│   ├── training
│   ├── utils
├── verify
│   ├── bubbles
│   ├── random
└── .gitignore
└── README.md
```