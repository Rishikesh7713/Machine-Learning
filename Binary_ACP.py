import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

dt=load_breast_cancer()

plt.scatter(dt.target, dt.target_names, marker="x", color="green")
plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(dt[["target"]], dt.target_names, train_size=0.8)
x_test
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train, y_train)

x_test

y_pred=model.predict(x_test)

model.predict_proba(x_test)

model.score(x_test, y_test)

y_pred

x_test

model.coef_

model.intercept_

import math
def sigmoid(x):
    a=1/(1+math.exp(-x))
    print(a)

def prediction(target):
    z=0.042*target-1.53
    y=sigmoid(z)
    print(y)

target=12
prediction(target)

target=42
prediction(target)