## Comparing bm rets vs portfolio rets

import pandas as pd
from project_paths import DATA_DIR

current_holdings = pd.read_csv(DATA_DIR / "current_holdings.csv")
allocation = pd.read_csv(DATA_DIR / "initial_allocations.csv")
bm_weights = pd.read_csv(DATA_DIR / "benchmark_weights.csv")
bm_prices = pd.read_csv(
    DATA_DIR / "bm_adjusted_close_prices.csv",
    index_col="Date",
    parse_dates=["Date"])

returns = bm_prices.pct_change(fill_method=None)

def calculate_weighted_returns(asset_returns, weights_table):
    weights = weights_table.set_index("ticker")["weight"]
    weights = weights.reindex(asset_returns.columns)
    
    if abs(weights.sum() - 1) > 1e-10:
        raise ValueError("weights do not sum to one")

    port_ret_contribs = asset_returns.mul(weights, axis=1).dropna()

    total_daily_returns = (
        port_ret_contribs[asset_returns.columns].sum(axis=1, min_count=1)
    )

    return total_daily_returns

bm_daily_returns = calculate_weighted_returns(returns, bm_weights)
port_daily_returns = calculate_weighted_returns(returns, current_holdings)

performance_returns = pd.concat(
    [
        port_daily_returns.rename("Portfolio"),
        bm_daily_returns.rename("Benchmark")
    ],
axis=1
)

cum_perf_rets = ((1+performance_returns).cumprod())*100

performance_index = (
    cum_perf_rets / cum_perf_rets.iloc[0] * 100
)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7,4))

performance_index.plot(ax=ax)
ax.set_title("Portfolio vs Benchmark")
ax.set_xlabel("Date")
ax.set_ylabel("Growth of 100")
ax.grid(True, alpha=0.3)
ax.axhline(100, color="grey", linewidth=1, linestyle="--")
fig.tight_layout()
fig.savefig("22102026_portfolio_performance.png", dpi=300)
plt.show()
