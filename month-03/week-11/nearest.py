from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
settlements = gpd.read_file(base, layer='settlements')
roads = gpd.read_file(base, layer='roads_osm')
centres = settlements[['block_id', 'geometry']].copy()
centres['geometry'] = centres.geometry.centroid
nearest = gpd.sjoin_nearest(centres, roads[['highway', 'geometry']], how='left', distance_col='distance_m')
print('Settlement centres:', len(centres))
print('Nearest-road matches:', len(nearest))
print('Mean nearest-road distance (m):', round(nearest.distance_m.mean(), 2))
print(nearest[['block_id', 'highway', 'distance_m']].head().to_string(index=False))
