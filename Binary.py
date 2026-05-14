import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("insurance_data.csv")
df.head()

plt.scatter(df.age, df.bought_insurance, marker="+", color="red")
plt.show()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(df[["age"]], df.bought_insurance, train_size=0.8)

x_test

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train, y_train)

x_test

y_predicted=model.predict(x_test)

model.predict_proba(x_test)

model.score(x_test, y_test)

y_predicted

x_test

model.coef_

model.intercept_

import math
def sigmoid(x):
    a= 1/(1+math.exp(-x))
    print(a)

def prediction_func(age):
    z=0.042*age-1.53
    y=sigmoid(z)
    print (y)

age=35
prediction_func(age)

age=43
prediction_func(age)