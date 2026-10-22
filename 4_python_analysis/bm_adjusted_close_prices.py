import pandas as pd

adjusted_prices = pd.read_csv(
    r"C:\Users\jedda\OneDrive\Dahlke Global Opportunities\2_portfolio_data/bm_adjusted_close_prices.csv",
    index_col="Date",
    parse_dates=["Date"]

)

monthly_adj_close = adjusted_prices.resample("ME").last()

print(monthly_adj_close)

monthly_ret = monthly_adj_close.pct_change().dropna()
BM_weights = pd.Series({"SSAC.L": 0.6,
                        "CRHG.L": 0.2,
                        "IGLH.L": 0.2})

bm_portfolio_ret = monthly_ret.dot(BM_weights)
print(bm_portfolio_ret)
growth_factors = 1+bm_portfolio_ret
cumalative_bm_ret = growth_factors.prod()-1
print(cumalative_bm_ret)
bm_cum_val = 100*growth_factors.cumprod()
print(bm_cum_val)

bm_history = monthly_ret.copy()
bm_history["BM Cumalative Val"] = bm_cum_val
bm_history["BM Ret"] = cumalative_bm_ret
bm_history.to_csv(
    r"C:\Users\jedda\OneDrive\Dahlke Global Opportunities\2_portfolio_data/bm_history.csv",
    index=True,
    index_label="Date"
)