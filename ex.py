import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ex = pd.DataFrame({"foo": ['one', 'one', 'two', 'two', 'three', 'three', 'four', 'four'],
                   "bar": ['A', 'A', 'B', 'B', 'A', 'C', 'B', 'C'],
                   "baz": [1, 2, 3, 4, 5, 6, 7, 8]})
# make into pivot table format
ex_sum = ex.groupby(['foo','bar']).sum()

print(ex_sum)

ex_sum_p = ex_sum.pivot(ex_sum['foo'], ex_sum['bar'], ex_sum['baz'])

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(ex_sum_p, annot=True, fmt="d", linewidths=.5, ax=ax)