# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''

'''Input File_1 ist für Sommer Profile'''

import sys,os
sys.path.append('../')
import pandas as pd
from ramp.core.core import User, np
from ramp.core.initialise import days

User_list = []

'''
TMPs example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a 
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles. 
For examples related to "thermal loads", see the "input_file_2".
'''
my_path = os.path.abspath(os.path.dirname(__file__))
###############################################################################
pfad = r"C:\Users\rbala\Nextcloud4\Home office\RAMP\Heat pump\04_Ergebnisse\Test_1\Strombus_sequences.csv"
Inputdaten_Strombus = pd.read_csv(pfad, encoding = 'unicode_escape', sep=',', decimal=',')
###############################################################################
Strom_WP = Inputdaten_Strombus["(('Strombus', 'Waermepumpe'), 'flow')"]

Strom_WP_365 = [None]*365

i = 0
for a in range(0, 365):
    Summe_WP = 0
    for k in range(0,24):
        Summe_WP += Strom_WP[i]
        i += 1
        
    Strom_WP_365[a]=Summe_WP/24
#s_m = start_month
#e_m = end_month    
#month_list =[31,28,31,30,31,30,31,31,30,31,30,31,30]
#start_day = sum(month_list[0:start_month-1])
#end_day = sum(month_list[0:end_month])-1
#start_day, end_day = days()
#Strom_WP_mod = Strom_WP_365[start_day:end_day]

#%%


#%%
#Create new user classes

MP = User("Mehrperson",3,3)
User_list.append(MP)

MP_HP = MP.Appliance(MP,1,Strom_WP_365,2,1440,0,30,occasional_use = 1, thermal_P_var= 0.2)
MP_HP.windows([0,1440],[0,0])