import numpy as np, pandas as pd, matplotlib.pyplot as plt

obs = 10_000
reps = 1_000
beta = 2
beta_estimates = []

# Monte Carlo Simulation
for _ in range(reps):
    x = np.random.normal(0, 9, obs)
    u = np.random.normal(0, 36, obs)
    y = 3 + beta*x + u
    cov_mtx = np.cov(x, y) # np.array([[var(x), cov(x,y)], [cov(y,x), var(y)]])
    beta_estimates.append(cov_mtx[0, 1] / cov_mtx[0, 0])
e_beta_expected = round(np.array(beta_estimates).mean())
assert(e_beta_expected == beta) # E(beta_hat) = beta, unbiasedness holds

# Summary
pd.Series(beta_estimates).describe().to_frame('beta').T.iloc[:, :3]

# Distribution
pd.Series(beta_estimates).plot.hist(color = 'grey', bins = 40, linewidth = .5, edgecolor = 'k' )
plt.ylabel('Density')
plt.xlabel('_b[x]')
plt.title('Distribution of coefficients from Monte Carlo simulation')
plt.show()