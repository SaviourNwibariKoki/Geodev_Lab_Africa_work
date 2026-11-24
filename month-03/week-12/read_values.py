import numpy as np
import rasterio
from _common import SCENE
with rasterio.open(SCENE) as src:
    red = src.read(1, masked=True)
    dem = src.read(3, masked=True)
    print('red shape:', red.shape, 'valid cells:', int((~red.mask).sum()))
    print('red mean:', round(float(red.mean()), 2))
    print('DEM minimum and maximum:', round(float(dem.min()), 2), round(float(dem.max()), 2))
    print('band 1 is first band; Rasterio numbering starts at 1')
