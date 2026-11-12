from pathlib import Path
import geopandas as gpd
ROOT = Path(__file__).resolve().parents[2]
settlements = gpd.read_file(ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg', layer='settlements')
print('Own settlement CRS:', settlements.crs)
print('EPSG:32632 is the correct projected CRS for this Port Harcourt work.')
print('Area of all settlement polygons (m2):', round(settlements.geometry.area.sum(), 2))
