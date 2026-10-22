import pandas as pd

inflation_snapshot_2026_09_16 = pd.read_clipboard(sep="\t")

print(inflation_snapshot_2026_09_16.columns.tolist())
inflation_snapshot_2026_09_16["Difference"] =  inflation_snapshot_2026_09_16["Previous"] - inflation_snapshot_2026_09_16["Last"]
print(inflation_snapshot_2026_09_16)

inflation_snapshot_2026_09_16.to_csv(
    r"C:\Users\jedda\OneDrive\Dahlke Global Opportunities\3_research\uk/inflation_snapshot_2026_09_16.csv"
)