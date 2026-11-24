from pathlib import Path
import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask
from _common import ROOT, SCENE
polys = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements').to_crs(32632)
rows=[]
with rasterio.open(SCENE) as src:
    red = src.read(1, masked=True); nir = src.read(2, masked=True)
    ndvi = np.ma.divide(nir-red, nir+red)
    for _, row in polys.iterrows():
        data, _ = mask(rasterio.io.MemoryFile().open(), [row.geometry], crop=True) if False else (None, None)
        # Use rasterio.mask on the in-memory NDVI array through a temporary profile-independent dataset.
        with rasterio.io.MemoryFile() as mem:
            profile=src.profile.copy(); profile.update(count=1,dtype='float32',nodata=-9999)
            with mem.open(**profile) as temp:
                temp.write(ndvi.filled(-9999).astype('float32'),1)
                clipped,_=mask(temp,[row.geometry],crop=True,filled=False)
        vals=clipped.compressed()
        rows.append({'block_id':row.block_id,'ndvi_mean':float(vals.mean()) if len(vals) else None,'pixel_count':int(len(vals))})
out=Path(__file__).resolve().parent/'my_zonal_stats.csv'; pd.DataFrame(rows).to_csv(out,index=False)
print('wrote', out.name, 'rows:', len(rows), 'non-empty zones:', sum(r['pixel_count']>0 for r in rows))
