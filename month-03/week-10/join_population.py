from pathlib import Path
import geopandas as gpd
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
wards = pd.read_csv(ROOT / 'wards.csv')
pop = pd.read_csv(ROOT / 'data' / 'ward_population_2024.csv')
joined = wards.merge(pop, on='ward', how='left', validate='one_to_one')
print('matched population values:', joined['population_2024'].notna().sum(), 'of', len(joined))
print(joined.head().to_string(index=False))
