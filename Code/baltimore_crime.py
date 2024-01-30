import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np

import seaborn as sns
sns.set_palette('Set2')
sns.set_style(style = 'darkgrid')
import matplotlib.pyplot as plt
plt.figure(figsize = (8,5))

df = pd.read_csv("/Users/ivangrandov/Downloads/BPD_Part_1_Victim_Based_Crime_Data.csv")
print(df.columns())