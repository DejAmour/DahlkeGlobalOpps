import yfinance as yf
import pandas as pd

One_yr_BM_Rets = yf.download(
    ["SSAC.L", "CRHG.L", "IGLH.L"],
    start= "2025-09-01",
    end= "2026-09-01",
    auto_adjust=False
)

print(One_yr_BM_Rets.head())

adjusted_close = One_yr_BM_Rets["Adj Close"]

adjusted_close.to_csv(
    r"C:\Users\jedda\Projects\DahlkeGlobalOpps\2_portfolio_data/bm_adjusted_close_prices.csv",
    index=True,
    index_label="Date"
)

