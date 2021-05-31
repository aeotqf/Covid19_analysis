# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:44:41 2020

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


 

