import pandas as pd
data = pd.read_csv("regions.csv")

print(data.Regions.unique())