# Week 10: GeoPandas exploration, joins and maps

This week connects the Month 1 Port Harcourt GIS project to Python. The guided scripts inspect tables and layers, calculate geometry properties, convert CSV coordinates to points, join a small population table, make a map, and save a CSV output.

## Guided scripts

Run from the repository root with `uv run python month-03/week-10/<script>.py`:

- `explore_pandas.py` inspects the settlement CSV as a pandas table.
- `filter_sort.py` filters and sorts settlement records.
- `explore_layer.py` reports row count, geometry type, CRS and bounds for three GeoPackage layers.
- `geom_props.py` calculates settlement area in hectares.
- `csv_to_points.py` converts `data/facilities.csv` coordinates into a projected point GeoPackage.
- `join_population.py` joins the ward table to `data/ward_population_2024.csv`.
- `make_map.py` writes `facilities_map.png`.
- `save_outputs.py` writes `wards_table.csv`.

## Independent challenge

The challenge uses the real Month 1 Port Harcourt settlement layer, not the practice wards data:

- `my_explore.py` checks the settlement layer and summarises building counts.
- `my_points.py` creates settlement centroids in `settlement_centroids.gpkg`.
- `my_join.py` spatially joins settlements to the Port-Harcourt LGA boundary.
- `my_map.py` writes `my_map.png`, a map coloured by building count.

Small input CSVs used by the guided scripts are in the repository `data/` folder. No rasters are included.
