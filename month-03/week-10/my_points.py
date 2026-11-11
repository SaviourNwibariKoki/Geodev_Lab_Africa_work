from pathlib import Path
import geopandas as gpd
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
rows = pd.read_csv(ROOT / 'data' / 'week10_settlement_points.csv')
points = gpd.GeoDataFrame(rows, geometry=gpd.points_from_xy(rows['longitude'], rows['latitude']), crs='EPSG:4326').to_crs('EPSG:32632')
points.to_file(week / 'settlement_centroids.gpkg', layer='centroids', driver='GPKG')
print('created', len(points), 'settlement centroid points')
