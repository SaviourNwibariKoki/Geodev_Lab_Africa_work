from pathlib import Path
import matplotlib.pyplot as plt
import rasterio
from _common import SCENE
ndvi_path=Path(__file__).resolve().parent/'my_ndvi.tif'
with rasterio.open(ndvi_path) as src: data=src.read(1,masked=True)
fig, ax=plt.subplots(figsize=(8,6)); image=ax.imshow(data,cmap='YlGn',vmin=-1,vmax=1); fig.colorbar(image,ax=ax,label='NDVI'); ax.set_title('Port-Harcourt NDVI: 15 January 2024'); ax.set_xlabel('Column'); ax.set_ylabel('Row'); fig.tight_layout(); fig.savefig(Path(__file__).resolve().parent/'my_map.png',dpi=160)
print('wrote my_map.png')
