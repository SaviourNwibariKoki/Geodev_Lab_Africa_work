from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
lga = gpd.read_file(base, layer='lga_boundary')
roads = gpd.read_file(base, layer='roads_osm')
facilities = gpd.read_file(week / 'facilities_points.gpkg', layer='facilities')
fig, ax = plt.subplots(figsize=(9, 7))
lga.boundary.plot(ax=ax, color='black', linewidth=1.2, label='Port-Harcourt LGA')
roads.plot(ax=ax, color='lightgray', linewidth=0.25, label='Mapped roads')
facilities.plot(ax=ax, color='red', edgecolor='white', markersize=55, label='Example facilities')
ax.set_title('Port-Harcourt: GeoPandas layers and point locations')
ax.set_axis_off()
ax.legend(loc='lower left')
fig.tight_layout()
fig.savefig(week / 'facilities_map.png', dpi=180)
print('wrote facilities_map.png')
