# labelling and general naming conventions
import requests as req
import pandas as pd
import numpy as np


df = pd.DataFrame(pd.read_csv('articles.csv', sep='|'))
df_gofuckyourself = df.loc[df['content_type'].isin(['web'])]
print(df_gofuckyourself.loc[:, 'location'].to_numpy())