from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[2]
table = pd.read_csv(ROOT / 'port_harcourt_settlements.csv')
print('shape:', table.shape)
print('columns:', list(table.columns))
print(table.head(3).to_string(index=False))
print('missing values:', table.isna().sum().to_dict())
