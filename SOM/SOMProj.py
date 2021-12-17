import numpy
import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

data = pd.read_csv("SOM/som.csv")

quick = []
curr = []
debt = []
for i in range(0,10):
    quick.append(round((data.TCA[i] - data.A[i])/data.TCL[i], 3))
    curr.append(round(data.TOR[i]/data.TCL[i], 3))
    debt.append(round(data.TCA[i]/data.PL[i], 3))

years=[2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
# datfrm = DataFrame((quick, curr, debt), index=['Quick', 'Current Turnover', 'Debt Turnover'], columns=years)
# datfrm = datfrm.transpose()

# datfrm.to_csv("Vals.csv")

plt.bar(years, debt, width=0.5)
plt.show()