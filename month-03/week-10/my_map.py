from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
settlements = gpd.read_file(base, layer='settlements')
lga = gpd.read_file(base, layer='lga_boundary')
fig, ax = plt.subplots(figsize=(9, 7))
settlements.plot(ax=ax, column='building_count', cmap='YlOrRd', legend=True, linewidth=0)
lga.boundary.plot(ax=ax, color='navy', linewidth=1.5)
ax.set_title('Port-Harcourt settlement blocks by building count')
ax.set_axis_off()
fig.tight_layout()
fig.savefig(week / 'my_map.png', dpi=180)
print('wrote my_map.png')
