# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:55:37 2023

@author: Romit
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#df = pd.read_excel('All_10_Herd Load Profile.xlsx' ,index_col='Date')
df =  pd.read_excel('All_10_0.3_Herd Load Profile.xlsx' ,index_col='Date')

df2 = pd.read_csv('SLP_H0.csv', sep =';', decimal=',') 

figsize = (19.1, 10.5)
ax = df['Stromverbrauch'].plot(stacked=True, kind = 'line', drawstyle = 'steps-post', figsize=(19.1, 10.5), fontsize = 20)
plt.xticks(rotation=0)
plt.title('Stromlast', fontsize = 20)
plt.ylabel('Leistung in MW', fontsize = 20)
plt.show()

date_time_index = pd.date_range(start= '1/1/2050', periods=8760,
                              freq='H')
Last_nom = df/(sum(df['Stromverbrauch'])/1000)
data=[None]* len(df)
i=0
for j in range(len(df)):
    Sum = 0 
    for k in range(0,4):
        Sum += df2['H0'][i]
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


# df2=df.resample('D').sum()
# plt.figure(figsize=(8,6))
# df2['Stromverbrauch'].plot()
# plt.title('Name' , fontsize=12, fontweight='bold')
# plt.xlabel('Months' ,fontsize=10, fontweight= 'bold')
# plt.ylabel('Consumption(kW)', fontsize=10, fontweight= 'bold')
# #plt.savefig('Daily_Load Profile.jpeg',bbox_inches='tight')

# plt.figure(figsize=(8,6))
# df['Stromverbrauch'].plot(color='orange')
# plt.title('Name' , fontsize=12, fontweight='bold')
# plt.xlabel('Hours' ,fontsize=10, fontweight= 'bold')
# plt.ylabel('Consumption(kW)', fontsize=10, fontweight= 'bold')
# #plt.savefig('Hourly_Load Profile.jpeg',bbox_inches='tight')