from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
lga = gpd.read_file(base, layer='lga_boundary')
roads = gpd.read_file(base, layer='roads_osm')
clipped = gpd.clip(roads, lga)
buffered = clipped.buffer(200)
dissolved = gpd.GeoDataFrame({'operation': ['200 m road access area'], 'geometry': [buffered.union_all()]}, crs=roads.crs)
dissolved.to_file(week / 'roads_200m_dissolved.gpkg', layer='road_access', driver='GPKG')
print('Roads clipped:', len(clipped))
print('Dissolved output features:', len(dissolved))
print('Wrote roads_200m_dissolved.gpkg')
