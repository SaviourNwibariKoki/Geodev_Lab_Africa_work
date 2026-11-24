from pathlib import Path
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from _common import SCENE
out = Path(__file__).resolve().parent / 'scene_wgs84.tif'
with rasterio.open(SCENE) as src:
    transform, width, height = calculate_default_transform(src.crs, 'EPSG:4326', src.width, src.height, *src.bounds)
    profile = src.profile.copy(); profile.update(crs='EPSG:4326', transform=transform, width=width, height=height, compress='deflate')
    with rasterio.open(out, 'w', **profile) as dst:
        for band in range(1, src.count + 1):
            reproject(source=rasterio.band(src, band), destination=rasterio.band(dst, band), src_transform=src.transform, src_crs=src.crs, dst_transform=transform, dst_crs='EPSG:4326', resampling=Resampling.nearest)
print('wrote scene_wgs84.tif')
