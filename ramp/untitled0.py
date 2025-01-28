# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:10:35 2024

@author: Romit
"""

import pandas as pd
import numpy as np
import datetime
import calendar
import holidays

# Define the temperature profile
data = pd.read_csv('temperature_profile.csv', parse_dates=[[0, 1, 2, 3]], header=None, names=['Year', 'Month', 'Day', 'Hour', 'Temperature'])
data.columns = ['Date', 'Temperature']
data.set_index('Date', inplace=True)

# Define the date ranges for the four seasons
winter_start = '2022-12-01'
winter_end = '2023-02-28'
spring_start = '2023-03-01'
spring_end = '2023-05-31'
summer_start = '2023-06-01'
summer_end = '2023-08-31'
autumn_start = '2023-09-01'
autumn_end = '2023-11-30'

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

# Define the function to calculate power consumption
def calculate_power_consumption(temp_data, year_behaviour, season):
    power_consumption = np.zeros_like(temp_data)
    
    for i, (temp, behavior) in enumerate(zip(temp_data, year_behaviour)):
        if season in ['Winter', 'Autumn', 'Spring']:
            if temp < 15 and behavior != 3:  # Heating demand
                power_consumption[i] = 2 + np.random.uniform(-0.2, 0.2)  # Slight variation
            else:
                power_consumption[i] = 0  # No demand or no operation (holidays/weekends)
        elif season == 'Summer':
            if behavior != 3 and 8 <= i % 24 < 20:  # Cooling demand during working hours
                if temp >= 20:
                    T_min, T_max = 20, 30
                    COP_base = 4.0
                    alpha = 0.1
                    if temp >= T_max:
                        cop = COP_base - alpha * (T_max - T_min)
                    else:
                        cop = COP_base - alpha * (temp - T_min)
                    power_consumption[i] = 10 / cop  # Power consumption calculation
                else:
                    power_consumption[i] = 0  # No demand
            else:
                power_consumption[i] = 0  # No operation (holidays/weekends or non-working hours)
    
    return power_consumption

# Apply the power consumption calculation season-wise
year = data.index.year[0]
yearly_behavior = yearly_pattern(year)

winter_mask = (data.index >= winter_start) & (data.index <= winter_end)
spring_mask = (data.index >= spring_start) & (data.index <= spring_end)
summer_mask = (data.index >= summer_start) & (data.index <= summer_end)
autumn_mask = (data.index >= autumn_start) & (data.index <= autumn_end)

data['Power Consumption'] = 0  # Initialize power consumption column

data.loc[winter_mask, 'Power Consumption'] = calculate_power_consumption(data.loc[winter_mask, 'Temperature'].values, yearly_behavior[winter_mask], 'Winter')
data.loc[spring_mask, 'Power Consumption'] = calculate_power_consumption(data.loc[spring_mask, 'Temperature'].values, yearly_behavior[spring_mask], 'Spring')
data.loc[summer_mask, 'Power Consumption'] = calculate_power_consumption(data.loc[summer_mask, 'Temperature'].values, yearly_behavior[summer_mask], 'Summer')
data.loc[autumn_mask, 'Power Consumption'] = calculate_power_consumption(data.loc[autumn_mask, 'Temperature'].values, yearly_behavior[autumn_mask], 'Autumn')

# Save the final data to an Excel file
data[['Power Consumption']].to_excel('Power_Consumption.xlsx')
