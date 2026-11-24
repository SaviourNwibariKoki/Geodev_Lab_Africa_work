import rasterio
from _common import SCENE
with rasterio.open(SCENE) as src:
    print('Own scene:', SCENE.name)
    print('date:', src.tags().get('scene_date'), 'cloud cover:', src.tags().get('cloud_cover'))
    print('shape:', (src.height, src.width), 'bands:', src.count, 'CRS:', src.crs)
    print('nodata:', src.nodata)
