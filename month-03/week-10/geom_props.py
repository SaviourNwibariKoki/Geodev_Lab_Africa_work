from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
settlements = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements')
settlements['area_ha'] = settlements.geometry.area / 10_000
print(settlements[['block_id', 'area_ha']].head(5).to_string(index=False))
print('area range hectares:', round(settlements.area_ha.min(), 2), 'to', round(settlements.area_ha.max(), 2))
