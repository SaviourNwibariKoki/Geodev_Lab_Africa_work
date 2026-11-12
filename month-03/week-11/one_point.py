from pathlib import Path
import geopandas as gpd
from pyproj import Transformer
ROOT = Path(__file__).resolve().parents[2]
settlements = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements')
point = settlements.geometry.iloc[0].centroid
transformer = Transformer.from_crs(32632, 4326, always_xy=True)
longitude, latitude = transformer.transform(point.x, point.y)
print('Projected centroid:', round(point.x, 2), round(point.y, 2))
print('Longitude, latitude:', round(longitude, 6), round(latitude, 6))
print('always_xy=True means x/longitude is transformed before y/latitude.')
