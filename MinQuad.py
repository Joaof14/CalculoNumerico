import pandas as pd
import numpy as np
from math import log1p
from sympy import Symbol

def linear():
    pibpc_df = pd.read_excel("CalcN3/Tabela_pib_per_capita_brasileiro.xlsx")
    pibpc_df['xy'] = pibpc_df['Ano'] * pibpc_df["PIB per capita-valores correntes (Reais)"]
    pibpc_df["x²"] = pibpc_df['Ano'] * pibpc_df['Ano'] 
    print(pibpc_df.head())
    sumx2 = pibpc_df["x²"].sum()
    sumx = pibpc_df["Ano"].sum()
    sumy = pibpc_df["PIB per capita-valores correntes (Reais)"].sum()
    sumxy = pibpc_df["xy"].sum()
    n = pibpc_df["xy"].size
    a = (n*sumxy - sumx*sumy)/(sumx**2 - n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/(- sumx**2 + n*sumx2)
    print(str(a) + 'x +(' + str(b) + ')')


    print("Linear: R² = ")
linear()