from pathlib import Path
import numpy as np
import rasterio
from _common import SCENE
out = Path(__file__).resolve().parent / 'ndvi.tif'
with rasterio.open(SCENE) as src:
    red = src.read(1, masked=True).astype('float32')
    nir = src.read(2, masked=True).astype('float32')
    ndvi = np.ma.divide(nir - red, nir + red).filled(-9999).astype('float32')
    profile = src.profile.copy(); profile.update(count=1, dtype='float32', nodata=-9999, compress='deflate')
    with rasterio.open(out, 'w', **profile) as dst:
        dst.write(ndvi, 1); dst.set_band_description(1, 'NDVI')
print('wrote', out.name, 'mean NDVI:', round(float(np.ma.masked_equal(ndvi, -9999).mean()), 4))
