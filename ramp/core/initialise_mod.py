# -*- coding: utf-8 -*-

#%% Initialisation of a model instance

import numpy as np 
import importlib
import datetime
import calendar
# import pytz

# Import holidays package 
import holidays
 

def yearly_pattern(year,start_month,end_month):
    '''
    Definition of a yearly pattern of weekends and weekdays, in case some appliances have specific wd/we behaviour
    '''
    
    #Yearly behaviour pattern
    first_day = datetime.date(year, 1, 1).strftime("%A")
    country = 'DE'
    subdiv= "TH"
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
            Year_behaviour[dict_year[d][1]:year_len:7] = 3
            Year_behaviour[dict_year[d][0]:year_len:7] = 4
            Year_behaviour[dict_year[d][1]:year_len:7] = 4
    
            
    if country == 'EL': 
        country = 'GR'
    elif country == 'FR':
        country = 'FRA'
        
    try:
        holidays_country = list(holidays.CountryHoliday(country,subdiv, years = year).keys())
    except KeyError: 
        c_error = {'LV':'LT', 'RO':'BG'}
        print(f"[WARNING] Due to a known issue, the version of the holidays package you automatically installed is the 0.10.2, not containing {country}. Please refer to 'https://github.com/dr-prodigy/python-holidays/issues/338' for an explanation on how to install holidays 0.10.3. Otherwise, holidays from {c_error[country]} will be used.")
        country = c_error[country]
        holidays_country = list(holidays.CountryHoliday(country, years = year).keys())

    for i in range(len(holidays_country)):
        day_of_year = holidays_country[i].timetuple().tm_yday
        Year_behaviour[day_of_year-1] = 3
    Year_behaviour=Year_behaviour[start_day:end_day]
    # #Yearly behaviour pattern
    # Year_behaviour = np.zeros(365)
    # Year_behaviour[5:365:7] = 1
    # Year_behaviour[6:365:7] = 1
    
    return(Year_behaviour)



def user_defined_inputs(j, t, r):
    room_modules = {
      1.1:  "Room inputfiles.Small Seminar Hall.SSH",
      1.2:  "Room inputfiles.Medium Seminar Hall.MSH",
      1.3:  "Room inputfiles.Large Seminar Hall.LSH",
      2.1:  "Room inputfiles.Small Lecture Hall.SLH",
      2.2:  "Room inputfiles.Medium Lecture Hall.MLH",
      2.3:  "Room inputfiles.Large Lecture Hall.LLH",
        3:  "Room inputfiles.Office 1P.OFF_1P",
        4:  "Room inputfiles.Office 2P.OFF_2P",
        5:  "Room inputfiles.Office 3P.OFF_3P",
        6:  "Room inputfiles.Office 5P.OFF_5P",
        7:  "Room inputfiles.Computer Lab.ITLAB",
      8.1:  "Room inputfiles.Small Meeting Room.SMTR",
      8.2:  "Room inputfiles.Big Meeting Room.BMTR",
      9.1:  "Room inputfiles.Small Toilet.SWC",
      9.2:  "Room inputfiles.Medium Toilet.MWC",
      9.3:  "Room inputfiles.Large Toilet.LWC",
      9.4:  "Room inputfiles.Common Toilet.CWC",
     10.1:  "Room inputfiles.Small Corridor.COS",
     10.2:  "Room inputfiles.Medium Corridor with Stairs.MCOS",
     10.3:  "Room inputfiles.Large Corridor with Stairs.LCOS",
     11.1:  "Room inputfiles.Small Waiting Area.SWA",
     11.2:  "Room inputfiles.Big Waiting Area.BWA",
       12:  "Room inputfiles.Server Room.SR",
       13:  "Room inputfiles.Storage Room.STR",
       14:  "Room inputfiles.Electronics Lab.ELAB",
       15:  "Room inputfiles.Thermal Lab.THLAB",
       16:  "Room inputfiles.Geotech Lab.GTL",
       17:  "Room inputfiles.Water Tech Lab.WTL",
       18:  "Room inputfiles.Hybrid Tech Lab.HTL",
       19:  "Room inputfiles.High Power Lab.HPL",
       20:  "Room inputfiles.Geothermal Lab.GTHL",  
       21:  "Room inputfiles.Personal Room.PR",
     22.1:  "Room inputfiles.Small Kitchen.SKI",
     22.2:  "Room inputfiles.Kitchen 2P.KI2",
     22.3:  "Room inputfiles.Kitchen 4P.KI4",
     22.4:  "Room inputfiles.Kitchen 5P.KI5",
       23:  "Room inputfiles.Bathroom.BT",
       24:  "Room inputfiles.Hallway.HW",
       25:  "Room inputfiles.Dorm Corridor with Stairs.DCOS",
       26:  "Room inputfiles.Hike Lab.HKL",
       27:  "Room inputfiles.Workshop.WKS",
       28:  "Room inputfiles.Design Room.DSR",
       29:  "Room inputfiles.Test Hall.TSH",
       30:  "Room inputfiles.Geo Preparation Room.GPR",
       31:  "Room inputfiles.Mechanical Energy Storage.MES",
       32:  "Room inputfiles.Electric Energy Center.EEC",
       33:  "Room inputfiles.Hydropulse Lab.HYL",
       34:  "Room inputfiles.Biogas Lab.BGL",
       35:  "Room inputfiles.Mechanical Workshop.MWK",
       36:  "Room inputfiles.E-Tech Workshop.EWK",
       37:  "Room inputfiles.Hot Water Center.HWC",
       38:  "Room inputfiles.Multi Work Room.MWR",
       39:  "Room inputfiles.Information Center.IC",
       40:  "Room inputfiles.Shower Room.SWR",
       
       
       
    }

    if r in room_modules:
        module_name = f'input_files.{room_modules[r]}_{j}{t}'
        file_module = importlib.import_module(module_name)
        Room_list = file_module.Room_list
        return Room_list
    else:
        return None


def Initialise_model(year, num_pro):
    '''
    The model is ready to be initialised
    '''
    num_profiles = num_pro
    print('Please wait...') 
    Profile = [] #creates an empty list to store the results of each code run, i.e. each stochastically generated profile
    Room_profile = []
    Room_avg_list = []
    return (Profile, num_profiles,Room_profile, Room_avg_list)
    
def Initialise_inputs(j,t,r,year, start_month, end_month):
    Year_behaviour = yearly_pattern(year,start_month,end_month)
    user_defined_inputs(j,t,r)
    Room_list = user_defined_inputs(j,t,r)
    # Calibration parameters
    '''
    Calibration parameters. These can be changed in case the room has some real data against which the model can be calibrated
    They regulate the probabilities defining the largeness of the peak window and the probability of coincident switch-on within the peak window
    '''
    peak_enlarg = 0.15 #percentage random enlargement or reduction of peak time range length
    mu_peak = 0.5 #median value of gaussian distribution [0,1] by which the number of coincident switch_ons is randomly selected
    s_peak = 0.5 #standard deviation (as percentage of the median value) of the gaussian distribution [0,1] above mentioned
    op_factor = 0.5 #off-peak coincidence calculation parameter

    return (peak_enlarg, mu_peak, s_peak, op_factor, Year_behaviour, Room_list)
