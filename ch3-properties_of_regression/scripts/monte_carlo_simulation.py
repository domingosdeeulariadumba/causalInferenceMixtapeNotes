# Dependencies
import numpy as np, pandas as pd, matplotlib.pyplot as plt

# Observations, repetitions, slope, and an empty slope list 
obs, reps, beta, beta_estimates = 10_000, 1_000, 2, []

# Monte Carlo Simulation
for _ in range(reps):
    x = np.random.normal(0, 9, obs)
    u = np.random.normal(0, 36, obs)
    y = 3 + beta*x + u
    cov_mtx = np.cov(x, y) # np.array([[var(x), cov(x,y)], [cov(y,x), var(y)]])
    beta_hat = cov_mtx[0, 1] / cov_mtx[0, 0]
    beta_estimates.append(beta_hat)
e_beta_hat = round(np.array(beta_estimates).mean())
assert(e_beta_hat == beta) # E(beta_hat) = beta, unbiasedness holds

# Summary
beta_estimates_series = pd.Series(beta_estimates)
beta_estimates_series.describe().to_frame('beta').T.iloc[:, :3]

# Distribution
beta_estimates_series.plot.hist(color = 'grey', bins = 40, linewidth = .5, edgecolor = 'k' )
plt.ylabel('Density')
plt.xlabel('_b[x]')
plt.title('Distribution of coefficients from Monte Carlo simulation')
plt.show()