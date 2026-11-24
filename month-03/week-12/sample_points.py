import geopandas as gpd
import rasterio
from _common import ROOT, SCENE
settlements = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements').to_crs(32632)
with rasterio.open(SCENE) as src:
    points = [geom.centroid for geom in settlements.head(5).geometry]
    samples = list(src.sample([(p.x, p.y) for p in points], indexes=1))
print('sampled first five settlement centroids:', [round(float(v[0]), 2) for v in samples])
