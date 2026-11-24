# Week 12 raster data notes

The local raster used for the Week 12 exercises is `data/port_harcourt_scene_2024-01-15.tif`. It is an ignored, three-band teaching scene covering the Port-Harcourt LGA extent in EPSG:32632. Band 1 is red reflectance, band 2 is near-infrared reflectance, and band 3 is an elevation-model-style band in metres. The scene date is **2024-01-15** and the recorded cloud cover is **10 percent**.

This small scene was generated locally from deterministic arrays over the real Port-Harcourt study-area bounds because the repository contained no starter raster after the environment reset. It is used to demonstrate Rasterio workflows and is not committed to GitHub. The top-left corner contains nodata value `-9999` so masked reads and nodata-safe NDVI calculations can be tested.

The repository intentionally contains no `.tif` files. The raster remains on the laptop and is excluded by `.gitignore`.
