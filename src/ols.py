import numpy as np
import pandas as pd
from scipy import stats


def fit_ols(X, y):
    names = ["const"] + list(X.columns)
    X = X.to_numpy(dtype=float)
    y = y.to_numpy(dtype=float)

    # add an intercept column of ones, then fit the coefficients
    X1 = np.column_stack([np.ones(len(X)), X])
    n, k = X1.shape
    assert np.linalg.matrix_rank(X1) == k, "X has linearly dependent columns"
    beta = np.linalg.lstsq(X1, y, rcond=None)[0]

    # residuals and their variance
    fitted = X1 @ beta
    resid = y - fitted
    ssr = resid @ resid
    dof = n - k
    sigma2 = ssr / dof

    # standard errors, t-tests and 95% confidence intervals
    XtX_inv = np.linalg.inv(X1.T @ X1)
    se = np.sqrt(sigma2 * np.diag(XtX_inv))
    t = beta / se
    p_value = 2 * stats.t.sf(np.abs(t), dof)
    t_crit = stats.t.ppf(0.975, dof)
    ci_low = beta - t_crit * se
    ci_high = beta + t_crit * se

    # share of variance explained
    sst = ((y - y.mean()) ** 2).sum()
    r2 = 1 - ssr / sst
    adj_r2 = 1 - (1 - r2) * (n - 1) / dof

    table = pd.DataFrame(
        {"coef": beta, "se": se, "t": t, "p": p_value, "ci_low": ci_low, "ci_high": ci_high},
        index=names,
    )
    return {
        "table": table, "r2": r2, "adj_r2": adj_r2, "sigma2": sigma2,
        "dof": dof, "resid": resid, "XtX_inv": XtX_inv,
        "fitted": fitted, "names": names,
    }
