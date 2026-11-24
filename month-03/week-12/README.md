# Week 12: rasters with Rasterio

The scene used here is `port_harcourt_scene_2024-01-15.tif`, covering Port Harcourt on **2024-01-15** with recorded cloud cover of **10 percent**. It has red, near-infrared, and elevation-style bands in EPSG:32632. The raster is local and ignored; no `.tif` file is committed. See `data-notes.md` for the full description.

## Guided scripts

Run from the repository root with `uv run python month-03/week-12/<script>.py`:

- `inspect_raster.py` checks dimensions, bands, CRS, bounds, transform, nodata and tags.
- `read_values.py` reads masked band values safely.
- `pixel_coords.py` converts row and column positions to map coordinates.
- `sample_points.py` samples the raster at settlement centroids.
- `ndvi.py` calculates NDVI from bands 1 and 2.
- `plot_raster.py` writes the required `ndvi_map.png`.
- `clip_raster.py` clips the scene to the Port-Harcourt LGA.
- `zonal_stats.py` writes `zonal_stats.csv`.
- `reproject_raster.py` reprojects a local output to EPSG:4326.

## Independent challenge

The challenge uses the Port-Harcourt scene and Month 1 settlement polygons:

- `my_inspect.py` records the scene metadata.
- `my_index.py` writes a local `my_ndvi.tif` and reports valid NDVI statistics.
- `my_zonal.py` writes `my_zonal_stats.csv`, summarising NDVI per settlement polygon.
- `my_map.py` writes `my_map.png`.

The limitation is that this is a small deterministic teaching scene, not a downloaded satellite acquisition. The NDVI results demonstrate the method but should not be interpreted as a real remote-sensing vegetation assessment.
