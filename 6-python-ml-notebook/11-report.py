import matplotlib
import statsmodels.api as sm
from sklearn.datasets import load_diabetes

matplotlib.rcParams.update({'font.size': 12})

diabetes = load_diabetes()
columns_names = diabetes.feature_names
y = diabetes.target
X = diabetes.data

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())
