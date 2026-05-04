import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

from sklearn.metrics import mean_squared_error, r2_score

diabetes_x, diabetes_y=datasets.load_diabetes(return_X_y=True)

diabetes_x=diabetes_x[:, np.newaxis, 2]

diabetes_x_train=diabetes_x[:-50]
diabetes_x_test=diabetes_x[-50:]

diabetes_y_train=diabetes_y[:-50]
diabetes_y_test=diabetes_y[-50:]

regr=linear_model.LinearRegression()

regr.fit(diabetes_x_train, diabetes_y_train)

diabetes_y_pred=regr.predict(diabetes_x_test)

print("Coefficients : \n", regr.coef_)

print("Mean squared Error : %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

print("Coefficient od determination : %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

plt.scatter(diabetes_x_test, diabetes_y_test, color="blue")
plt.plot(diabetes_x_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()