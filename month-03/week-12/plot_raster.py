from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from _common import SCENE
with rasterio.open(SCENE) as src:
    red = src.read(1, masked=True).astype('float32')
    nir = src.read(2, masked=True).astype('float32')
    ndvi = np.ma.divide(nir - red, nir + red)
fig, ax = plt.subplots(figsize=(8, 6)); image = ax.imshow(ndvi, cmap='YlGn', vmin=-1, vmax=1); fig.colorbar(image, ax=ax, label='NDVI')
ax.set_title('Port-Harcourt NDVI: 15 January 2024'); ax.set_xlabel('Column'); ax.set_ylabel('Row'); fig.tight_layout()
out = Path(__file__).resolve().parent / 'ndvi_map.png'
fig.savefig(out, dpi=160)
print('wrote', out.name)
