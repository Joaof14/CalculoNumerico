import pandas as pd
import numpy as np
from math import log, exp
import SistLinear
from urllib.request import urlopen
import matplotlib.pyplot as plt


#tratamento dos dados
url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"
pag = urlopen(url)
html = pag.read()
texto = html.decode()
ind1 = texto.rfind('decimal')
lista = texto[ind1-12:-1].split('\n')

dados = {'year' : [],
'month' : [],
'decimal_date' : [],
'monthly_average' : [],
'de_season_alized' : [],
'days' : [],
'std_dev_days' : [],
'unc_mon_mean' : []}

for item in lista[2:-1]:
    dados['year'].append(item[0:6])
    dados['month'].append(item[6:12])
    dados['decimal_date'].append(item[12:23])
    dados['monthly_average'].append(item[26:35])
    dados['de_season_alized'].append(item[38:48])
    dados['days'].append(item[48:55])
    dados['std_dev_days'].append(item[55:63])
    dados['unc_mon_mean'].append(item[63:])


dataframe = pd.DataFrame(dados)
print(dataframe.head())


dataframe['year'] = dataframe['year'].apply(int)
dataframe['month'] = dataframe['month'].apply(int)
dataframe['decimal_date'] = dataframe['decimal_date'].apply(float)
dataframe['monthly_average'] = dataframe['monthly_average'].apply(float)
dataframe['de_season_alized'] = dataframe['de_season_alized'].apply(float)
dataframe['days'] = dataframe['days'].apply(float)
dataframe['std_dev_days'].apply(float)
dataframe['unc_mon_mean'].apply(float)







e = exp(1)
def ln(x):
    return log(x, e)

def linear():
    #construindo tabela
    output = ''
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    tabela['xy'] = tabela['x'] * tabela['y']
    tabela["x²"] = tabela['x'] * tabela['x']
    print(tabela.head())

    #somas
    sumx2 = tabela["x²"].sum()
    sumx = tabela["x"].sum()
    sumy = tabela['y'].sum()
    sumxy = tabela["xy"].sum()

    #calculo coeficientes
    n = tabela["xy"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    print(str(a) + '*x +(' + str(b) + ')')


    # calculando R²
    ymedio = tabela['y'].mean()
    tabela['SQREG'] = (ymedio - (a * tabela['x']) - b)**2
    tabela["SQTOT"] = (ymedio - tabela['y'] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()
    print("Linear: R² = " + str(r2))

    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(a*x_col + b)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL.png')

    

def logaritmico():
    #construindo tabela
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    tabela['Lnx'] = tabela['x'].apply(ln)
    tabela['yLnx'] = tabela['Lnx'] * tabela['y']
    tabela["(Ln x)²"] = tabela['Lnx'] * tabela['Lnx'] 
    print(tabela.head())

    #somas
    sumx2 = tabela["(Ln x)²"].sum()
    sumx = tabela["Lnx"].sum()
    sumy = tabela['y'].sum()
    sumxy = tabela["yLnx"].sum()

    #calculo coeficientes
    n = tabela["Lnx"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)

    # calculando R²
    ymedio = tabela['y'].mean()
    tabela['SQREG'] = (ymedio - (a * tabela['Lnx']) - b)**2
    tabela["SQTOT"] = (ymedio - tabela['y'] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()

    #gráfico
    x_col = np.array(tabela['Lnx']) 
    y_reg = np.array(a*x_col + b)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_log.png')

    print("Logaritmico: R² = " + str(r2))

    print(str(a) + '*Lnx +(' + str(b) + ')')
    




def exponencial():

    # construindo a tabela
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    #tabela = pd.DataFrame(dict1)
    tabela['Ln y'] = tabela['y'].apply(ln)
    tabela['xLny'] = tabela['x'] * tabela["Ln y"]
    tabela["x²"] = tabela['x'] * tabela['x'] 
    print(tabela.head())

    #somas
    sumx2 = tabela["x²"].sum()
    sumx = tabela["x"].sum()
    sumy = tabela["Ln y"].sum()
    sumxy = tabela["xLny"].sum()

    #calculo coeficentes
    n = tabela["Ln y"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    

    # calculando R²
    ymedio = tabela["Ln y"].mean()
    tabela['SQREG'] = (ymedio - (a * tabela['x']) - b)**2
    tabela["SQTOT"] = (ymedio - tabela["Ln y"] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()
    b = exp(b)
    
    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(a*e**(b*x_col))
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_exp.png')


    
    print("Exponencial: R² = " + str(r2))
    print(str(a) + '*e^(' + str(b) + '*x)')

def potencia():
    # construindo a tabela
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    #tabela = pd.DataFrame(dict1)
    tabela['Ln y'] = tabela['y'].apply(ln)
    tabela['Ln x'] = tabela['x'].apply(ln)
    tabela['LnxLny'] = tabela['Ln x'] * tabela["Ln y"]
    tabela["Ln x²"] = tabela['Ln x'] * tabela['Ln x'] 
    print(tabela.head())

    #somas
    sumx2 = tabela["Ln x²"].sum()
    sumx = tabela["Ln x"].sum()
    sumy = tabela["Ln y"].sum()
    sumxy = tabela["LnxLny"].sum()

    #calculo coeficentes
    n = tabela["Ln y"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    

    # calculando R²
    ymedio = tabela["Ln y"].mean()
    tabela['SQREG'] = (ymedio - (a * tabela['Ln x']) - b)**2
    tabela["SQTOT"] = (ymedio - tabela["Ln y"] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()

    b = exp(b)
    print("Potência: R² = " + str(r2))
    print(str(b) + '*x^(' + str(a) + ')')

    #grafico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(b*x_col**a)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_pot.png')
    
    




#igual exponencial
def geometrico():
    # construindo a tabela
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    #tabela = pd.DataFrame(dict2)
    tabela['Ln y'] = tabela['y'].apply(ln)
    tabela['xLny'] = tabela['x'] * tabela["Ln y"]
    tabela["x²"] = tabela['x'] * tabela['x'] 
    print(tabela.head())

    #somas
    sumx2 = tabela["x²"].sum()
    sumx = tabela["x"].sum()
    sumy = tabela["Ln y"].sum()
    sumxy = tabela["xLny"].sum()

    #calculo coeficentes
    n = tabela["Ln y"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)
    

    # calculando R²
    ymedio = tabela["Ln y"].mean()
    tabela['SQREG'] = (ymedio - (a * tabela['x']) - b)**2
    tabela["SQTOT"] = (ymedio - tabela["Ln y"] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()
    b = exp(b)
    a = exp(a)

    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(b*a**x_col)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_Geo.png')

    
    print("Geometrica: R² = " + str(r2))
    print(str(b) + '*' + str(a) + '^(x)')

def polinomial():

    pass

linear()
logaritmico()
exponencial()
potencia()
geometrico()




