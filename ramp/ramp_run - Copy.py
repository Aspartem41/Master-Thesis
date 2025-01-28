 # -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:35:00 2019
This is the code for the open-source stochastic model for the generation of 
multi-energy load profiles in off-grid areas, called RAMP, v0.3.0.

@authors:
- Francesco Lombardi, Politecnico di Milano
- Sergio Balderrama, Université de Liège
- Sylvain Quoilin, KU Leuven
- Emanuela Colombo, Politecnico di Milano

Copyright 2019 RAMP, contributors listed above.
Licensed under the European Union Public Licence (EUPL), Version 1.2;
you may not use this file except in compliance with the License.

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations
under the License.
"""

#%% Import required modules

import sys,os
sys.path.append('../')
from core.stochastic_process_mod import Stochastic_Process
from ramp.core.initialise_mod import Initialise_model
from post_process import post_process as pp
from datetime import datetime
import pandas as pd
from pid import PidFile
import numpy as np
import matplotlib.pyplot as plt


# Set code starting time, to compute execution time
startTime = datetime.now()

year = 2022

building_num= int(input('Please choose the building number: '))

if building_num == 5:
    Building = '5'
elif building_num == 6:
    Building = '6'
elif building_num == 8:
    Building = '8'
elif building_num == 11:
    Building = '11'
elif building_num == 13:
    Building = '13'
elif building_num == 14:
    Building = '14'
elif building_num == 19:
    Building = '19'
elif building_num == 22:
    Building = '22'
elif building_num == 34:
    Building = '34'
    
Semester_choice =int(input('Please choose a semester: 1-Winter_sem, 2-Summer_sem: ')) #[1,2,3,4]

if Semester_choice == 1:
    Sub_choice = int(input('Please choose a option for Winter semester: 1-Semester break, 2-Autumn, 3-Winter, 4-Examination period: '))
    if Sub_choice == 1:
        Simulation_name = 'WS_Break'    # Winter season
    elif Sub_choice == 2:
        Simulation_name = 'WS_Autumn'
    elif Sub_choice == 3:
        Simulation_name = 'WS_Winter'      
    elif Sub_choice == 4:
        Simulation_name = 'WS_Exam'     # Spring season
    else:
        Simulation_name = 'Invalid sub-choice'
elif Semester_choice == 2:
    Sub_choice = int(input('Please choose a option for Summer semester: 1-Semester break, 2-Spring, 3-Summer, 4-Examination period: '))
    if Sub_choice == 1:
        Simulation_name = 'SS_Break'    # Summer season
    elif Sub_choice == 2:
        Simulation_name = 'SS_Spring'
    elif Sub_choice == 3:
        Simulation_name = 'SS_Summer'     
    elif Sub_choice == 4:
        Simulation_name = 'SS_Exam'    # Autumn season
    else:
        Simulation_name = 'Invalid sub-choice'
else:
    Simulation_name = 'Invalid semester choice'
    


#Simulation_name = input('Bitte den Simulationname name eingeben: ')
start_month = int(input('Enter the start month: '))       # 1-12 == Jan-Dez
end_month = int(input('Enter the end month: '))             # 2-13 == Feb-Jan

num_pro = int(input('How many days must be simulated?: '))

# Define which input files should be considered and run. 
# Files are specified as numbers in a list (e.g. [1,2] will consider input_file_1.py and input_file_2.py)


#pro,Num_profiles = Initialise_model()
#Num_Profiles = int(input("please indicate the number of profiles to be generated: "))  # Should be the same as the requested no.of Profiles
input_parameter_1 = [Semester_choice]
input_parameter_2 = [Sub_choice]
for_which_building = [building_num]
# Calls the stochastic process and saves the result in a list of stochastic profiles
for j in input_parameter_1:
    for t in input_parameter_2:
        for r in for_which_building:
    
         Profiles_list, User_profile, User_list = Stochastic_Process(j,t,r,year, start_month, end_month, num_pro)
        
# Post-processes the results and generates plots
         Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(Profiles_list)
         Profile_user = pp.Profiles_user_formatting(User_profile)
         pp.Profile_series_plot(Profiles_series) #by default, profiles are plotted as a series
        
         pp.export_series(Profiles_series,j)
    
         if len(Profiles_list) > 1: #if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
#%%

User_df = pd.DataFrame.from_dict(User_profile)
#number_of_time_steps = 24*60*Num_Profiles
Profiles_series= pd.DataFrame(Profiles_series)

date_time_index = pd.date_range(name='Date',start= str(start_month)+'/1/2022', periods=len(Profiles_series),
                            freq='1min')

Profiles_series = Profiles_series.set_index(date_time_index)
Profiles_series_h = Profiles_series.resample('H').mean() 
Profiles_series_h.rename(columns = { 0: 'Power Consumption'}, inplace=True)
Profiles_series_h.head()

Consumption_kW = Profiles_series_h/1000       # W to kW


#Skalierung

# def Profile_formatting(n_user_profiles):
#     n_user_avg = np.zeros(1440)
#     for u in n_user_profiles:
#         n_user_avg = n_user_avg + u
#     n_user_avg = n_user_avg/len(n_user_profiles)
    
#     Profile_kW = []
#     for kW in n_user_profiles:
#         Profile_kW.append(kW/1000)
    
#     Profile_series = np.array([])
#     for uuu in n_user_profiles:
#         Profile_series = np.append(Profile_series,uuu)
    
#     return (n_user_avg, Profile_kW, Profile_series)

# def Profile_cloud_plot(n_user_profiles,n_user_profiles_avg):
#     #x = np.arange(0,1440,5)
#     plt.figure(figsize=(10,5))
#     for n in n_user_profiles:
#         plt.plot(np.arange(1440),n,'#b0c4de')
#         plt.xlabel('Time (hours)')
#         plt.ylabel('Power (W)')
#         plt.ylim(ymin=0)
#         #plt.ylim(ymax=5000)
#         plt.margins(x=0)
#         plt.margins(y=0)
#     plt.plot(np.arange(1440),n_user_profiles_avg,'#4169e1')
#     plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
#     #plt.savefig('profiles.eps', format='eps', dpi=1000)
#     plt.show()

figsize = (10,5)
ax = Consumption_kW.plot(kind='line', color= 'blue', drawstyle= 'steps-post', rot=0, fontsize=15, legend=True, figsize = figsize)
ax.set_ylabel('Power [kW]', fontsize = 15)
ax.grid()
ax.set_title(" Loadprofile of Building ", fontsize = 15) 



#%% Ergebnisse

# Saving load profiles in csv formate
#Consumption_kW.to_csv('Romit_results/'+ 'Building '+ Building + '/' + Simulation_name + '/Load Profile '+ str(0)+str(start_month)+'-'+ str(0)+str(end_month)+'.csv')

print('\nExecution Time:', datetime.now() - startTime)

