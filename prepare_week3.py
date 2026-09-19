from pathlib import Path
import geopandas as gpd

INPUT = Path('port_harcourt_waste_accessibility.gpkg')
OUTPUT = Path('port_harcourt_waste_accessibility_analysis_ready.gpkg')
TARGET_CRS = 'EPSG:32632'  # WGS 84 / UTM zone 32N; metres

layers = {
    'lga_boundary': gpd.read_file(INPUT, layer='lga_boundary'),
    'settlements': gpd.read_file(INPUT, layer='settlements'),
    'roads_osm': gpd.read_file(INPUT, layer='roads_osm'),
    'waste_points_osm': gpd.read_file(INPUT, layer='waste_points_osm'),
}

boundary = layers['lga_boundary'].to_crs(TARGET_CRS)
prepared = {'lga_boundary': boundary}

# Keep only features intersecting the exact study-area boundary, then clip them.
for name in ('settlements', 'roads_osm', 'waste_points_osm'):
    layer = layers[name].to_crs(TARGET_CRS)
    if layer.empty:
        prepared[name] = layer
    else:
        prepared[name] = gpd.clip(layer, boundary)

if OUTPUT.exists():
    OUTPUT.unlink()

for name, layer in prepared.items():
    layer.to_file(OUTPUT, layer=name, driver='GPKG', index=False)

print(f'Created {OUTPUT}')
for name, layer in prepared.items():
    print(name, 'features=', len(layer), 'crs=', layer.crs, 'geometry=', layer.geometry.geom_type.unique().tolist())
