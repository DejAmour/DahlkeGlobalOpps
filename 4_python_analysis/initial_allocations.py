import pandas as pd

initial_allocations = pd.DataFrame({"sleeve": ["US Equities", "UK equities", "EU ex UK equities", "Jap equities", "EM", "Gov bonds", "Strat bonds"],
                                    "asset_class": ["Equity", "Equity", "Equity", "Equity", "Equity", "Fixed Income", "Fixed Income"],
                                   "target_weight": [0.4, 0.1, 0.05, 0.03, 0.02, 0.2, 0.2]})
print(initial_allocations)

initial_allocations.to_csv(
    r"C:\Users\jedda\OneDrive\Dahlke Global Opportunities\2_portfolio_data/initial_allocations.csv",
    index=False
)

allocation_weight_by_class = initial_allocations.groupby("asset_class")["target_weight"].sum()
print(allocation_weight_by_class)