from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

INPUT = Path('port_harcourt_waste_accessibility_analysis_ready.gpkg')
OUTPUT = Path('week4_roads_100m_buffer.gpkg')
MAP = Path('week4_100m_road_access_buffer.png')
BUFFER_M = 100
TARGET_CRS = 'EPSG:32632'

# Expectation written before running: one buffer feature per road feature, about
# 4,994 features, each representing the area within 100 m of that road feature.
roads = gpd.read_file(INPUT, layer='roads_osm')
boundary = gpd.read_file(INPUT, layer='lga_boundary')
settlements = gpd.read_file(INPUT, layer='settlements')

assert roads.crs.to_string() == TARGET_CRS
assert boundary.crs.to_string() == TARGET_CRS
assert settlements.crs.to_string() == TARGET_CRS

# One spatial operation: buffer every road feature by 100 metres. The GeoPackage
# driver may expose its internal fid or omit it, so retain the available fields.
keep_fields = [c for c in ['fid', 'osm_id', 'highway', 'name', 'geometry'] if c in roads.columns]
buffered = roads[keep_fields].copy()
original_count = len(buffered)
original_length_m = buffered.geometry.length
buffered['geometry'] = buffered.geometry.buffer(BUFFER_M)
buffered['buffer_m'] = BUFFER_M
buffered = gpd.GeoDataFrame(buffered, geometry='geometry', crs=TARGET_CRS)

if OUTPUT.exists():
    OUTPUT.unlink()
buffered.to_file(OUTPUT, layer='roads_100m_buffer', driver='GPKG', index=False)

# Four checks: map, row count, one feature by hand, and empty geometry.
empty_geometries = int(buffered.geometry.is_empty.sum())
null_geometries = int(buffered.geometry.isna().sum())
first_area = float(buffered.geometry.iloc[0].area)
first_length = float(original_length_m.iloc[0])
approx_straight_area = 2 * BUFFER_M * first_length + 3.141592653589793 * BUFFER_M**2

# Map: show the buffer result with the study boundary and settlement outlines.
fig, ax = plt.subplots(figsize=(11, 9), dpi=180)
boundary.boundary.plot(ax=ax, color='#263238', linewidth=1.3, zorder=4)
settlements.boundary.plot(ax=ax, color='#7B8794', linewidth=0.25, alpha=0.7, zorder=2)
buffered.plot(ax=ax, color='#2B8CBE', edgecolor='none', alpha=0.28, zorder=1)
roads.plot(ax=ax, color='#145A86', linewidth=0.18, alpha=0.5, zorder=3)

ax.set_title('Port Harcourt: Areas Within 100 m of Mapped Roads', fontsize=16, fontweight='bold', pad=16)
ax.set_axis_off()
legend_items = [
    Patch(facecolor='#2B8CBE', edgecolor='none', alpha=0.45, label='100 m road buffer'),
    Line2D([0], [0], color='#145A86', linewidth=1.2, label='Mapped roads'),
    Line2D([0], [0], color='#7B8794', linewidth=1.0, label='Settlement boundaries'),
    Line2D([0], [0], color='#263238', linewidth=1.8, label='Port-Harcourt LGA boundary'),
]
ax.legend(handles=legend_items, loc='lower left', frameon=True, framealpha=0.95, title='Map layers')

# Scale bar: 5 km, placed in axes coordinates at lower right so it remains
# separate from the legend.
x0, x1, y = 0.76, 0.91, 0.075
ax.plot([x0, x1], [y, y], transform=ax.transAxes, color='black', linewidth=3, solid_capstyle='butt', zorder=10)
ax.plot([x0, x0], [y - 0.012, y + 0.012], transform=ax.transAxes, color='black', linewidth=1.5)
ax.plot([x1, x1], [y - 0.012, y + 0.012], transform=ax.transAxes, color='black', linewidth=1.5)
ax.text((x0 + x1) / 2, y + 0.018, '5 km', transform=ax.transAxes, ha='center', va='bottom', fontsize=9)
ax.text(0.99, 0.015, 'CRS: EPSG:32632 | Buffer distance: 100 m', transform=ax.transAxes, ha='right', va='bottom', fontsize=8, color='#455A64')
fig.savefig(MAP, bbox_inches='tight', facecolor='white')
plt.close(fig)

print('INPUT_ROADS', original_count)
print('OUTPUT_BUFFERS', len(buffered))
print('EXPECTED_OUTPUT', original_count)
print('EMPTY_GEOMETRIES', empty_geometries)
print('NULL_GEOMETRIES', null_geometries)
print('FIRST_ROAD_LENGTH_M', round(first_length, 3))
print('FIRST_BUFFER_AREA_M2', round(first_area, 3))
print('FIRST_BUFFER_STRAIGHT_LINE_APPROX_M2', round(approx_straight_area, 3))
print('OUTPUT', OUTPUT)
print('MAP', MAP)
