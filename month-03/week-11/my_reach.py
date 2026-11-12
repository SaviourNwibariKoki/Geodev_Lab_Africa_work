from pathlib import Path
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
base = ROOT / 'port_harcourt_waste_accessibility_analysis_ready.gpkg'
lga = gpd.read_file(base, layer='lga_boundary')
settlements = gpd.read_file(base, layer='settlements')
facilities = pd.read_csv(ROOT / 'data' / 'facilities.csv')
points = gpd.GeoDataFrame(facilities, geometry=gpd.points_from_xy(facilities.longitude, facilities.latitude), crs=4326).to_crs(32632)
reach = gpd.GeoDataFrame({'geometry': [points.buffer(2000).union_all()]}, crs=32632)
covered = gpd.overlay(lga[['geometry']], reach, how='intersection')
covered_area = covered.geometry.area.sum()
print('Own-data facilities:', len(points))
print('Port-Harcourt LGA covered within 2 km:', round(covered_area / lga.geometry.area.sum() * 100, 2), '%')
fig, ax = plt.subplots(figsize=(9, 7))
lga.boundary.plot(ax=ax, color='black', linewidth=1)
settlements.plot(ax=ax, color='lightgray', alpha=0.7, linewidth=0, label='Settlements')
reach.plot(ax=ax, color='green', alpha=0.35, label='2 km facility reach')
points.plot(ax=ax, color='red', edgecolor='white', markersize=50, label='Facilities')
ax.set_title('Port-Harcourt facility reach: 2 km dissolved buffers')
ax.set_axis_off()
ax.legend(loc='lower left')
fig.tight_layout()
fig.savefig(week / 'my_reach.png', dpi=180)
