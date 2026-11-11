from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
week = Path(__file__).resolve().parent
wards = pd.read_csv(ROOT / 'wards.csv')
pop = pd.read_csv(ROOT / 'data' / 'ward_population_2024.csv')
joined = wards.merge(pop, on='ward', how='left', validate='one_to_one')
joined.to_csv(week / 'wards_table.csv', index=False)
print(f'wrote {len(joined)} rows to wards_table.csv')
