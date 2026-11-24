import rasterio
from _common import SCENE
with rasterio.open(SCENE) as src:
    print('scene:', SCENE.name)
    print('width, height:', src.width, src.height)
    print('bands:', src.count, 'dtype:', src.dtypes)
    print('CRS:', src.crs)
    print('bounds:', tuple(round(v, 2) for v in src.bounds))
    print('transform:', src.transform)
    print('nodata:', src.nodata)
    print('tags:', src.tags())
