import pandas as pd
import numpy as np
from math import log, exp
import SistLinear

dict1 = {'Ano' : [1,2,3,4],
        'PIB per capita-valores correntes (Reais)': [3,5,6,8]}

dict2 = {'Ano' : [1,3,4,7],
        'PIB per capita-valores correntes (Reais)': [0.5,1,3,4.5]}

e = exp(1)
def ln(x):
    return log(x, e)



def linear():
    #construindo tabela
    pibpc_df = pd.read_excel("CalcN3/Tabela_pib_per_capita_brasileiro.xlsx")
    #pibpc_df = pd.DataFrame(dict1)
    pibpc_df['xy'] = pibpc_df['Ano'] * pibpc_df["PIB per capita-valores correntes (Reais)"]
    pibpc_df["x²"] = pibpc_df['Ano'] * pibpc_df['Ano'] 
    print(pibpc_df.head())

    #somas
    sumx2 = pibpc_df["x²"].sum()
    sumx = pibpc_df["Ano"].sum()
    sumy = pibpc_df["PIB per capita-valores correntes (Reais)"].sum()
    sumxy = pibpc_df["xy"].sum()

    #calculo coeficientes
    n = pibpc_df["xy"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    print(str(a) + '*x +(' + str(b) + ')')


    # calculando R²
    ymedio = pibpc_df["PIB per capita-valores correntes (Reais)"].mean()
    pibpc_df['SQREG'] = (ymedio - (a * pibpc_df['Ano']) - b)**2
    pibpc_df["SQTOT"] = (ymedio - pibpc_df["PIB per capita-valores correntes (Reais)"] )**2
    r2 = pibpc_df['SQREG'].sum()/pibpc_df['SQTOT'].sum()
    print("Linear: R² = " + str(r2))






def logaritmico():
    #construindo tabela
    pibpc_df = pd.read_excel("CalcN3/Tabela_pib_per_capita_brasileiro.xlsx")
    #pibpc_df = pd.DataFrame(dict1)
    pibpc_df['Ln Ano'] = pibpc_df['Ano'].apply(ln)
    pibpc_df['yLnx'] = pibpc_df['Ln Ano'] * pibpc_df["PIB per capita-valores correntes (Reais)"]
    pibpc_df["(Ln x)²"] = pibpc_df['Ln Ano'] * pibpc_df['Ln Ano'] 
    print(pibpc_df.head())

    #somas
    sumx2 = pibpc_df["(Ln x)²"].sum()
    sumx = pibpc_df["Ln Ano"].sum()
    sumy = pibpc_df["PIB per capita-valores correntes (Reais)"].sum()
    sumxy = pibpc_df["yLnx"].sum()

    #calculo coeficientes
    n = pibpc_df["Ln Ano"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)

    # calculando R²
    ymedio = pibpc_df["PIB per capita-valores correntes (Reais)"].mean()
    pibpc_df['SQREG'] = (ymedio - (a * pibpc_df['Ln Ano']) - b)**2
    pibpc_df["SQTOT"] = (ymedio - pibpc_df["PIB per capita-valores correntes (Reais)"] )**2
    r2 = pibpc_df['SQREG'].sum()/pibpc_df['SQTOT'].sum()

    print("Logaritmico: R² = " + str(r2))

    print(str(a) + '*Lnx +(' + str(b) + ')')

def exponencial():

    # construindo a tabela
    pibpc_df = pd.read_excel("CalcN3/Tabela_pib_per_capita_brasileiro.xlsx")
    #pibpc_df = pd.DataFrame(dict1)
    pibpc_df['Ln y'] = pibpc_df['PIB per capita-valores correntes (Reais)'].apply(ln)
    pibpc_df['xLny'] = pibpc_df['Ano'] * pibpc_df["Ln y"]
    pibpc_df["x²"] = pibpc_df['Ano'] * pibpc_df['Ano'] 
    print(pibpc_df.head())

    #somas
    sumx2 = pibpc_df["x²"].sum()
    sumx = pibpc_df["Ano"].sum()
    sumy = pibpc_df["Ln y"].sum()
    sumxy = pibpc_df["xLny"].sum()

    #calculo coeficentes
    n = pibpc_df["Ln y"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    

    # calculando R²
    ymedio = pibpc_df["Ln y"].mean()
    pibpc_df['SQREG'] = (ymedio - (a * pibpc_df['Ano']) - b)**2
    pibpc_df["SQTOT"] = (ymedio - pibpc_df["Ln y"] )**2
    r2 = pibpc_df['SQREG'].sum()/pibpc_df['SQTOT'].sum()

    b = exp(b)
    print("Exponencial: R² = " + str(r2))
    print(str(a) + '*e^(' + str(b) + '*x)')

def potencia():
    # construindo a tabela
    pibpc_df = pd.read_excel("CalcN3/Tabela_pib_per_capita_brasileiro.xlsx")
    #pibpc_df = pd.DataFrame(dict1)
    pibpc_df['Ln y'] = pibpc_df['PIB per capita-valores correntes (Reais)'].apply(ln)
    pibpc_df['Ln x'] = pibpc_df['Ano'].apply(ln)
    pibpc_df['LnxLny'] = pibpc_df['Ln x'] * pibpc_df["Ln y"]
    pibpc_df["Ln x²"] = pibpc_df['Ln x'] * pibpc_df['Ln x'] 
    print(pibpc_df.head())

    #somas
    sumx2 = pibpc_df["Ln x²"].sum()
    sumx = pibpc_df["Ln x"].sum()
    sumy = pibpc_df["Ln y"].sum()
    sumxy = pibpc_df["LnxLny"].sum()

    #calculo coeficentes
    n = pibpc_df["Ln y"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    

    # calculando R²
    ymedio = pibpc_df["Ln y"].mean()
    pibpc_df['SQREG'] = (ymedio - (a * pibpc_df['Ln x']) - b)**2
    pibpc_df["SQTOT"] = (ymedio - pibpc_df["Ln y"] )**2
    r2 = pibpc_df['SQREG'].sum()/pibpc_df['SQTOT'].sum()

    b = exp(b)
    print("Potência: R² = " + str(r2))
    print(str(b) + '*x^(' + str(a) + ')')
    


#igual exponencial
def geometrico():
    # construindo a tabela
    pibpc_df = pd.read_excel("CalcN3/Tabela_pib_per_capita_brasileiro.xlsx")
    #pibpc_df = pd.DataFrame(dict2)
    pibpc_df['Ln y'] = pibpc_df['PIB per capita-valores correntes (Reais)'].apply(ln)
    pibpc_df['xLny'] = pibpc_df['Ano'] * pibpc_df["Ln y"]
    pibpc_df["x²"] = pibpc_df['Ano'] * pibpc_df['Ano'] 
    print(pibpc_df.head())

    #somas
    sumx2 = pibpc_df["x²"].sum()
    sumx = pibpc_df["Ano"].sum()
    sumy = pibpc_df["Ln y"].sum()
    sumxy = pibpc_df["xLny"].sum()

    #calculo coeficentes
    n = pibpc_df["Ln y"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    

    # calculando R²
    ymedio = pibpc_df["Ln y"].mean()
    pibpc_df['SQREG'] = (ymedio - (a * pibpc_df['Ano']) - b)**2
    pibpc_df["SQTOT"] = (ymedio - pibpc_df["Ln y"] )**2
    r2 = pibpc_df['SQREG'].sum()/pibpc_df['SQTOT'].sum()

    b = exp(b)
    a = exp(a)
    print("Geometrica: R² = " + str(r2))
    print(str(b) + '*' + str(a) + '^(x)')

def polinomial():




    pass

linear()
logaritmico()
exponencial()
potencia()
geometrico()