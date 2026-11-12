from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
processed = ROOT / 'data' / 'processed'
processed.mkdir(exist_ok=True)
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
settlements = gpd.read_file(base, layer='settlements')
settlements['geometry'] = settlements.geometry.make_valid()
result = settlements[['block_id', 'building_count', 'geometry']].copy()
out = processed / 'week11_validated_settlements.gpkg'
result.to_file(out, layer='settlements_validated', driver='GPKG')
print('valid geometries:', result.geometry.is_valid.all())
print('empty geometries:', result.geometry.is_empty.sum())
print('wrote', out)
