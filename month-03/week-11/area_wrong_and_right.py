from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
path = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
lga = gpd.read_file(path, layer='lga_boundary')
wrong = lga.to_crs(4326).geometry.area.iloc[0]
right = lga.geometry.area.iloc[0]
print('EPSG:4326 area (not meaningful square degrees):', round(wrong, 6))
print('EPSG:32632 area (square metres):', round(right, 2))
print('EPSG:32632 area (hectares):', round(right / 10000, 2))
