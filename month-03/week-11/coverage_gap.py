from pathlib import Path
import geopandas as gpd
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
lga = gpd.read_file(base, layer='lga_boundary')
facilities = pd.read_csv(ROOT / 'data' / 'facilities.csv')
points = gpd.GeoDataFrame(facilities, geometry=gpd.points_from_xy(facilities.longitude, facilities.latitude), crs=4326).to_crs(32632)
reach = points.buffer(2000).union_all()
covered = lga.geometry.iloc[0].intersection(reach)
gap = lga.geometry.iloc[0].difference(reach)
print('Facilities:', len(points))
print('Dissolved reach area hectares:', round(covered.area / 10000, 2))
print('Uncovered LGA area hectares:', round(gap.area / 10000, 2))
