print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

x, y=make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)

clf=SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)

clf.fit(x, y)

xx=np.linspace(-1, 5, 10)
yy=np.linspace(-1, 5, 10)

X1, X2=np.meshgrid(xx, yy)
z=np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1=val
    x2=X2[i, j]
    p=clf.decision_function([[x1, x2]])
    z[i, j]=p[0]
levels=[-1.0, 0.0, 1.0]
linestyles=["dashed", "solid", "dashed"]
colors="k"
plt.contour(X1, X2 ,z, levels, colors=colors, linestyles=linestyles)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Paired, edgecolor="black", s=20)
plt.axis("tight")
plt.show()