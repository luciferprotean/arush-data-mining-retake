import pandas as pd
import numpy as np
import matplotlib as mpt
import seaborn as sb

base_df=pd.read_csv("matched_records_filteredLoc.csv")

base_df.fillna(0, inplace=True)

base_df.to_csv("records_cleaned.csv", index=False, encoding='utf-8-sig')

print(base_df.head())