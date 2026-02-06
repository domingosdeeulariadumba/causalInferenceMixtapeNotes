# Dependencies
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Data Generation, model fitting, and prediction
np.random.seed(1234)
n = 10
x = 9 * np.random.randn(n)
u = 36 * np.random.randn(n)
y = 3 + 2*x + u
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
yhat = model.predict(X)
uhat = y - yhat
pd.Series(uhat).describe() # su residuals

# Summarized output
df = pd.DataFrame({
    'x': x,
    'u': u,
    'y': y,
    'yhat': yhat,
    'residuals': uhat
})
print(df)

# collapse (sum) x u y yhat residuals
collapsed = df.sum().to_frame('Sum').T
print(collapsed)

# Verifying residuals sum to ~0
assert round(uhat.sum(), 10) == 0