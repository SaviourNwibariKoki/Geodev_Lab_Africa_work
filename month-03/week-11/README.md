# Week 11: coordinate reference systems and spatial operations

This week uses **EPSG:32632 (WGS 84 / UTM zone 32N)**. Port Harcourt lies in UTM zone 32N, and this projected CRS measures distance and area in metres, unlike EPSG:4326 degrees.

## Guided scripts

Run from the repository root with `uv run python month-03/week-11/<script>.py`:

- `area_wrong_and_right.py` compares meaningless geographic square-degree area with projected square-metre area.
- `set_vs_to.py` demonstrates assigning a CRS with `set_crs` versus transforming coordinates with `to_crs`.
- `one_point.py` transforms one projected point to longitude and latitude with `always_xy=True`.
- `spatial_ops.py` creates 100 m road buffers and intersects them with settlement polygons.
- `coverage_gap.py` dissolves 2 km facility buffers and calculates covered and uncovered LGA area.
- `nearest.py` finds the nearest mapped road to each settlement centre.
- `clip_dissolve.py` clips roads to the LGA and dissolves 200 m road buffers.
- `fix_geometry.py` checks and repairs invalid geometries with `make_valid`.

## Independent challenge

The challenge uses the real Month 1 Port Harcourt settlement, road, LGA, and facility data:

- `my_crs.py` measures the settlement layer in EPSG:32632.
- `my_count.py` counts settlement centres within 100 m of mapped roads.
- `my_reach.py` calculates 2 km facility reach and writes `my_reach.png`.
- `my_validity.py` validates settlement geometries and writes `data/processed/week11_validated_settlements.gpkg`.

## Limitation

The facility points are mapped examples from the available project data, not a complete official inventory. Therefore, the 2 km coverage result describes access to mapped points only and may underestimate true facility coverage.
