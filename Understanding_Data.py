import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic=pd.read_csv(r"titanic.csv")
titanic.head()

titanic.shape

titanic.isnull().sum()

sns.heatmap(titanic.isnull(), cmap="spring")

titanic.head()

titanic.drop("deck", axis=1, inplace=True, errors="ignore")

titanic.head()

titanic.dropna(inplace=True)

sns.heatmap(titanic.isnull(), cbar=False)

titanic.isnull().sum()

pd.get_dummies(titanic["Sex"]).head()

sex=pd.get_dummies(titanic["Sex"], drop_first=True)

sex.head(4)

pd.get_dummies(titanic["embarked"]).head(4)

arked=pd.get_dummies(titanic["embarked"], drop_first=True)

pclass=pd.get_dummies(titanic["pclass"], drop_first=True)

pclass.head(4)

titanic=pd.concat([titanic, sex, pclass] ,axis=1)

titanic.head()