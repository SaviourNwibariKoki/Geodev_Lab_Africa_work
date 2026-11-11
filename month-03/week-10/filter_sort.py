from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
table = pd.read_csv(ROOT / 'port_harcourt_settlements.csv')
large = table[table['building_count'] >= 50].sort_values('block_area_sqm', ascending=False)
print('settlements with at least 50 buildings:', len(large))
print(large[['block_id', 'block_area_sqm', 'building_count']].head(5).to_string(index=False))
