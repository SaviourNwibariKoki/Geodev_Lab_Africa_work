from pathlib import Path
import geopandas as gpd
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
rows = pd.read_csv(ROOT / 'data' / 'facilities.csv')
points = gpd.GeoDataFrame(rows, geometry=gpd.points_from_xy(rows['longitude'], rows['latitude']), crs='EPSG:4326').to_crs('EPSG:32632')
out = week / 'facilities_points.gpkg'
points.to_file(out, layer='facilities', driver='GPKG')
print(f'wrote {len(points)} points to {out.name}; CRS={points.crs}')
