import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dlry=pd.read_csv(r"deliveries.csv")
dlry.head()

dlry.shape

dlry.isnull().sum()

sns.heatmap(dlry.isnull(), cmap="summer")
plt.show()

mat=pd.read_csv(r"matches.csv")
mat.head()

mat.shape

mat.isnull().sum()

sns.heatmap(mat.isnull(), cmap="summer")
plt.show()