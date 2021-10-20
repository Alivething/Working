import pandas as pd

df = pd.read_csv("heights.csv")

print("Mean", df["height(cm)"].mean())
print("Median", df["height(cm)"].median())
print("Std", df["height(cm)"].std())
print("Max", df["height(cm)"].max())
print("Min", df["height(cm)"].min())

y = [df["height(cm)"].quantile(0.25), df["height(cm)"].quantile(0.5), df["height(cm)"].quantile(0.75)]
x = [25, 50, 75]

import matplotlib.pyplot as plt
plt.title("Percentile values")
plt.xlabel("%Percent")
plt.ylabel("Value")
plt.bar(x, y)
plt.show()
