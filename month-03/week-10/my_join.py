from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
points = gpd.read_file(week / 'settlement_centroids.gpkg', layer='centroids')
lga = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='lga_boundary')[['lganame', 'geometry']]
joined = gpd.sjoin(points, lga, predicate='within', how='left')
print('centroids assigned to an LGA:', joined['lganame'].notna().sum(), 'of', len(joined))
print(joined[['block_id', 'lganame']].head().to_string(index=False))
