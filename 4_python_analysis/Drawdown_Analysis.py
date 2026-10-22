import pandas as pd
import numpy as np
import yfinance as yf

gilt_equity_bm_rets = yf.download(
    ["SSAC.L", "IGLT.L"],
        start= "2020-01-01",
        end= "2026-09-01",
        auto_adjust=False
)

fridayEnd_GiltEqRets = gilt_equity_bm_rets.resample("W-FRI").last()

weekly_adj_prices = fridayEnd_GiltEqRets["Adj Close"]

weekly_rets = weekly_adj_prices.pct_change().dropna()

## Want to see if holding gilts had diversification benefits.
## Contruct 60/40 port and 100 eq port and compare drawdowns
## need two series, running max port val and current port val
## max/current - 1 = drawdown
## compare drawdowns between ports

## 60/40

allocation_6040 = [0.4, 0.6]
portfolio_rets_6040 = weekly_rets.dot(allocation_6040)
portfolio_rets_6040_factor = 1+portfolio_rets_6040

cumPortVal = 100*portfolio_rets_6040_factor.cumprod()
runningMax6040 = cumPortVal.cummax()
MaxDD6040 = (runningMax6040/cumPortVal)-1

## 100 Eq
EqRets = weekly_rets["SSAC.L"]
EqRetsFactor = 1+EqRets
CumPortEqVal = 100*EqRetsFactor.cumprod()
runningMax100 = CumPortEqVal.cummax()
MaxDD100 = (runningMax100/CumPortEqVal)-1

print(MaxDD6040.idxmax())
print(MaxDD100.idxmax())

