# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:25:03 2023

@author: rbala
"""

import sys,os
sys.path.append('../')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

F_type = 'All'
my_path = os.path.abspath(os.path.dirname(__file__))

pfad = os.path.join(my_path, '..//Final Load Profiles/'+ str(F_type)+ '/Load profile_'+ str(F_type)+'.xlsx')
if F_type == 'All':
    pfad = os.path.join(my_path, '..//Final Load Profiles/'+ str(F_type)+ '/' +str(F_type)+'_Households_Load_profile.xlsx')
Profil_ind = pd.read_excel(pfad, decimal = ',',index_col='Date')

figsize = (19.1, 10.5)
ax = Profil_ind['Stromverbrauch'].plot(stacked=True, kind = 'line', drawstyle = 'steps-post', figsize=(19.1, 10.5), fontsize = 20)
plt.xticks(rotation=0)
#plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['1.1.','1.2.','1.3.','1.4.','1.5.','1.6.','1.7.','1.8.','1.9.','1.10.','1.11.','1.12.'])
#plt.xlabel(year)
plt.title('Stromlast', fontsize = 20)
plt.ylabel('Leistung in MW', fontsize = 20)
plt.show()


if F_type == 'All':
    P_tot = sum(Profil_ind['Stromverbrauch'])*10000
    print('Jahresenergiemenge: '+str(P_tot/1000000000) + 'in TWh')
else:
    print('Jahresenergiemenge: '+str(sum(Profil_ind['Stromverbrauch'])/100) + 'in TWh')

date_time_index = pd.date_range(start= '1/1/2050', periods=8760,
                              freq='H')

#%%

Last_nom = Profil_ind/(sum(Profil_ind['Stromverbrauch'])/1000)
inputfile_SLP = r"..\Final Load Profiles\SLP_H0.csv"
SLP= pd.read_csv(inputfile_SLP, sep =';', decimal=',')

data=[None]* len(Profil_ind)
i=0
for j in range(len(Profil_ind)):
    Sum = 0 
    for k in range(0,4):
        Sum += SLP['H0'][i]
        i += 1
    data[j] = Sum/4 

SLP_h = pd.DataFrame(data)

SLP_h = SLP_h.set_index(date_time_index)
SLP_h = SLP_h.rename(columns = {0: 'SLP Strom Haushalte'})
Last_nom = Last_nom.set_index(date_time_index)
Last_nom = Last_nom.rename(columns = {'Stromverbrauch': 'Stromlast(RAMP)'})
SLP_h = SLP_h*4
fig,ax = plt.subplots(figsize=(19.1, 10.5))
Last_nom['Stromlast(RAMP)'].plot(ax=ax, kind='line', color='orangered',drawstyle = 'steps-post', grid=True, fontsize=28,linewidth =3, legend=True)#, figsize = (19.1, 10.5))
(SLP_h).plot(ax=ax, kind='line', color='yellowgreen', legend=True,drawstyle = 'steps-post', linewidth=3) # Nomiert auf 1000 MWh
#ax.set_xlim(pd.Timestamp('2050-07-01 00:00:00'),pd.Timestamp('2050-07-10 00:00:00'))
ax.set_ylabel('Leistung in MW', fontsize = 28)
ax.set_title("Stromlast im Sektor Haushalte", fontsize = 28) 
ax.legend(fontsize =28)
ax.grid()
plt.show()


#%%

arr = np.arange(0,150,1)
Energy = pd.DataFrame()
E=[None] * len(arr)
#%%
Par_P_EV = {}
Par_P_EV['bus']  = [0.5, -16.5, 700]
Par_P_EV['small']  = [0.26, -13, 546]
Par_P_EV['medium'] = [0.3, -14, 600]
Par_P_EV['large']  = [0.35, -15.2, 620]
Par_P_EV['bahn']  = [0.7, -17.5, 900]
vehicles =['small', 'medium', 'large', 'bus', 'bahn']
for v in vehicles: 
    for i in range(len(arr)):
        E[i] = Par_P_EV[v][0] * arr[i]**2 + Par_P_EV[v][1] *arr[i] + Par_P_EV[v][2]
        if v == 'bus':
            Energy['bus']= E
        elif v == 'bahn':
            Energy['bahn']= E
        elif v == 'small':
            Energy['small']= E
        elif v == 'medium':
            Energy['medium']= E
        elif v == 'large':
            Energy['large']= E
            
fig,ax = plt.subplots(figsize=(19.1, 10.5))
Energy.plot(ax=ax, kind='line', grid=True, fontsize=28,linewidth =3, legend=True)#, figsize = (19.1, 10.5))

#ax.set_xlim(pd.Timestamp('2050-07-01 00:00:00'),pd.Timestamp('2050-07-10 00:00:00'))
ax.set_ylabel('Power consumption in Wh/5min', fontsize = 28)
ax.set_title("PV faktor", fontsize = 28) 
ax.legend(fontsize =28)
ax.grid()
plt.show()