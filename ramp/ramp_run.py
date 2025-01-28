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
import numpy as np
import matplotlib.pyplot as plt


# Set code starting time, to compute execution time
startTime = datetime.now()

year = 2022  # Year to be simulated

Rooms = { 1.1: 'Small Seminar Hall', 1.2: 'Medium Seminar Hall', 1.3: 'Large Seminar Hall', 2.1: 'Small Lecture Hall', 2.2: 'Medium Lecture Hall', 2.3: 'Large Lecture Hall', 3: 'Office 1P', 4: 'Office 2P', 5: 'Office 3P', 6: 'Office 5P', 11.1: 'Small Waiting Area', 11.2: 'Big Waiting Area', 
         7: 'Computer Lab', 8.1: 'Small Meeting Room', 8.2: 'Big Meeting Room', 9.1: 'Small Toilet', 9.2: 'Medium Toilet', 9.3: 'Large Toilet', 9.4: 'Common Toilet', 10.1: 'Small Corridor', 10.2: 'Medium Corridor with Stairs', 10.3: 'Large Corridor with Stairs',
         12: 'Server Room', 13: 'Storage Room', 14: 'Electronics Lab', 15: 'Thermal Lab', 16: 'Geotech Lab', 17: 'Water Tech Lab', 18: 'Hybrid Tech Lab', 19: 'High Power Lab', 20: 'Geothermal Lab', 21: 'Personal Room', 22.1: 'Small Kitchen', 22.2: 'Kitchen 2P', 22.3: 'Kitchen 4P', 22.4: 'Kitchen 5P',
         23: 'Bathroom', 24: 'Hallway', 25: 'Dorm Corridor with Stairs', 26: 'Hike Lab' , 27: 'Workshop', 28: 'Design Room',  29: 'Test Hall', 30: 'Geo Preparation Room', 31:'Mechanical Energy Storage', 32: 'Electric Energy Center', 33: 'Hydropulse Lab', 34: 'Biogas Lab', 35: 'Mechanical Workshop',
         36: 'E-Tech Workshop', 37: 'Hot Water Center', 38: 'Multi Work Room', 39: 'Information Center', 40: 'Shower Room',
}

Room_code = float(input('Please choose the room code: '))
Room = Rooms.get(Room_code, None)

if Room is None:
    print("Invalid room code")

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

# Define which input parameters 
input_parameter_1 = [Semester_choice]
input_parameter_2 = [Sub_choice]
for_which_room = [Room_code]

# Calls the stochastic process and saves the result in a list of stochastic profiles
for j in input_parameter_1:
    for t in input_parameter_2:
        for r in for_which_room:
    
         Profiles_list, Room_profile, Room_list, Room_load, all_rooms_avg = Stochastic_Process(j,t,r,year, start_month, end_month, num_pro)
        
# Post-processes the results and generates plots
         Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(Profiles_list)
         Profile_room = pp.Profiles_room_formatting(Room_profile)
         # Avg_all_room = pp.Profiles_room_formatting(all_rooms_avg)
         pp.Profile_series_plot(Profiles_series) #by default, profiles are plotted as a series
         
         rooms_avg, rooms_list_kW, rooms_series = pp.Room_formatting(Room_load)
        
         pp.export_series(Profiles_series,j)
    
         if len(Profiles_list) > 1: #if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
         if len(Room_load) > 1:     #if more than one room is considered, also cloud plots are shown for N rooms
            pp.Room_cloud_plot(Room_load, rooms_avg)
            
#%%
# Room_df = pd.DataFrame.from_dict(all_rooms_avg)
# Room_df = pd.DataFrame.from_dict(Profile_room)

Profiles_series= pd.DataFrame(Profiles_series)

date_time_index = pd.date_range(name='Date',start= str(start_month)+'/1/2022', periods=len(Profiles_series),
                            freq='1min')

Profiles_series = Profiles_series.set_index(date_time_index)
Profiles_series_h = Profiles_series.resample('H').mean() 
Profiles_series_h.rename(columns = { 0: 'Power Consumption'}, inplace=True)
Profiles_series_h.head()

Consumption_kW = Profiles_series_h/1000       # W to kW

figsize = (10,5)
ax = Consumption_kW.plot(kind='line', color= 'blue', drawstyle= 'steps-post', rot=0, fontsize=15, legend=True, figsize = figsize)
ax.set_ylabel('Power [kW]', fontsize = 15)
ax.grid()
ax.set_title(f'Loadprofile of {Room}', fontsize = 15) 



#%%
# Saving load profiles in csv formate
#Consumption_kW.to_csv('Room_results/'+ 'Building '+ Building + '/' + Simulation_name + '/Load Profile '+ str(0)+str(start_month)+'-'+ str(0)+str(end_month)+'.csv')
Consumption_kW.to_csv('Room_results/'+ Room + '/' + Simulation_name + '/Load Profile '+ str(0)+str(start_month)+'-'+ str(0)+str(end_month)+'.csv')
print('\nExecution Time:', datetime.now() - startTime)

