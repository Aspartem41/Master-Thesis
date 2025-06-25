# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:51:22 2024

@author: Romit
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


# Reading dataframes of every rooms
# The dataframes are allocated according to the Room code

df1_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Seminar Hall.xlsx')            # Small Seminar Hall  
df1_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Medium Seminar Hall.xlsx')           # Medium Seminar Hall 
df1_3 = pd.read_excel('Results/Room Dataframes/Dataframe of Large Seminar Hall.xlsx')            # Large Seminar Hall 
# df2_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Lecture Hall.xlsx')          # Small Lecture Hall
df2_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Medium Lecture Hall.xlsx')           # Medium Lecture Hall
df2_3 = pd.read_excel('Results/Room Dataframes/Dataframe of Large Lecture Hall.xlsx')            # Large Lecture Hall
df3 = pd.read_excel('Results/Room Dataframes/Dataframe of Office 1P.xlsx')                       # 1 Person Office
df4 = pd.read_excel('Results/Room Dataframes/Dataframe of Office 2P.xlsx')                       # 2 Person Office
#df5 = pd.read_excel('Results/Room Dataframes/Dataframe of Office 3P.xlsx')                      # 3 Person Office
df6 = pd.read_excel('Results/Room Dataframes/Dataframe of Office 5P.xlsx')                       # 5 Person Office
df7 = pd.read_excel('Results/Room Dataframes/Dataframe of Computer Lab.xlsx')                    # Computer Lab
df8_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Meeting Room.xlsx')            # Small Meeting Room
# df8_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Big Meeting Room.xlsx')              # Big Meeting Room
df9_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Toilet.xlsx')                  # Small Toilet
df9_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Medium Toilet.xlsx')                 # Medium Toilet
df9_3 = pd.read_excel('Results/Room Dataframes/Dataframe of Large Toilet.xlsx')                  # Large Toilet
df9_4 = pd.read_excel('Results/Room Dataframes/Dataframe of Common Toilet.xlsx')                 # Common Toilet
df10_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Corridor.xlsx')               # Small Corridor
df10_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Medium Corridor with Stairs.xlsx')  # Medium Corridor and Stairs
df10_3 = pd.read_excel('Results/Room Dataframes/Dataframe of Large Corridor with Stairs.xlsx')   # Large Corridor and Stairs
# df11_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Waiting Area.xlsx')           # Small Waiting Area
# df11_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Big Waiting Area.xlsx')             # Big Waiting Area
# df12 = pd.read_excel('Results/Room Dataframes/Dataframe of Server Room.xlsx')                    # Server Room
df13 = pd.read_excel('Results/Room Dataframes/Dataframe of Storage Room.xlsx')                   # Storage Room
df14 = pd.read_excel('Results/Room Dataframes/Dataframe of Electronics Lab.xlsx')                # Electronics Lab
df15 = pd.read_excel('Results/Room Dataframes/Dataframe of Thermal Lab.xlsx')                    # Thermal Lab
df21 = pd.read_excel('Results/Room Dataframes/Dataframe of Personal Room.xlsx')                  # Personal Room
# df22_1 = pd.read_excel('Results/Room Dataframes/Dataframe of Small Kitchen.xlsx')                # Small Kitchen
df22_2 = pd.read_excel('Results/Room Dataframes/Dataframe of Kitchen 2P.xlsx')                      # Kitchen 2P
df22_3 = pd.read_excel('Results/Room Dataframes/Dataframe of Kitchen 4P.xlsx')                      # Kitchen 4P
df22_4 = pd.read_excel('Results/Room Dataframes/Dataframe of Kitchen 5P.xlsx')                   # Kitchen 5P
df23 = pd.read_excel('Results/Room Dataframes/Dataframe of Bathroom.xlsx')                       # Bathroom
# df24 = pd.read_excel('Results/Room Dataframes/Dataframe of Hallway.xlsx')                        # Hallway
# df25 = pd.read_excel('Results/Room Dataframes/Dataframe of Dorm Corridor with Stairs.xlsx')      # Dorm Corridor with Stairs
df26 = pd.read_excel('Results/Room Dataframes/Dataframe of Hike Lab.xlsx')                       # Hike Lab
df27 = pd.read_excel('Results/Room Dataframes/Dataframe of Workshop.xlsx')                       # Workshop
df28 = pd.read_excel('Results/Room Dataframes/Dataframe of Design Room.xlsx')                    # Design Room
df29 = pd.read_excel('Results/Room Dataframes/Dataframe of Test Hall.xlsx')                      # Test Hall
# df30 = pd.read_excel('Results/Room Dataframes/Dataframe of Geo Preparation Room.xlsx')           # Geo Preparation Room
# df31 = pd.read_excel('Results/Room Dataframes/Dataframe of Mechanical Energy Storage.xlsx')      # Mechanical Energy Storage
# df32 = pd.read_excel('Results/Room Dataframes/Dataframe of Electric Energy Center.xlsx')         # Electric Energy Center
# df33 = pd.read_excel('Results/Room Dataframes/Dataframe of Hydropulse Lab.xlsx')                 # Hydropulse Lab
# df34 = pd.read_excel('Results/Room Dataframes/Dataframe of Biogas Lab.xlsx')                     # Biogas Lab
# df35 = pd.read_excel('Results/Room Dataframes/Dataframe of Mechanical Workshop.xlsx')            # Mechanical Workshop
# df36 = pd.read_excel('Results/Room Dataframes/Dataframe of E-Tech Workshop.xlsx')                # E-Tech Workshop
# df37 = pd.read_excel('Results/Room Dataframes/Dataframe of Hot Water Center.xlsx')               # Hot Water Center
# df38 = pd.read_excel('Results/Room Dataframes/Dataframe of Multi Work Room.xlsx')                # Multi Work Room
# df39 = pd.read_excel('Results/Room Dataframes/Dataframe of Information Center.xlsx')             # Information Center
# df40 = pd.read_excel('Results/Room Dataframes/Dataframe of Shower Room.xlsx')                    # Shower Room


# Reading dataframes of electrical power consumption for ventilation system of different buildings
df_Ven_34 = pd.read_excel('Results/Ventilation Dataframes of Buildings/Ventilation Consumption of Building 34.xlsx')                    # 34 Ventilation Electrical Consumption


# Function to get monthly consumption for a selected building
df_2021 = pd.read_excel('Measured Consumption.xlsx', sheet_name = '2021')
df_2022 = pd.read_excel('Measured Consumption.xlsx', sheet_name = '2022')
df_2023 = pd.read_excel('Measured Consumption.xlsx', sheet_name = '2023')
df_avg =  pd.read_excel('Measured Consumption.xlsx', sheet_name = 'Average')
def building_consumption_2021(building_number):
    building_data = df_2021[df_2021['Building_number'] == building_number]
    if not building_data.empty:
        monthly_consumption = building_data.iloc[0, 1:].tolist()
        return monthly_consumption
    else:
        return None

def building_consumption_2022(building_number):
    building_data = df_2022[df_2022['Building_number'] == building_number]
    if not building_data.empty:
        monthly_consumption = building_data.iloc[0, 1:].tolist()
        return monthly_consumption
    else:
        return None

def building_consumption_2023(building_number):
    building_data = df_2023[df_2023['Building_number'] == building_number]
    if not building_data.empty:
        monthly_consumption = building_data.iloc[0, 1:].tolist()
        return monthly_consumption
    else:
        return None
    
def building_consumption_avg(building_number):
    building_data = df_avg[df_avg['Building_number'] == building_number]
    if not building_data.empty:
        monthly_consumption = building_data.iloc[0, 1:].tolist()
        return monthly_consumption
    else:
        return None

def avg_total_consumption(building_number):
    building_data = df_avg[df_avg['Building_number'] == building_number]
    if not building_data.empty:
        avg_yearly_consumption = building_data.iloc[0, 1:].sum()
        return avg_yearly_consumption
    else:
        return None
    
# Choose the building number
Buildings = [36,34,28,19,20,18,35,25,5,6]
Building = int(input('Please choose the building from the list: '))
if Building not in Buildings:
    print("Invalid building number")
    exit() 
    
    
# Selection of the rooms corresponding to the particular building
if Building == 34:
    df1_2['Power Consumption'] *= 1    # The multiplier reprents the number of rooms of each type in that particular building
    df2_2['Power Consumption'] *= 1
    df3['Power Consumption'] *= 3
    df4['Power Consumption'] *= 2
    df6['Power Consumption'] *= 2
    df14['Power Consumption'] *= 1
    df15['Power Consumption'] *= 1
    df9_2['Power Consumption'] *= 2
    df9_4['Power Consumption'] *= 1
    df10_2['Power Consumption'] *= 2
    df_Ven_34['Power Consumption'] *= 1
    final_df = df1_2.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df2_2['Power Consumption'] + df3['Power Consumption'] + df4['Power Consumption'] + df6['Power Consumption'] + df14['Power Consumption'] + df15['Power Consumption'] + df9_2['Power Consumption'] + df9_4['Power Consumption'] + df10_2['Power Consumption'] + df_Ven_34['Power Consumption']
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)  
    measured_consumption_avg = building_consumption_avg(Building)
    measured_sum = avg_total_consumption(Building)
elif Building == 28:
    df1_1['Power Consumption'] *= 1           
    df1_2['Power Consumption'] *= 1
    df3['Power Consumption'] *= 2
    df4['Power Consumption'] *= 2
    df9_1['Power Consumption'] *= 2
    df9_4['Power Consumption'] *= 1
    df10_1['Power Consumption'] *= 2
    df10_2['Power Consumption'] *= 1
    df29['Power Consumption'] *= 1
    # df40['Power consumption'] *=1
    final_df = df1_1.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df1_2['Power Consumption'] + df3['Power Consumption'] + df4['Power Consumption'] + df9_1['Power Consumption'] + df9_4['Power Consumption'] + df10_1['Power Consumption'] + df10_2['Power Consumption'] + df29['Power Consumption'] 
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)
    measured_consumption_avg = building_consumption_avg(Building) 
    measured_sum = avg_total_consumption(Building)
elif Building == 35:
    df1_2['Power Consumption'] *= 1           
    df3['Power Consumption'] *= 1
    df4['Power Consumption'] *= 3
    df9_1['Power Consumption'] *= 2
    df10_1['Power Consumption'] *= 2
    final_df = df1_2.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df3['Power Consumption'] + df4['Power Consumption'] + df9_1['Power Consumption'] + df10_1['Power Consumption'] 
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)  
    measured_consumption_avg = building_consumption_avg(Building) 
    measured_sum = avg_total_consumption(Building)
elif Building == 20:
    df1_3['Power Consumption'] *= 3            
    df2_3['Power Consumption'] *= 1
    df3['Power Consumption'] *= 5
    df7['Power Consumption'] *= 1
    df9_3['Power Consumption'] *= 2
    df9_4['Power Consumption'] *= 1
    df10_2['Power Consumption'] *= 1
    final_df = df1_3.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df2_3['Power Consumption'] + df3['Power Consumption'] + df7['Power Consumption'] + df9_3['Power Consumption'] + df9_4['Power Consumption'] + df10_2['Power Consumption']
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)  
    measured_consumption_avg = building_consumption_avg(Building) 
    measured_sum = avg_total_consumption(Building)
elif Building == 25:
    df1_3['Power Consumption'] *= 3            
    df2_3['Power Consumption'] *= 1
    df3['Power Consumption'] *= 5
    df9_3['Power Consumption'] *= 2
    df9_4['Power Consumption'] *= 1
    df10_2['Power Consumption'] *= 1
    final_df = df1_3.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df2_3['Power Consumption'] + df3['Power Consumption'] + df9_3['Power Consumption'] + df9_4['Power Consumption'] + df10_2['Power Consumption']
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)  
    measured_consumption_avg = building_consumption_avg(Building) 
    measured_sum = avg_total_consumption(Building)
elif Building == 5 or 6:
    df21['Power Consumption'] *= 70
    df22_2['Power Consumption'] *= 4
    df22_3['Power Consumption'] *= 8
    df22_4['Power Consumption'] *= 6
    df23['Power Consumption'] *= 24     
    final_df = df21.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df23['Power Consumption'] + df22_2['Power Consumption'] + df22_3['Power Consumption'] + df22_4['Power Consumption']
    # final_df['Power Consumption'] += df22_2['Power Consumption'] + df22_3['Power Consumption'] + df22_4['Power Consumption'] + df23['Power Consumption']
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)  
    measured_consumption_avg = building_consumption_avg(Building) 
    measured_sum = avg_total_consumption(Building)
elif Building == 19:
    df1_1['Power Consumption'] *= 9  # including Raatsaal 
    df2_3['Power Consumption'] *= 2
    df3['Power Consumption'] *= 2
    df4['Power Consumption'] *= 7 
    df7['Power Consumption'] *= 2
    df9_2['Power Consumption'] *= 4
    df9_4['Power Consumption'] *= 1
    df10_3['Power Consumption'] *= 4
    final_df = df1_1.copy()            # Initialize final dataframe with the first dataframe
    final_df['Power Consumption'] += df2_3['Power Consumption'] + df3['Power Consumption'] + df4['Power Consumption'] + df7['Power Consumption'] + df9_2['Power Consumption'] + df9_4['Power Consumption'] + df10_3['Power Consumption']
    measured_consumption_2021 = building_consumption_2021(Building)     # Monthly power consumption in kWh
    measured_consumption_2022 = building_consumption_2022(Building)
    measured_consumption_2023 = building_consumption_2023(Building)  
    measured_consumption_avg = building_consumption_avg(Building) 
    measured_sum = avg_total_consumption(Building)
# elif Building == 36:                     # The newly constructed Hike Building
#     df8_1['Power Consumption'] *= 1           
#     df9_1['Power Consumption'] *= 1
#     df26['Power Consumption'] *= 2
#     df27['Power Consumption'] *= 2
#     df28['Power Consumption'] *= 2
#     df29['Power Consumption'] *= 1
#     final_df = df8_1.copy()            # Initialize final dataframe with the first dataframe
#     final_df['Power Consumption'] += df9_1['Power Consumption'] + df26['Power Consumption'] + df27['Power Consumption'] + df28['Power Consumption'] + df29['Power Consumption'] 
 
    
# and so on for every buildings
else:
    print('Invalid building number')
    exit()


# Adding base load of the particular building 
building_basic_loads = {
    
    32: 0.1,        # Building 32 with base load of 0.1 kW
    34: 0,          # Building 34 with base load of 0 kW because already included in ventilation system
    35: 0.4,        # Building 35 with base load of 0.5 kW    
    36: 0,          # Because there was no data in the old report (Building was in function from the year 2024)
    19: 0,          # Because there was no data in the old report (Building was in function from the year 2023)
    20: 1.37,       # Building 20 with base load of 1.37 kW
    22: 1.057,      # Building 22 with base load of 1.057 kW
    28: 5.25,       # Building 28 with base load of 5.25 kW
    25: 2.1,        # Building 25 with base load of 2.1 kW
    5: 2.05,        # Building 5 with base load of2.05 kW (Total 4.11 kW combined of Building 5 and 6)
    
}

dates = pd.date_range(start='2022-01-01 00:00:00', end='2022-12-31 23:00:00', freq='H')
base_load = building_basic_loads.get(Building)
if base_load <=0.5:
    base_variation = np.abs(np.random.normal(loc=base_load, scale=0.02, size=len(dates)))
else:
    base_variation = np.abs(np.random.normal(loc=base_load, scale=0.2, size=len(dates)))
final_df['Power Consumption'] += base_variation

 
#%% Scaling factor calculation 


# Converting the dates into datetime formate
final_df['Date']=pd.to_datetime(final_df['Date'])
final_df=final_df.set_index('Date')
final_df['Month'] = final_df.index.month
monthly_hourly_sum = final_df.groupby('Month')['Power Consumption'].sum()
# calculated_sum = final_df['Power Consumption'].sum()

# Calculate scaling factors for each month
scaling_factors = measured_consumption_avg / monthly_hourly_sum
# scaling_factor = measured_sum / calculated_sum

# Apply scaling factors to the hourly data
final_df['Scaling Factor'] = final_df['Month'].map(scaling_factors)
final_df['Scaled Power Consumption'] = final_df['Power Consumption'] * final_df['Scaling Factor']
final_df.drop(columns=['Month'], inplace=True)
final_df.drop(columns=['Scaling Factor'], inplace=True)

scaled_data = final_df['Scaled Power Consumption']

# Saving the final dataframe
final_df.to_excel(f'Results/Building Dataframes/Dataframe of Building {Building}.xlsx', index = 'Date')


#%%
# Plotting the final load profile of required building
final_df2=final_df.resample('M').sum()
plt.figure(figsize=(16, 8))
plt.plot(final_df2.index.month,final_df2['Scaled Power Consumption'], color='green', marker='o', markersize=7, linestyle='-')
plt.plot(final_df2.index.month,final_df2['Power Consumption'], color='blue', marker='o', markersize=7, linestyle='-')
plt.plot(final_df2.index.month,measured_consumption_2021, color='0.7', marker='x', markersize=5, linestyle='--')
plt.plot(final_df2.index.month,measured_consumption_2022, color='0.75', marker='x', markersize=5, linestyle='--')
plt.plot(final_df2.index.month,measured_consumption_2023, color='0.8', marker='x', markersize=5, linestyle='--')
# plt.plot(final_df2.index.month,measured_consumption_avg, color='black', marker='o', markersize=7, linestyle='-')
# final_df2['Power Consumption'].plot(color='green', marker='o', markersize=8, linestyle='-')
plt.title(f'Load Profile of Building {Building}', fontsize=20, fontweight='bold')
plt.xlabel('Months', fontsize=19, fontweight='bold')
plt.ylabel('Power Consumption (kWh)', fontsize=19, fontweight='bold')
plt.ylim(0)
plt.grid(axis='y', linestyle='-') 
plt.grid(axis='x', linestyle='-')
plt.tight_layout()
plt.show()
plt.legend(['Scaled Power','Calculated Power','2021','2022','2023'], fontsize=14, loc='lower right') 
plt.savefig(f'Results/Building Plots/Load Profile of Building {Building}.jpeg',bbox_inches='tight')

plt.figure(figsize=(16,8))
final_df['Scaled Power Consumption'].plot(color='orange', drawstyle = 'steps-post')
plt.title(f'Hourly Load Profile of Building {Building}' , fontsize=20, fontweight='bold')
plt.xlabel('Hours' ,fontsize=19, fontweight= 'bold')
plt.ylabel('Power Consumption (kW)', fontsize=19, fontweight= 'bold')
plt.grid(axis='y', linestyle='-') 
plt.grid(axis='x', linestyle='-')
#plt.ylim(0)
plt.tight_layout()
plt.show()
plt.savefig(f'Results/Building Plots/Hourly Load Profile of Building {Building}.jpeg',bbox_inches='tight')



