from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
table = pd.read_csv(ROOT / 'data' / 'week10_settlement_points.csv')
print('My Port Harcourt settlement point table')
print('rows:', len(table))
print('columns:', list(table.columns))
print('average buildings:', round(table['building_count'].mean(), 2))
print('coordinate range:', round(table.longitude.min(), 4), 'to', round(table.longitude.max(), 4))
