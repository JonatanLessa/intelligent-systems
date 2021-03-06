import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.metrics import confusion_matrix

X=np.transpose(np.array([[2.5 ,1.7, 4.0, 2.3 ,3.7, 4.8, 1.9, 5.3, 3.1, 1.9, 2.3, 3.6, 4.7, 5.8, 6.0, 3.9, 2.4, 1.7, 3.7 ,4.8 ,3.2 ,2.7, 1.2, 8.2, 1.8, 2.5, 2.2, 4.0, 4.2, 3.7, 2.4, 1.6, 2.0, 2.5, 3.8, 4.3, 2.0, 5.2, 2.4, 2.6, 1.3, 3.8, 4.5, 3.0, 2.1, 1.9, 5.0, 2.2, 1.3, 1.7, 3.0, 3.0, 3.5, 5.8, 4.8, 2.3, 2.6, 1.8, 2.9, 3.2, 4.2, 2.6, 6.0, 4.5, 1.3, 2.4, 4.3, 1.8, 2.4],
[3 ,3, 2, 2 ,4, 1, 3, 2, 4, 3, 4, 1, 2, 2, 4, 3, 4, 4, 2 ,1 ,2 ,3, 3, 5, 1, 1, 3, 1, 1, 1, 2, 3, 1, 3, 1, 2, 2, 2, 3, 4, 2, 1, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 1, 3, 2, 2, 2, 1, 1, 1, 1, 3, 2, 2, 2, 0, 2],
[1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0 ,0 ,1 ,1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]]))

Y=np.transpose(np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]))

from sklearn.linear_model import LogisticRegression, LinearRegression
from scipy.special import expit

# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, Y)

y_previsto= clf.predict(X[:])
#clf.predict_proba(X[:2, :])
clf.score(X, Y)
# y_true = [2, 0, 2, 2, 0, 1]
# y_pred = [0, 0, 2, 2, 0, 2]

confusion_matrix(Y, y_previsto)