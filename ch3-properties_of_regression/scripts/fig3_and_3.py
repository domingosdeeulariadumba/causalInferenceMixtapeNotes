# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Data Generation, model fitting, and prediction
np.random.seed(1)
n = 10_000
x = np.random.randn(n)
u = np.random.randn(n)
y = 5.5 * x + 12 * u
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
yhat1 = model.predict(X)

# y_hat summary
intercept, slope = model.intercept_, model.coef_[0]
yhat2 = intercept + slope * x # Just to handle PRNG differences between Stata and Python instead of using the prameters inserted manually by Scott 
df_yhat = pd.DataFrame({'yhat1': yhat1, 'yhat2': yhat2})
df_yhat.describe() # sum yhat*

# residuals summary
uhat1 = y - yhat1
uhat2 = y - yhat2
df_uhat = pd.DataFrame({'uhat1': uhat1, 'uhat2': uhat2})
df_uhat.describe() # sum uhat*

# Graphical representations
_, axes = plt.subplots(1, 2, figsize = (14, 5))
data = pd.DataFrame({'x': x, 'y': y})
# OLS Regression Line
sns.regplot(
    data, x = x , y = y, color = 'k', marker = '.', ax = axes[0],
    line_kws = dict(linewidth = 1, alpha = .5, label = 'Fitted values y')
    )
axes[0].axhline(0, color = 'k', linestyle = '--')
axes[0].set_xlabel('')
axes[0].set_ylabel('')
axes[0].set_title('OLS Regression Line')
axes[0].legend(loc = 'lower center')
# Residual vs fitted values plot (rvfplot)
sns.residplot(
    data, x = 'x', y = 'y', color = 'grey', ax = axes[1],
    line_kws = dict(linestyle = '-')
              )
axes[1].set_xlabel('Fitted values')
axes[1].set_ylabel('Residuals')
axes[1].set_title('Residuals vs Fitted Values')
plt.tight_layout()
plt.show()