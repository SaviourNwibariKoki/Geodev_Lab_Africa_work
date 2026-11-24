import rasterio
from _common import SCENE
with rasterio.open(SCENE) as src:
    for row, col in [(0, 0), (src.height // 2, src.width // 2), (src.height - 1, src.width - 1)]:
        x, y = src.xy(row, col)
        print(f'row={row}, col={col} -> x={x:.2f}, y={y:.2f}')
