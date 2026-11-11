from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
path = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
for layer in ['lga_boundary', 'settlements', 'roads_osm']:
    frame = gpd.read_file(path, layer=layer)
    print(f'{layer}: rows={len(frame)}, geometry={frame.geometry.geom_type.iloc[0]}, CRS={frame.crs.to_string()}, bounds={tuple(round(x, 2) for x in frame.total_bounds)}')
