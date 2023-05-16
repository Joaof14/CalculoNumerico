import pandas as pd
import numpy as np
from math import log, exp
import SistLinear as sl
from urllib.request import urlopen
import matplotlib.pyplot as plt
import random


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

for item in lista[2:]:
    dados['year'].append(item[0:6])
    dados['month'].append(item[6:12])
    dados['decimal_date'].append(item[12:23])
    dados['monthly_average'].append(item[26:35])
    dados['de_season_alized'].append(item[38:48])
    dados['days'].append(item[48:55])
    dados['std_dev_days'].append(item[55:63])
    dados['unc_mon_mean'].append(item[63:])


dataframe = pd.DataFrame(dados)



dataframe['year'] = dataframe['year'].apply(int)
dataframe['month'] = dataframe['month'].apply(int)
dataframe['decimal_date'] = dataframe['decimal_date'].apply(float)
dataframe['monthly_average'] = dataframe['monthly_average'].apply(float)
dataframe['de_season_alized'] = dataframe['de_season_alized'].apply(float)
dataframe['days'] = dataframe['days'].apply(float)
dataframe['std_dev_days'].apply(float)
dataframe['unc_mon_mean'].apply(float)



#dados usados para previsão com máximo de 50 anos no futuro
prev_data = np.zeros(10)
for i in range(10):
    datapre = round(dataframe['decimal_date'].max() + 50*random.random(), 4)
    prev_data[i] = datapre
prev_data.sort()
y_prev = np.zeros(10)




f = open('Resolução_MMQ.txt','w')
f.write('Método dos mínimos quadrado para média de partes por milhão de carbono na atmosfera em função do tempo\n')
f.write('Amostra: \n\n')
dataframe.sample(10).to_string(f)
f.close()

def outputtxt(texto):
    with open('Resolução_MMQ.txt', 'a') as f:
        f.write(texto)


e = exp(1)
def ln(x):
    return log(x, e)

def linear():
    #construindo tabela
    output = "\n\nMétodo da regressão linear, ajuste geométrico"
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    tabela['xy'] = tabela['x'] * tabela['y']
    tabela["x²"] = tabela['x'] * tabela['x']
    

    #somas
    sumx2 = tabela["x²"].sum()
    sumx = tabela["x"].sum()
    sumy = tabela['y'].sum()
    sumxy = tabela["xy"].sum()

    #calculo coeficientes
    n = tabela["xy"].size
    a = (n*sumxy - sumx*sumy)/(-sumx**2 + n*sumx2)
    b = (sumx * sumxy - sumy*sumx2)/( sumx**2 - n*sumx2)

    # calculando R²
    ymedio = tabela['y'].mean()
    tabela['SQREG'] = (ymedio - (a * tabela['x']) - b)**2
    tabela["SQTOT"] = (ymedio - tabela['y'] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()

    #Previsão
    output+= '\nPrevisão'
    x_prev = np.copy(prev_data)
    y_prev = a * x_prev + b
    for i in range(x_prev.size):
        output += '\n'
        output+= f'na data decimal:{prev_data[i]} a previsão é de {y_prev[i]} ppm de carbono na atmosfera em média'

    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(a*x_col + b)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL.png')

    with open('Tabela_Linear.txt','w') as f:
        tabela.to_string(f)

    outputtxt(output)

def logaritmico():
    #construindo tabela
    output = "\n\nMétodo da regressão linear, ajuste logaritimico"
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    tabela['Lnx'] = tabela['x'].apply(ln)
    tabela['yLnx'] = tabela['Lnx'] * tabela['y']
    tabela["(Ln x)²"] = tabela['Lnx'] * tabela['Lnx'] 

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

    #Previsão
    output+= '\nPrevisão'
    x_prev = np.copy(prev_data)
    for i in range(x_prev.size):
        x_prev[i] = ln(x_prev[i])
        y_prev[i] = a * x_prev[i] + b
        output += '\n'
        output+= f'na data decimal:{prev_data[i]} a previsão é de {y_prev[i]} ppm de carbono na atmosfera em média'

    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(a*tabela['Lnx'] + b)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_log.png')


    with open('Tabela_Log.txt', 'w') as f:
        tabela.to_string(f)
    output += "\n\nR² = " + str(r2) + '\n\nEquação: Y = ' + str(a) +'*Ln(x)'+str(b)
    outputtxt(output)



def exponencial():

    # construindo a tabela
    output = "\n\nMétodo da regressão linear, ajuste exponencial"
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    #tabela = pd.DataFrame(dict1)
    tabela['Ln y'] = tabela['y'].apply(ln)
    tabela['xLny'] = tabela['x'] * tabela["Ln y"]
    tabela["x²"] = tabela['x'] * tabela['x'] 

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
    
    #Previsão
    output+= '\nPrevisão'
    x_prev = np.copy(prev_data)
    for i in range(x_prev.size):
        y_prev[i] = a * x_prev[i] + b
        y_prev[i] = exp(y_prev[i])
        output+= '\n'
        output += f'na data decimal:{prev_data[i]} a previsão é de {y_prev[i]} ppm de carbono na atmosfera em média'
    
    
    
    
    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = e**(a*tabela['x'] + b)
    y_reg = np.array(y_reg)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_exp.png')

    with open('Tabela_exponencial.txt','w') as f:
            tabela.to_string(f)
    b = exp(b)
    output += "\n\nR² = " + str(r2) + '\n\nEquação: Y = ' + str(b) +'*e'+'**(x*'+str(a)+')'
    outputtxt(output)

def potencia():
    # construindo a tabela
    output = "\n\nMétodo da regressão linear, ajuste de potencia"
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    #tabela = pd.DataFrame(dict1)
    tabela['Ln y'] = tabela['y'].apply(ln)
    tabela['Ln x'] = tabela['x'].apply(ln)
    tabela['LnxLny'] = tabela['Ln x'] * tabela["Ln y"]
    tabela["Ln x²"] = tabela['Ln x'] * tabela['Ln x'] 

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

    #Previsão
    output+= '\nPrevisão'
    x_prev = np.copy(prev_data)
    for i in range(x_prev.size):
        x_prev[i] = ln(x_prev[i])
        y_prev[i] = a * x_prev[i] + b
        y_prev[i] = exp(y_prev[i])
        output += '\n'
        output+= f'na data decimal:{prev_data[i]} a previsão é de {y_prev[i]} ppm de carbono na atmosfera em média'

    
    #grafico
    x_col = np.array(tabela['x']) 
    y_reg = e**(a * tabela['Ln x'] + b)
    y_reg = np.array(y_reg)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_pot.png')
    
    
    b= exp(b)
    with open('Tabela_pot.txt','w') as f:
        tabela.to_string(f)
    output += "\n\nR² = " + str(r2) + '\n\nEquação: Y = ' + str(b) +'*x'+'**'+str(a)
    outputtxt(output)

#igual exponencial
def geometrico():
    # construindo a tabela
    output = "\n\nMétodo da regressão linear, ajuste geométrico"
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    #tabela = pd.DataFrame(dict2)
    tabela['Ln y'] = tabela['y'].apply(ln)
    tabela['xLny'] = tabela['x'] * tabela["Ln y"]
    tabela["x²"] = tabela['x'] * tabela['x'] 

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
    

    #Previsão
    output+= '\nPrevisão'
    x_prev = np.copy(prev_data)
    for i in range(x_prev.size):
        y_prev[i] = a * x_prev[i] + b
        y_prev[i] = exp(y_prev[i])
        output += '\n'
        output+= f'na data decimal:{prev_data[i]} a previsão é de {y_prev[i]} ppm de carbono na atmosfera em média'


    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = e**(a*tabela['x'] + b)
    y_reg = np.array(y_reg)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_Geo.png')

    with open('Tabela_geo.txt','w') as f:
        tabela.to_string(f)

    a = exp(a)
    b = exp(b)
    output += "\n\nR² = " + str(r2) + '\n\nEquação: Y = ' + str(b) +'*'+str(a)+'**x'
    outputtxt(output)


def polinomial(grau = 2):
    output = '\n\n Método da regressão linear, ajuste polinimial de grau ' + str(grau)
    #criando tabela
    n = grau + 1
    tabela = pd.DataFrame()
    tabela['x'] = dataframe['decimal_date']
    tabela['y'] = dataframe['monthly_average']
    
    #criando matrizes para receber coeficientes como resultado
    mA = np.zeros((n,n))
    mB = np.zeros(n)
    for i in range(mB.size):
        for j in range(mB.size):
            mA[i][j] = (tabela['x']**(i + j)).sum()
        mB[i] = (tabela['y'] * (tabela['x']**(i))).sum()
    sl.atribuiMatriz(mA,mB)
    coef = sl.EliminGauss()
    
    #cálculo R²
    ymedio = tabela['y'].mean()
    y_reg = 0
    equac = ''
    for i in range(n-1, -1, -1):
        y_reg += coef[i]*tabela['x']**i
        equac += '+(' + str(coef[i]) + '*x**' + str(i) + ')'
    tabela['SQREG'] = (ymedio - y_reg)**2
    tabela["SQTOT"] = (ymedio - tabela['y'] )**2
    r2 = tabela['SQREG'].sum()/tabela['SQTOT'].sum()

    #previsão
    output+= '\nPrevisão'
    x_prev = np.copy(prev_data)
    y_prev = np.zeros(x_prev.size)
    for i in range(x_prev.size):
        for j in range(n-1, -1, -1):
            y_prev[i] += coef[j]*x_prev[i]**j
    for i in range(x_prev.size):
        output += '\n'
        output+= f'na data decimal:{prev_data[i]} a previsão é de {y_prev[i]} ppm de carbono na atmosfera em média'


    #gráfico
    x_col = np.array(tabela['x']) 
    y_reg = np.array(y_reg)
    graf, eix = plt.subplots()
    eix.plot(x_col, y_reg)
    eix.set_xlabel('Ano')
    eix.set_ylabel('Partes por milhão de Co2 ')
    graf.savefig('RL_Polinomial_grau' + str(grau)+ '.png')

    with open('Tabela_pol.txt','w') as f:
        tabela.to_string(f)


    output += "\n\nR² = " + str(r2) + '\nEquação: Y = ' + equac
    outputtxt(output)

linear()
logaritmico()
exponencial()
potencia()
geometrico()
polinomial()



