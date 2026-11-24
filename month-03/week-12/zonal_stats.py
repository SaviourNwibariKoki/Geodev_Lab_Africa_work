from pathlib import Path
import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask
from _common import ROOT, SCENE
settlements = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements').to_crs(32632)
rows = []
with rasterio.open(SCENE) as src:
    red = src.read(1, masked=True).astype('float32')
    nir = src.read(2, masked=True).astype('float32')
    ndvi = np.ma.divide(nir - red, nir + red).filled(-9999).astype('float32')
    profile = src.profile.copy()
    profile.update(count=1, dtype='float32', nodata=-9999)
    with rasterio.io.MemoryFile() as mem:
        with mem.open(**profile) as ndvi_src:
            ndvi_src.write(ndvi, 1)
            for _, row in settlements.iterrows():
                data, _ = mask(ndvi_src, [row.geometry], crop=True, filled=False)
                values = data.compressed()
                rows.append({
                    'block_id': row.block_id,
                    'ndvi_mean': float(values.mean()) if len(values) else None,
                    'pixel_count': int(len(values)),
                })
out = pd.DataFrame(rows)
out.to_csv(Path(__file__).resolve().parent / 'zonal_stats.csv', index=False)
print('wrote zonal_stats.csv rows:', len(out))
print('non-empty zones:', int(out['pixel_count'].gt(0).sum()))
