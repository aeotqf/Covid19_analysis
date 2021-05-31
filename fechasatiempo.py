# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:20:41 2020

@author: ELLIS

based on the work of Gianluca Malato 

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