"""
Created on Mon Jun 22 20:06:42 2020

@author: ELLIS

based on the work of Gianluca Malato 

Ajustando los datos a un modelo exponencial

"""




import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import matplotlib.pyplot as plt



#Leemos el csv#
df = pd.read_csv('covid19HN.csv')  


"""

Suponga que solo ocupa por el momento del csv el numero de casos totales con
pandas.DataFrame.loc : accedemos a un grupo de filas y columnas de un arreglo asi:
data.iloc[<row selection>, <column selection>]


y ocupamos tambien manejar las fechas que por el momento estan en formato
%Y-%m-%d %H:%M:%S la manera mas simple es cambiar las fechas a un formato de numeros,
o sea tiempo.

"""


""" con la funcion .loc de pandas le decimos que queremos todas las filas de el csv que se encuentra en df
pero solo las columnas llamadas 'date' y 'total_cases'  """

df = df.loc[:,['date','total_cases']] 



"""Ahora queremos convertir las fechas en formato estandar a tiempo. Ahora que
df es un arreglo usamos la funcion de pandas pd.to_datetime() que convierte un
string a una clase datetime """

df['date'] = pd.to_datetime(df.date) 

"""Ahora que la columna date del arreglo es clase datetime podemos usar otra funcion de pandas como
.dt.dayofyear que convierte variables tipo datetime a dia del año """

df['date'] = df.date.dt.dayofyear    
 
#los primeros dos problemas estan resueltos#




"""

El modelo exponencial puede ser usado para describir el crecimiento
exponencial de algo en el tiempo. O sea que el modelo exponencial
describe una infeccion que no puede detnerse.


    
    f(t,a,b,c)=a*exp(b(t-c))
    
    donde: 
    
    f(t) es el numero de casos en el tiempo t
    a es el valor inicial, el numero de casos iniciales
    b es el factor de crecimiento
    k = b+c/t  k es el valor de cuanta gente infecta alguien que esta infectado
    
"""



#se agregan los valores del tiempo y total de casos a listas#
#estos son los valores que usted debe agregar a su grafica en VENTANA Q#
t = list(df.iloc[:,0]-72)
y = list(df.iloc[:,1])

#definimos el modelo

def exponential_model(t,a,b,c):
    #return a*np.exp(b*t)
    return a*np.exp(b*(t-c))

#ajustamos los datos al modelo
    
"""
Una vez ajustamos los datos al modelo, exp fit es una matriz de valores donde debemos de sacar
los argumentos a,b y c

"""

exp_fit = curve_fit(exponential_model,t,y,[1,5,0.1],maxfev=5000)


#j1=a, k1=b, l1=c, kk=k


j1=exp_fit[0][0]
k1=exp_fit[0][1]
l1=exp_fit[0][2]
kk = k1-l1/max(t)


#resolvemos el modelo, esto solo se hace para encontrar el error en el ajuste
exp_sol = int(fsolve(lambda t: exponential_model(t,j1,k1,l1),1,maxfev=5000))

de00 = exp_fit[1][0][0]
de11 = exp_fit[1][1][1]
de22 = exp_fit[1][2][2]

exp_variance = [de00,de11,de22] 

exp_error = np.sqrt(exp_variance)


""" 
Ahora es momento de usar matplotlib para graficar los datos analizados
no solo queremos graficar los datos de los valores de fechas del csv sino
mas bien la proyeccion del modelo, entonces lo que haremos es
agregar un array tal que este formado por los valores de tiempo obtenidos del
csv mas un valor agregado de la solucion encontrada del modelo predictivo



list(range(max(t)+1,sol+1)) una lista de un rango es un numero ascendente 

asi t + list(range(max(t)+1,sol+1))  agreaga un limite para el tiempo en la prediccion
se coloca en un array para poder graficarlo con matplotlib 



"""

#la prediccion para t t#
p_t = list(range(max(t)+1,100))

#parametros para la interfaz grafica# 
plt.rcParams['figure.figsize'] = [10, 10]
plt.rc('font', size=14)


#Datos reales, scatter es una funcion de plt pra graficar dispersion#
plt.scatter(t,y,label="Datos Reales ",color="red")

#Modelo logistico que no vamos a analizar#
#plt.plot(t+p_t,[logistic_model(t,j,k,l) for t in t+p_t],'tab:orange', label="Regresión Logística " )
#plt.text(2, 35, 'Proyección: (17 , 39 +- 6) ')

#Grafica de la prediccion del modelo exponencial#
plt.plot(t+p_t, [exponential_model(t,j1,k1,l1) for t in t+p_t],'tab:blue', label="Modelo exponencial" )

plt.legend()
plt.xlabel("Días desde que se registro el primer caso")
plt.ylabel("Cantidad total de infectados")

#si usted quiere agregar limites a los ejes coordenados habilite ylim y xlim#
#plt.ylim(0,500)
#plt.xlim(0,41)
 
#para mostrar la interfaz grafica#
plt.show()
