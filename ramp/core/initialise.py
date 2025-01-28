# -*- coding: utf-8 -*-

#%% Initialisation of a model instance

import numpy as np 
import importlib
import datetime
import calendar
import pytz

# Import holidays package 
import holidays
 

def yearly_pattern(year,start_month,end_month):
    '''
    Definition of a yearly pattern of weekends and weekdays, in case some appliances have specific wd/we behaviour
    '''
    
    #Yearly behaviour pattern
    first_day = datetime.date(year, 1, 1).strftime("%A")
    country = 'DE'
    if calendar.isleap(year):
        year_len = 366
        month_list =[31,29,31,30,31,30,31,31,30,31,30,31,30]
    else: 
        year_len = 365
        month_list =[31,28,31,30,31,30,31,31,30,31,30,31,30]
    start_day = sum(month_list[0:start_month-1])
    end_day = sum(month_list[0:end_month])-1
    Year_behaviour = np.zeros(year_len)
    
    dict_year = {'Monday'   : [5, 6], 
                 'Tuesday'  : [4, 5], 
                 'Wednesday': [3, 4],
                 'Thursday' : [2, 3], 
                 'Friday'   : [1, 2], 
                 'Saturday' : [0, 1], 
                 'Sunday'   : [6, 0]}
      
    for d in dict_year.keys():
        if first_day == d:
            Year_behaviour[dict_year[d][0]:year_len:7] = 1
            Year_behaviour[dict_year[d][1]:year_len:7] = 1
    
            
    if country == 'EL': 
        country = 'GR'
    elif country == 'FR':
        country = 'FRA'
        
    try:
        holidays_country = list(holidays.CountryHoliday(country, years = year).keys())
    except KeyError: 
        c_error = {'LV':'LT', 'RO':'BG'}
        print(f"[WARNING] Due to a known issue, the version of the holidays package you automatically installed is the 0.10.2, not containing {country}. Please refer to 'https://github.com/dr-prodigy/python-holidays/issues/338' for an explanation on how to install holidays 0.10.3. Otherwise, holidays from {c_error[country]} will be used.")
        country = c_error[country]
        holidays_country = list(holidays.CountryHoliday(country, years = year).keys())

    for i in range(len(holidays_country)):
        day_of_year = holidays_country[i].timetuple().tm_yday
        Year_behaviour[day_of_year-1] = 1
    Year_behaviour=Year_behaviour[start_day:end_day]
    # #Yearly behaviour pattern
    # Year_behaviour = np.zeros(365)
    # Year_behaviour[5:365:7] = 1
    # Year_behaviour[6:365:7] = 1
    
    return(Year_behaviour)


def user_defined_inputs(j,r):
    
    '''
    Imports an input file and returns a processed User_list
    '''
    if r == 5:
     #file_module = importlib.import_module(f'input_files.input_file_{j}')
     file_module = importlib.import_module(f'input_files.Romit_inputfiles.EP_{j}')
    elif r == 6:
     #file_module = importlib.import_module(f'input_files.input_file_{j}')
     file_module = importlib.import_module(f'input_files.Romit_inputfiles.AE_{j}')
    elif r == 7:
     #file_module = importlib.import_module(f'input_files.input_file_{j}')
     file_module = importlib.import_module(f'input_files.Romit_inputfiles.POK_{j}')
    elif r == 8:
     #file_module = importlib.import_module(f'input_files.input_file_{j}')
     file_module = importlib.import_module(f'input_files.Romit_inputfiles.PMK_{j}')
    elif r == 9:
     #file_module = importlib.import_module(f'input_files.input_file_{j}')
     file_module = importlib.import_module(f'input_files.Romit_inputfiles.MP_{j}')
    elif r == 10:
     #file_module = importlib.import_module(f'input_files.input_file_{j}')
     file_module = importlib.import_module(f'input_files.Romit_inputfiles.All_{j}')
        
        
    User_list = file_module.User_list
    
    return(User_list)



def Initialise_model(year, num_pro):
    '''
    The model is ready to be initialised
    '''
    num_profiles = num_pro
    #num_profiles = int(input('Please indicate the number of profiles to be generated: ')) #asks the user how many profiles (i.e. code runs) he wants
    print('Please wait...') 
    Profile = [] #creates an empty list to store the results of each code run, i.e. each stochastically generated profile
    
    return (Profile, num_profiles)
    
def Initialise_inputs(j, r,year, start_month, end_month):
    Year_behaviour = yearly_pattern(year,start_month,end_month)
    user_defined_inputs(j,r)
    user_list = user_defined_inputs(j,r)
    # Calibration parameters
    '''
    Calibration parameters. These can be changed in case the user has some real data against which the model can be calibrated
    They regulate the probabilities defining the largeness of the peak window and the probability of coincident switch-on within the peak window
    '''
    peak_enlarg = 0.15 #percentage random enlargement or reduction of peak time range length
    mu_peak = 0.5 #median value of gaussian distribution [0,1] by which the number of coincident switch_ons is randomly selected
    s_peak = 0.5 #standard deviation (as percentage of the median value) of the gaussian distribution [0,1] above mentioned
    op_factor = 0.5 #off-peak coincidence calculation parameter

    return (peak_enlarg, mu_peak, s_peak, op_factor, Year_behaviour, user_list)

