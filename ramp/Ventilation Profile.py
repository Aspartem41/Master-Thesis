# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:55:15 2024

@author: Romit
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random


df = pd.read_excel('Average Temperature Profile.xlsx')   
df['Date'] = pd.to_datetime(df['Date'])
# df=df.set_index('Date')

# Hourly average
def average_hourly_values(df):
    df = df.copy() 
    df['Hour'] = df['Date'].dt.hour  
    hourly_mean_df = df.groupby('Hour')['Temperature'].mean().reset_index()  
    hourly_mean_df['Temperature'] = hourly_mean_df['Temperature'].round(2) 
    
    # Set the 'Hour' column as the index
    hourly_mean_df.set_index('Hour', inplace=False)
    
    return hourly_mean_df

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))




#------------------------------

# Define the date ranges for Winter 
winter_dates_1 = (df['Date'] >= '2022-01-01') & (df['Date'] <= '2022-03-19')
winter_dates_2 = (df['Date'] >= '2022-11-01') & (df['Date'] <= '2022-12-31')


winter_df = df[winter_dates_1 | winter_dates_2]   
winter_hourly_mean = average_hourly_values(winter_df) 

# Save the DataFrames
winter_df.to_excel('Seasonal Dataframes/Winter_2022.xlsx', index=False)
winter_hourly_mean.to_excel('Seasonal Dataframes/Winter_mean_2022.xlsx', index=False)

# Winter Plot
plt.subplot(3, 2, 1)
sns.lineplot(data=winter_hourly_mean, x=winter_hourly_mean.index, y='Temperature', marker='o', color='b')
plt.title('Winter Hourly Mean Temperature')
plt.xlabel('Hour of the Day')
plt.ylabel('Temperature (°C)')

#--------------------------------------------

# Define the date ranges for Spring
spring_dates = (df['Date'] >= '2022-03-20') & (df['Date'] <= '2022-05-13')

spring_df = df[spring_dates]
spring_hourly_mean = average_hourly_values(spring_df)


# Save the DataFrames
spring_df.to_excel('Seasonal Dataframes/Spring_2022.xlsx', index=False)
spring_hourly_mean.to_excel('Seasonal Dataframes/Spring_mean_2022.xlsx', index=False)

# Spring Plot
plt.subplot(3, 2, 2)
sns.lineplot(data=spring_hourly_mean, x=spring_hourly_mean.index, y='Temperature', marker='o', color='g')
plt.title('Spring Hourly Mean Temperature')
plt.xlabel('Hour of the Day')
plt.ylabel('Temperature (°C)')

#---------------------------------------------

# Define the date ranges for Summer
summer_dates = (df['Date'] >= '2022-05-14') & (df['Date'] <= '2022-09-13')


summer_df = df[summer_dates]
summer_hourly_mean = average_hourly_values(summer_df)

# Save the DataFrames
summer_df.to_excel('Seasonal Dataframes/Summer_2022.xlsx', index=False)
summer_hourly_mean.to_excel('Seasonal Dataframes/Summer_mean_2022.xlsx', index=False)

# Summer Plot
plt.subplot(3, 2, 3)
sns.lineplot(data=summer_hourly_mean, x=summer_hourly_mean.index, y='Temperature', marker='o', color='r')
plt.title('Summer Hourly Mean Temperature')
plt.xlabel('Hour of the Day')
plt.ylabel('Temperature (°C)')

#--------------------------------------------------

# Define the date ranges for Autumn
autumn_dates = (df['Date'] >= '2022-09-14') & (df['Date'] <= '2022-10-30')

autumn_df = df[autumn_dates]
autumn_hourly_mean = average_hourly_values(autumn_df)

# Save the DataFrames
autumn_df.to_excel('Seasonal Dataframes/Autumn_2022.xlsx', index=False)
autumn_hourly_mean.to_excel('Seasonal Dataframes/Autumn_mean_2022.xlsx', index=False)

# Autumn Plot
plt.subplot(3, 2, 4)
sns.lineplot(data=autumn_hourly_mean, x=autumn_hourly_mean.index, y='Temperature', marker='o', color='orange')
plt.title('Autumn Hourly Mean Temperature')
plt.xlabel('Hour of the Day')
plt.ylabel('Temperature (°C)')


#-------------------------------------------------------

# Combined Plot
plt.subplot(3, 1, 3)
sns.lineplot(data=winter_hourly_mean, x=winter_hourly_mean.index, y='Temperature', marker='o', label='Winter', color='b')
sns.lineplot(data=spring_hourly_mean, x=spring_hourly_mean.index, y='Temperature', marker='o', label='Spring', color='g')
sns.lineplot(data=summer_hourly_mean, x=summer_hourly_mean.index, y='Temperature', marker='o', label='Summer', color='r')
sns.lineplot(data=autumn_hourly_mean, x=autumn_hourly_mean.index, y='Temperature', marker='o', label='Autumn', color='orange')
plt.title('Hourly Mean Temperature for All Seasons')
plt.xlabel('Hour of the Day')
plt.ylabel('Temperature (°C)')
plt.legend()


#%%

import pandas as pd
import numpy as np
import datetime
import calendar
import holidays

df = pd.read_excel('Average Temperature Profile.xlsx')   
df['Date'] = pd.to_datetime(df['Date'])
# df=df.set_index('Date')

# Function to determine yearly pattern based on holidays and weekends
def yearly_pattern(year):
    # Yearly behavior pattern
    first_day = datetime.date(year, 1, 1).strftime("%A")
    country = 'DE'
    subdiv = "TH"
    if calendar.isleap(year):
        year_len = 366
    else:
        year_len = 365

    Year_behaviour = np.zeros(year_len)
    
    dict_year = {'Monday': [5, 6], 
                 'Tuesday': [4, 5], 
                 'Wednesday': [3, 4],
                 'Thursday': [2, 3], 
                 'Friday': [1, 2], 
                 'Saturday': [0, 1], 
                 'Sunday': [6, 0]}
      
    for d in dict_year.keys():
        if first_day == d:
            Year_behaviour[dict_year[d][0]:year_len:7] = 1  # Saturdays 
            Year_behaviour[dict_year[d][1]:year_len:7] = 1  # Sundays 
    
    try:
        holidays_country = list(holidays.CountryHoliday(country, subdiv, years=year).keys())
    except KeyError:
        c_error = {'LV': 'LT', 'RO': 'BG'}
        print(f"[WARNING] Due to a known issue, the version of the holidays package you automatically installed is the 0.10.2, not containing {country}. Please refer to 'https://github.com/dr-prodigy/python-holidays/issues/338' for an explanation on how to install holidays 0.10.3. Otherwise, holidays from {c_error[country]} will be used.")
        country = c_error[country]
        holidays_country = list(holidays.CountryHoliday(country, years=year).keys())

    for holiday in holidays_country:
        day_of_year = holiday.timetuple().tm_yday
        Year_behaviour[day_of_year-1] = 3  # Holidays
    
    year_behaviour_hourly = Year_behaviour.repeat(24)
    return year_behaviour_hourly


# Basic parameters
COP_base = 4.0  # Baseline COP at reference temperature 20°C
alpha = 0.2     # COP decrease rate per degree Celsius
power_consumption = np.zeros_like(df['Temperature'].values)

# Define the function to calculate power consumption
def calculate_power_consumption(temperature_data, year_behaviour_hourly, season):
    power_consumption = np.zeros_like(temperature_data)
    
    for i, (temp, behavior) in enumerate(zip(temperature_data, year_behaviour_hourly)):
        if season in ['winter_dates_1', 'winter_dates_2', 'autumn_dates', 'spring_dates']:
            if temp < 15 and behavior != 3:  # Means Heating demand
                power_consumption[i] = 2 + np.random.uniform(-0.2, 0.2) 
            else:
                power_consumption[i] = 0.5 + np.random.uniform(-0.02, 0.02)  # That means basic consumption without ventilation system
        elif season == 'summer_dates':
            if temp < 15 and behavior != 3:  #Means Heating demand in Summer
                power_consumption[i] = 2 + np.random.uniform(-0.2, 0.2) 
            elif behavior != 3 and behavior !=1 and 8 <= i % 24 < 18:  # Means Cooling demand during working hours
                if temp >= 20:
                    T_min = 20 
                    T_max = max(df['Temperature'])
                    if temp >= T_max:
                        cop = COP_base - alpha * (T_max - T_min)
                    else:
                        cop = COP_base - alpha * (temp - T_min)
                    power_consumption[i] = 10 / cop  # Power consumption calculation
                else:
                    power_consumption[i] = 0.5 + np.random.uniform(-0.02, 0.02)  # That means basic consumption without ventilation system
            else:
                power_consumption[i] = 0.5 + np.random.uniform(-0.02, 0.02)  # That means basic consumption without ventilation system
    
    return power_consumption

year = 2022
yearly_behavior = yearly_pattern(year)
df['Power Consumption'] = 0

#------------------------------

# Define the date ranges for Winter 
winter_dates_1 = (df['Date'] >= '2022-01-01 00:00:00') & (df['Date'] <= '2022-03-19 23:00:00')
winter_dates_2 = (df['Date'] >= '2022-11-01 00:00:00') & (df['Date'] <= '2022-12-31 23:00:00')

winter_temps_1 = df.loc[winter_dates_1, 'Temperature'].values 
df.loc[winter_dates_1, 'Power Consumption'] = calculate_power_consumption(winter_temps_1, yearly_behavior[winter_dates_1], 'winter_dates_1')
winter_temps_2 = df.loc[winter_dates_2, 'Temperature'].values
df.loc[winter_dates_2, 'Power Consumption'] = calculate_power_consumption(winter_temps_2, yearly_behavior[winter_dates_2], 'winter_dates_2')

#--------------------------------------------

# Define the date ranges for Spring
spring_dates = (df['Date'] >= '2022-03-20 00:00:00') & (df['Date'] <= '2022-05-13 23:00:00')

spring_temps = df.loc[spring_dates, 'Temperature'].values
df.loc[spring_dates, 'Power Consumption'] = calculate_power_consumption(spring_temps, yearly_behavior[spring_dates], 'spring_dates')


#---------------------------------------------

# Define the date ranges for Summer
summer_dates = (df['Date'] >= '2022-05-14 00:00:00') & (df['Date'] <= '2022-09-13 23:00:00')

summer_temps = df.loc[summer_dates, 'Temperature'].values
df.loc[summer_dates, 'Power Consumption'] = calculate_power_consumption(summer_temps, yearly_behavior[summer_dates], 'summer_dates')

# --------------------------------------------------

# Define the date ranges for Autumn
autumn_dates = (df['Date'] >= '2022-09-14 00:00:00') & (df['Date'] <= '2022-10-30 23:00:00')

autumn_temps = df.loc[autumn_dates, 'Temperature'].values
df.loc[autumn_dates, 'Power Consumption'] = calculate_power_consumption(autumn_temps, yearly_behavior[autumn_dates], 'autumn_dates')

# --------------------------------------------------

# Save the final data to an Excel file
final_df = pd.DataFrame({'Date': df['Date'], 'Power Consumption': df['Power Consumption']})
final_df.set_index('Date', inplace = True)
final_df.to_excel('Results/Ventilation Dataframes of Buildings/Ventilation Consumption of Building 34.xlsx')

plt.figure(figsize=(16,8))
final_df['Power Consumption'].plot(color='violet', drawstyle = 'steps-post')
plt.title('Ventilation Consumption of Building 34' , fontsize=14, fontweight='bold')
plt.xlabel('Hours' ,fontsize=12, fontweight= 'bold')
plt.ylabel('Power Consumption (kW)', fontsize=12, fontweight= 'bold')
#plt.ylim(0)
plt.tight_layout()
plt.show()

























# def calculate_heating_power_consumption(temperature_data):
#     power_consumption = np.zeros_like(temperature_data)
    
#     for i, temp in enumerate(temperature_data):
#         if temp < 15:
#             # Heating demand with slight variation
#             power_consumption[i] = 2 + np.random.uniform(-0.1, 0.1)
#         else:
#             power_consumption[i] = 0  # No demand

#     return power_consumption

# def calculate_cooling_power_consumption(temperature_data):
#     power_consumption = np.zeros_like(temperature_data)
    
#     for i, temp in enumerate(temperature_data):
#         if temp >= 20:
#             # Cooling demand
#             T_min, T_max = 20, 30
#             if temp >= T_max:
#                 cop = COP_base - alpha * (T_max - T_min)
#             else:
#                 cop = COP_base - alpha * (temp - T_min)
            
#             power_consumption[i] = 10 / cop  # Power consumption calculation
#         else:
#             power_consumption[i] = 0  # No demand

#     return power_consumption



# # Combine the seasonal ranges into a single index
# full_date_range = pd.date_range(start='2022-01-01', end='2022-12-31 23:00:00', freq='H')

# # Ensure the date range of the temperature profile matches the combined range
# temperature_df = temperature_df.reindex(full_date_range)

# # Initialize the power consumption array
# power_consumption = np.zeros_like(temperature_df['Temperature'].values)

# # Calculate power consumption for each season
# winter_temps = temperature_df.loc[winter_range, 'Temperature'].values
# spring_temps = temperature_df.loc[spring_range, 'Temperature'].values
# summer_temps = temperature_df.loc[summer_range, 'Temperature'].values
# autumn_temps = temperature_df.loc[autumn_range, 'Temperature'].values

# power_consumption[winter_range] = calculate_heating_power_consumption(winter_temps)
# power_consumption[spring_range] = calculate_heating_power_consumption(spring_temps)
# power_consumption[summer_range] = calculate_cooling_power_consumption(summer_temps)
# power_consumption[autumn_range] = calculate_heating_power_consumption(autumn_temps)

# # Create the final dataframe with the Date index and Power Consumption column
# final_df = pd.DataFrame({'Date': full_date_range, 'Power Consumption': power_consumption})
# final_df.set_index('Date', inplace=True)

# # Save the final dataframe to an Excel file
# final_df.to_excel('power_consumption_profile.xlsx')

# # Display the first few rows of the final dataframe (optional)
# print(final_df.head())



# # Define the date ranges for the four seasons
# winter_range = pd.date_range(start='2022-12-01', end='2023-02-28 23:59:59', freq='H')
# spring_range = pd.date_range(start='2023-03-01', end='2023-05-31 23:59:59', freq='H')
# summer_range = pd.date_range(start='2023-06-01', end='2023-08-31 23:59:59', freq='H')
# autumn_range = pd.date_range(start='2023-09-01', end='2023-11-30 23:59:59', freq='H')


