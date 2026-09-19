import geopandas as gpd
from pathlib import Path

path = Path('port_harcourt_waste_accessibility_analysis_ready.gpkg')
layers = {}
for name in ['lga_boundary', 'settlements', 'roads_osm', 'waste_points_osm']:
    layers[name] = gpd.read_file(path, layer=name)

print('CRS')
for name, gdf in layers.items():
    print(name, gdf.crs.to_string() if gdf.crs else None)

print('\nGEOMETRY VALIDITY')
for name, gdf in layers.items():
    if gdf.empty:
        print(name, 'empty; no invalid geometries to test')
    else:
        print(name, 'invalid=', int((~gdf.geometry.is_valid).sum()), 'null_geom=', int(gdf.geometry.isna().sum()))

print('\nDUPLICATES')
for name, gdf in layers.items():
    cols = [c for c in gdf.columns if c != gdf.geometry.name]
    print(name, 'duplicate_attribute_rows=', int(gdf.duplicated(subset=cols).sum()) if cols else 0)

print('\nMISSING ATTRIBUTES')
for name, gdf in layers.items():
    non_geom = [c for c in gdf.columns if c != gdf.geometry.name]
    missing = {c: int(gdf[c].isna().sum()) for c in non_geom if int(gdf[c].isna().sum()) > 0}
    print(name, missing if missing else 'none')

print('\nCOVERAGE / CLIPPING')
boundary = layers['lga_boundary'].geometry.union_all()
for name in ['settlements', 'roads_osm', 'waste_points_osm']:
    gdf = layers[name]
    if gdf.empty:
        print(name, 'empty')
    else:
        outside = (~gdf.geometry.intersects(boundary)).sum()
        print(name, 'outside_boundary=', int(outside), 'features=', len(gdf))
