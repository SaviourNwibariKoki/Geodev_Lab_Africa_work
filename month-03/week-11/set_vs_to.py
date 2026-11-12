from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
layer = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements')
print('Original CRS:', layer.crs)
missing_crs = layer.copy()
missing_crs = missing_crs.set_crs(None, allow_override=True).set_crs(32632)
print('set_crs: labels existing coordinate numbers as EPSG:32632; bounds unchanged:', missing_crs.total_bounds.round(2).tolist())
converted = layer.to_crs(4326)
print('to_crs: transforms coordinates to EPSG:4326; bounds:', converted.total_bounds.round(5).tolist())
