# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:15:25 

@author: Romit
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

Rooms = { 1.1: 'Small Seminar Hall', 1.2: 'Medium Seminar Hall', 1.3: 'Large Seminar Hall', 2.1: 'Small Lecture Hall', 2.2: 'Medium Lecture Hall', 2.3: 'Large Lecture Hall', 3: 'Office 1P', 4: 'Office 2P', 5: 'Office 3P', 6: 'Office 5P', 11.1: 'Small Waiting Area', 11.2: 'Big Waiting Area', 
         7: 'Computer Lab', 8.1: 'Small Meeting Room', 8.2: 'Big Meeting Room', 9.1: 'Small Toilet', 9.2: 'Medium Toilet', 9.3: 'Large Toilet', 9.4: 'Common Toilet', 10.1: 'Small Corridor', 10.2: 'Medium Corridor with Stairs', 10.3: 'Large Corridor with Stairs',
         12: 'Server Room', 13: 'Storage Room', 14: 'Electronics Lab', 15: 'Thermal Lab', 16: 'Geotech Lab', 17: 'Water Tech Lab', 18: 'Hybrid Tech Lab', 19: 'High Power Lab', 20: 'Geothermal Lab', 21: 'Personal Room', 22.1: 'Small Kitchen', 22.2: 'Kitchen 2P', 22.3: 'Kitchen 4P', 22.4: 'Kitchen 5P',
         23: 'Bathroom', 24: 'Hallway', 25: 'Dorm Corridor with Stairs', 26: 'Hike Lab' , 27: 'Workshop', 28: 'Design Room',  29: 'Test Hall', 30: 'Geo Preparation Room', 31:'Mechanical Energy Storage', 32: 'Electric Energy Center', 33: 'Hydropulse Lab', 34: 'Biogas Lab', 35: 'Mechanical Workshop',
         36: 'E-Tech Workshop', 37: 'Hot Water Center', 38: 'Multi Work Room', 39: 'Information Center', 40: 'Shower Room',
}

Room_code = float(input('Please choose the room code: '))
Room = Rooms.get(Room_code, None)


# Define the folder path
folder_path = f'Room_results/{Room}/'

# Reading all required files of respective period from the folder

df11 = pd.read_csv(f'{folder_path}WS_Break/Load Profile 08-010.csv')  
df12 = pd.read_csv(f'{folder_path}WS_Autumn/Load Profile 010-011.csv')
df13 = pd.read_csv(f'{folder_path}WS_Winter/Load Profile 011-013.csv')
df13_1 = pd.read_csv(f'{folder_path}WS_Winter/Load Profile 01-02.csv')
df14 = pd.read_csv(f'{folder_path}WS_Exam/Load Profile 02-03.csv')
df21 = pd.read_csv(f'{folder_path}SS_Break/Load Profile 03-04.csv')
df22 = pd.read_csv(f'{folder_path}SS_Spring/Load Profile 04-05.csv')
df23 = pd.read_csv(f'{folder_path}SS_Summer/Load Profile 05-07.csv')
df24 = pd.read_csv(f'{folder_path}SS_Exam/Load Profile 07-08.csv')

# Converting the Date into datetime formate

df11['Date']=pd.to_datetime(df11['Date'])
df12['Date']=pd.to_datetime(df12['Date'])
df13['Date']=pd.to_datetime(df13['Date'])
df13_1['Date']=pd.to_datetime(df13_1['Date'])
df14['Date']=pd.to_datetime(df14['Date'])
df21['Date']=pd.to_datetime(df21['Date'])
df22['Date']=pd.to_datetime(df22['Date'])
df23['Date']=pd.to_datetime(df23['Date'])
df24['Date']=pd.to_datetime(df24['Date'])


# Setting Date as an index

df11=df11.set_index('Date')
df12=df12.set_index('Date')
df13=df13.set_index('Date')
df13_1=df13_1.set_index('Date')
df14=df14.set_index('Date')
df21=df21.set_index('Date')
df22=df22.set_index('Date')
df23=df23.set_index('Date')
df24=df24.set_index('Date')


#collecting the desired data from the datasheets for respected seasons

ws_13_1 = df13_1['2022-01-01 00:00:00':'2022-02-05 23:00:00']
#print(ws_13_1)
ws_14 = df14['2022-02-06 00:00:00':'2022-03-15 23:00:00']
#print(ws_14)
ss_21 = df21['2022-03-16 00:00:00':'2022-03-31 23:00:00']
#print(ss_21)
ss_22 = df22['2022-04-01 00:00:00':'2022-05-15 23:00:00']
#print(ss_22)
ss_23 = df23['2022-05-16 00:00:00':'2022-07-15 23:00:00']
#print(ss_23)
ss_24 = df24['2022-07-16 00:00:00':'2022-08-15 23:00:00']
#print(ss_24)
ws_11 = df11['2022-08-16 00:00:00':'2022-09-30 23:00:00']
#print(ws_11)
ws_12 = df12
#print(ws_12)
ws_13= df13
#print(ws_13)


final_df = pd.concat([ ws_13_1 , ws_14 , ss_21 , ss_22 , ss_23 , ss_24 , ws_11 , ws_12 , ws_13],ignore_index=False)
#print(final_df)
final_df.to_excel(f'Results/Room Dataframes/Dataframe of {Room}.xlsx', index = 'Date')


# Plotting the final load profile of required room
final_df2=final_df.resample('M').sum()
plt.figure(figsize=(16, 8))
final_df2['Power Consumption'].plot(color='blue', marker='o', markersize=8, linestyle='-')
plt.title(f'Load Profile of {Room}', fontsize=20, fontweight='bold')
plt.xlabel('Months', fontsize=19, fontweight='bold')
plt.ylabel('Power Consumption (kWh)', fontsize=19, fontweight='bold')
plt.ylim(0)
plt.grid(axis='y', linestyle='-') 
plt.tight_layout()
plt.show()
plt.savefig(f'Results/Room Plots/Load Profile of {Room}.jpeg',bbox_inches='tight')

plt.figure(figsize=(16,8))
final_df['Power Consumption'].plot(color='orange', drawstyle = 'steps-post')
plt.title(f'Hourly Load Profile of {Room}' , fontsize=20, fontweight='bold')
plt.xlabel('Hours' ,fontsize=19, fontweight= 'bold')
plt.ylabel('Power Consumption (kW)', fontsize=19, fontweight= 'bold')
#plt.ylim(0)
plt.tight_layout()
plt.show()
plt.savefig(f'Results/Room Plots/Hourly Load Profile of {Room}.jpeg',bbox_inches='tight')
