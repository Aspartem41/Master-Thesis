# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:02:45 2022

@author: rbala
"""

'Visualizierung Jahreslastgang für E-Mobilität'


import sys,os
sys.path.append('../')
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

inputfile_verbrauch = r"..\ramp\results_mod\Jahreslastgang.csv"
inputfile_SLP = r"..\ramp\input_files\SLP_H0.csv"
inputfile_JZ = r"..\ramp\results_mod\Last_Jahreszeiten.csv"
inputfile_Einspeiseprofil = r"..\ramp\input_files\Einspeiseprofile.csv"

Last_profile = pd.read_csv(inputfile_verbrauch, index_col = 0,sep =',', decimal='.')
SLP= pd.read_csv(inputfile_SLP, sep =';', decimal=',')
Last_JZ = pd.read_csv(inputfile_JZ,index_col = 0, sep =';', decimal=',')
Einspeiseprofil = pd.read_csv(inputfile_Einspeiseprofil,index_col = 0, sep =';', decimal=',')

date_time_index = pd.date_range(start= '1/1/2050', periods=8760,
                          freq='H')
mpl.rcParams.update(mpl.rcParamsDefault)
#%% Umrechnung der SLP von viertelstunde zu Stundenauflösung 

data=[None]* len(Last_profile)
i=0
for j in range(len(Last_profile)):
    Sum = 0 
    for k in range(0,4):
        Sum += SLP['H0'][i]
        i += 1
    data[j] = Sum/4 

SLP_h = pd.DataFrame(data)

#%%'
#Leistung Rechnung für PV
A_Hlt = 1053817   #'[hlt]'  # Anzahl Familie/Haushalte 
A_EFH = 444045     #'[EFH]' # Anzahl Ein- und Zweifamiliehaus
A_MFH = 92324      #'[MFH]' # Anzahl Mehrfamiliehaus
A_hlt_EFH = 518143 # [hlt]         # Anzahl Familie in EFH
A_hlt_MFH = 535674 # [hlt]                 # Anzahl Familie in MFH
Area_EFH = 100     # [m2/EFH]                # Dachfläche Ein- und Zweifamiliehaus
Area_MFH = 150     # [m2/MFH]       # Dachfläche Ein- und Zweifamiliehaus
P_PV = 0.1     # [kWp/m2]      # PV Leistung 1kWp /10m2 (hier 0,1kWp/m2)

Hlt_EFH = A_Hlt / A_EFH  #[Hlt/EFH] # Haushalte/Familie pro EHF 
Hlt_MFH = A_Hlt / A_MFH  #[Hlt/MFH] # Haushalte/Familie pro MHF

c = (P_PV * Area_EFH)/ Hlt_EFH  #[kWp/EFH]  # kWp pro Haushalte in EFH
b = (P_PV * Area_MFH)/ Hlt_MFH  #[kWp/MFH]

P_pv_Hlt = (c* A_hlt_EFH + b* A_hlt_MFH)/A_Hlt # [kWp/Hlt]
P_pv_Hlt = P_pv_Hlt / 1000

P_pv_Hlt_q = 7.5 /1000  # 7.5kWp to MWp

#%% Linear interpolation

x = [0,5,10,15,20,25,30]
y = [None] * len(x)
for i in range(len(x)):
    
    x1, y1 = 0,3.6  
    x2,y2 = 30, 100
    y[i] = y1 + ((x[i]-x1)*((y2-y1)/(x2-x1)))



#%%


Last_profile = Last_profile.set_index(date_time_index)
SLP_h = SLP_h.set_index(date_time_index)
SLP_h = SLP_h.rename(columns = {0: 'SLP Strom Haushalte'})

Last_nom = Last_profile/(sum(Last_profile['Stromverbrauch'])/1000)      # Nomierung auf 1000MWh
Last_nom = Last_nom.rename(columns = {'Stromverbrauch': 'Stromlast(RAMP)'})
Last_JZ.index = pd.to_datetime(Last_JZ.index)

Last_JZ['Winter'] = Last_JZ['Winter']/(sum(Last_JZ['Winter'])/1000) 
Last_JZ['Sommer'] = Last_JZ['Sommer']/(sum(Last_JZ['Sommer'])/1000)
Last_JZ['Uebergang'] = Last_JZ['Uebergang']/(sum(Last_JZ['Uebergang'])/1000)  
#fig, ax = plt.subplots(figsize=(19.1, 10.5))
Last_JZ = Last_JZ.rename(columns = {'Uebergang': 'Übergang'})


#%% Auswirkungen der PV-Anlage

Einspeiseprofil['Einspeiseprofil_PV'] = (Einspeiseprofil['data_PV_Aufdach_Erfurt'] + Einspeiseprofil['data_PV_Aufdach_Nordhausen'] + 
                          Einspeiseprofil['data_PV_Aufdach_Gera'] + Einspeiseprofil['data_PV_Aufdach_Hildburghausen'])/4

Einspeise_PV = (P_pv_Hlt_q * Einspeiseprofil['Einspeiseprofil_PV'])# Nominierte Leistung mal Einspeiseprofile in MW

Einspeise_PV = pd.DataFrame(Einspeise_PV)
Einspeise_PV = Einspeise_PV.set_index(date_time_index)

Stromlast_hlt = Last_profile/1070000 # Last pro Haushalt
#Stromlast_hlt = Stromlast_hlt * 1000    # in kW
Stromlast_hlt = Stromlast_hlt.rename(columns = {'Stromverbrauch': 'Stromlast(RAMP)'})

Last_dE = pd.DataFrame(Stromlast_hlt['Stromlast(RAMP)'] - Einspeise_PV['Einspeiseprofil_PV'])
Last_dE = Last_dE.rename(columns = {0: 'Stromlast(RAMP) pro Haushalt'})


#%%

fig,ax = plt.subplots(figsize=(19.1, 10.5))
Last_nom['Stromlast(RAMP)'].plot(ax=ax, kind='line', color='orangered',drawstyle = 'steps-post', grid=True, fontsize=28,linewidth =3, legend=True)#, figsize = (19.1, 10.5))
(SLP_h*4).plot(ax=ax, kind='line', color='yellowgreen', legend=True,drawstyle = 'steps-post', linewidth=3) # Nomiert auf 1000 MWh
#ax.set_xlim(pd.Timestamp('2050-07-01 00:00:00'),pd.Timestamp('2050-07-10 00:00:00'))
ax.set_ylabel('Leistung in MW', fontsize = 28)
ax.set_title("Stromlast im Sektor Haushalte", fontsize = 28) 
ax.legend(fontsize =28)
ax.grid()
plt.show()

#%%%

fig,ax = plt.subplots(figsize=(19.1, 10.5))

Last_JZ.plot(ax=ax, kind='line',drawstyle='steps-post', grid=True, legend=True, fontsize=28, linewidth= 3)

# #ax.set_xlim(pd.Timestamp('2030-07-01 00:00:00'),pd.Timestamp('2030-07-10 00:00:00'))
ax.set_ylabel('Leistung in MW', fontsize = 28)
ax.set_title("Stromlast im Sektor Haushalte", fontsize = 28) 
ax.legend(fontsize =28)
plt.show()



fig,ax = plt.subplots(figsize=(19.1, 10.5))
(Stromlast_hlt['Stromlast(RAMP)']*1000).plot(ax=ax, kind='line', color='orangered', grid=True, fontsize=20, legend=True)#, figsize = (19.1, 10.5))
(Einspeise_PV*1000).plot(ax=ax, kind='line', grid=True, legend=True, fontsize=15)
ax.set_ylabel('Leistung in kW', fontsize = 20)
ax.set_title("Stromlast und PV Erzeugungsprofil pro Haushalt", fontsize = 20) 
ax.legend(["Stromlast (RAMP)", "Erzeugungsprofil_PV"], fontsize =20)
plt.show()

#%%

# fig,ax = plt.subplots(figsize=(19.1, 10.5))
# fig = plt.figure()

# plt.subplot(2, 2, 1)
# plt.plot((Stromlast_hlt['Stromlast(RAMP)']*1000), color='orangered')#, figsize = (19.1, 10.5))
# plt.plot((Einspeise_PV*1000))
# ax.set_xlim(pd.Timestamp('2050-01-17 00:00:00'),pd.Timestamp('2050-01-24 00:00:00'))


# plt.subplot(2, 2, 2)
# plt.plot((Stromlast_hlt['Stromlast(RAMP)']*1000), color='orangered')#, figsize = (19.1, 10.5))
# plt.plot((Einspeise_PV*1000))
# ax.set_xlim(pd.Timestamp('2050-06-20 00:00:00'),pd.Timestamp('2050-06-27 00:00:00'))
# plt.legend(fontsize = 20)
# plt.grid()
# plt.show()
#%%
fig,ax = plt.subplots(figsize=(19.1, 10.5))


signal = Last_dE['Stromlast(RAMP) pro Haushalt']*1000   
pos_signal = signal.copy()
neg_signal = signal.copy()

a=pd.DataFrame(np.zeros(len(Last_dE)))
a = a.set_index(date_time_index)
pos_signal[pos_signal < 0] = 0
neg_signal[neg_signal > 0] = 0
pos_signal= pd.DataFrame(pos_signal)
neg_signal= pd.DataFrame(neg_signal)

pos_signal = pos_signal.set_index(date_time_index)
neg_signal = neg_signal.set_index(date_time_index)

pos_signal.plot(ax=ax,color='orangered',label = 'Stromlast pro Haushalt',grid=True, fontsize=20, linewidth=1.5)
neg_signal.plot(ax=ax, color='green',label = 'Eingespeicherte Energie',grid=True, linewidth=1.5)
a.plot(ax=ax, color='lightgrey', linewidth=2)
ax.set_title("Auswirkungen der dezentralen Energieversorgung auf Stormlast (pro Haushalt) im Sektor Haushalte", fontsize = 15)
plt.legend(['Stromlast pro Haushalt','Eingespeicherte Energie'], fontsize = 20)
plt.grid()
plt.show()


#%%
fig,ax = plt.subplots(figsize=(19.1, 10.5))
(Last_dE*1000).plot(ax=ax,kind='line',color= 'orangered', grid=True, legend=True,  fontsize=20, linewidth = 2)
a.plot(ax=ax, color='black', linewidth=1.5, grid=True, legend = False)
ax.set_ylabel('Leistung in kW]', fontsize = 20)
ax.set_title("Auswirkungen der dezentralen Energieversorgung auf Stormlast (pro Haushalt) im Sektor Haushalte", fontsize = 15) 
ax.legend(['Stromlast(RAMP) pro Haushalt'],fontsize =20)
plt.show()

