from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
for layer in ['lga_boundary', 'settlements']:
    frame = gpd.read_file(base, layer=layer)
    invalid_before = (~frame.geometry.is_valid).sum()
    fixed = frame.copy()
    fixed['geometry'] = fixed.geometry.make_valid()
    invalid_after = (~fixed.geometry.is_valid).sum()
    print(f'{layer}: invalid before={invalid_before}, invalid after={invalid_after}, empty={fixed.geometry.is_empty.sum()}')
