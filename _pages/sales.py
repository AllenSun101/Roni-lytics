import pandas as pd
   
df = pd.read_csv("https://raw.githubusercontent.com/Aran203/ronis-viz-td-2024/refs/heads/main/data/data_full.csv?token=GHSAT0AAAAAACR3LQDGXQQA76ROQELPMSQIZZP35TA", parse_dates = ["Sent Date"])

print(df)