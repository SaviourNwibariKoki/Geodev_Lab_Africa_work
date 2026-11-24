from pathlib import Path
import geopandas as gpd
import rasterio
from rasterio.mask import mask
from _common import ROOT, SCENE
out = Path(__file__).resolve().parent / 'scene_clipped.tif'
lga = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='lga_boundary').to_crs(32632)
with rasterio.open(SCENE) as src:
    data, transform = mask(src, lga.geometry, crop=True)
    profile = src.profile.copy(); profile.update(height=data.shape[1], width=data.shape[2], transform=transform, compress='deflate')
    with rasterio.open(out, 'w', **profile) as dst: dst.write(data)
print('wrote clipped scene:', data.shape)
