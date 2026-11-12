from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
settlements = gpd.read_file(base, layer='settlements')
roads = gpd.read_file(base, layer='roads_osm')
centres = settlements[['block_id', 'geometry']].copy()
centres['geometry'] = centres.geometry.centroid
road_area = gpd.GeoDataFrame({'geometry': [roads.buffer(100).union_all()]}, crs=roads.crs)
counted = gpd.sjoin(centres, road_area, predicate='within', how='left')
print('Settlement centres within 100 m of mapped roads:', counted['index_right'].notna().sum(), 'of', len(counted))
