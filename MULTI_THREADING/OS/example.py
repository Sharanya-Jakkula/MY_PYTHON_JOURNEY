import pandas as pd
import openpyxl as op
data=pd.read_excel("/home/rgukt123/Hackathon/TEMP/HELLO/simple_data.xlsx",engine="openpyxl")
df=pd.DataFrame(data)
print(df)