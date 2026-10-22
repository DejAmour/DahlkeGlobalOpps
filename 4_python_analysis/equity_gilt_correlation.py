import pandas as pd
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

correlation = (weekly_rets["IGLT.L"]
               .rolling(26)
               .corr
               (weekly_rets["SSAC.L"])
               .dropna()
               )
PctChange_26Wk = weekly_adj_prices.pct_change(26)


PosEq = PctChange_26Wk["SSAC.L"][PctChange_26Wk["SSAC.L"]>0]

NegBd = PctChange_26Wk["IGLT.L"][PctChange_26Wk["SSAC.L"]<0]
PosBd = PctChange_26Wk["IGLT.L"][PctChange_26Wk["SSAC.L"]>0]

equity_downturn_condition = (
    PctChange_26Wk.loc[correlation.index, "SSAC.L"] < 0
)

NegEqCorr = correlation[equity_downturn_condition]

## Testing whether there is a higher correlation during equity downturns or upturns

equity_upturn_condition = (
    PctChange_26Wk.loc[correlation.index, "SSAC.L"] > 0
)

PosEqCorr = correlation[equity_upturn_condition]


print(NegEqCorr)
print(NegEqCorr.mean())
print(len(NegEqCorr))

print(PosEqCorr)
print(PosEqCorr.mean())
print(len(PosEqCorr)+len(NegEqCorr))

## Seeing Gilt rets during equity upturns and downturns

AlignedGiltRets = PctChange_26Wk.loc[
    correlation.index,
    "IGLT.L"
]

giltRetsDuringEqDownturn = AlignedGiltRets[equity_downturn_condition]
print(giltRetsDuringEqDownturn.mean())
print(giltRetsDuringEqDownturn.median())

positiveGilt = giltRetsDuringEqDownturn > 0
print(positiveGilt.mean())

giltRetsDuringEqUpturn = AlignedGiltRets[equity_upturn_condition]
print(giltRetsDuringEqUpturn.mean())
print(giltRetsDuringEqUpturn.median())

posGiltEqUp = giltRetsDuringEqUpturn > 0
print(f"posGiltEqUp Mean: {posGiltEqUp.mean()}")

print(len(giltRetsDuringEqUpturn))
import matplotlib.pyplot as plt
