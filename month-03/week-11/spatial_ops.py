from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
roads = gpd.read_file(base, layer='roads_osm').head(100)
settlements = gpd.read_file(base, layer='settlements')
road_buffer = roads.buffer(100)
intersections = gpd.overlay(settlements[['block_id', 'geometry']], gpd.GeoDataFrame({'geometry': road_buffer}, crs=roads.crs), how='intersection')
print('100 m road buffers created:', len(road_buffer))
print('Settlement-buffer intersections:', len(intersections))
print('CRS used for metre operation:', roads.crs)
