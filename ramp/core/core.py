# -*- coding: utf-8 -*-

#%% Import required libraries
import numpy as np
import numpy.ma as ma
import pandas as pd
#%% Definition of Python classes that constitute the model architecture
'''
The code is based on two concatenated python classes, namely 'room' and
'Appliance', which are used to define at the outer level the room classes and 
at the inner level all the available appliances within each room class, with 
their own characteristics. Within the Appliance class, some other functions are
created to define windows of use and, if needed, specific duty cycles
'''

#Define the outer python class that represents 'Room classes'
class Room():
    
    def __init__(self, name = "", n_rooms = 1, rm_pref = 0):
        self.room_name = name
        self.num_rooms = n_rooms #specifies the number of rooms within the class
        self.room_preference = rm_pref #allows to check if random number coincides with room preference, to distinguish between various appliance_use options (e.g. different cooking options)
        self.App_list = [] #each instance of room (i.e. each room class) has its own list of Appliances

#Define the inner class for modelling room's appliances within the correspoding room class
    class Appliance():
    
        def __init__(self,room, n = 1, P = 0, w = 1, t = 0, r_t = 0, c = 1, fixed = 'no', fixed_cycle = 0, occasional_use = 1, flat = 'no', thermal_P_var = 0, pref_index = 0, wd_we_type = 3, P_series = False):
            self.room = room #room to which the appliance is bounded
            self.number = n #number of appliances of the specified kind
            self.num_windows = w #number of functioning windows to be considered
            self.func_time = t #total time the appliance is on during the day
            self.r_t = r_t #percentage of total time of use that is subject to random variability
            self.func_cycle = c #minimum time the appliance is kept on after switch-on event 
            self.fixed = fixed #if 'yes', all the 'n' appliances of this kind are always switched-on together
            self.activate = fixed_cycle #if equal to 1,2 or 3, respectively 1,2 or 3 duty cycles can be modelled, for different periods of the day
            self.occasional_use = occasional_use #probability that the appliance is always (i.e. everyday) included in the mix of appliances that the room actually switches-on during the day
            self.flat = flat #allows to model appliances that are not subject to any kind of random variability, such as public lighting
            self.Thermal_P_var = thermal_P_var #allows to randomly variate the App power within a range
            self.Pref_index = pref_index #defines preference index for association with random room daily preference behaviour
            self.wd_we = wd_we_type #defines if the App is associated with weekdays or weekends | 0 is wd, 1 is sat, 2 is all days, 3 is holidays/sunday, 4 is sat and sun only
            if P_series == False and isinstance(P, pd.DataFrame) == False: #check if the room defined P as timeseries
                self.POWER = P*np.ones(365) #treat the power as single value for the entire year
            else:
                self.POWER = P.values[:,0] #if a timeseries is given the power is treated as so    
            
        def windows(self, w1 = np.array([0,0]), w2 = np.array([0,0]),r_w = 0, w3 = np.array([0,0]), w4 = np.array([0,0])):    
            self.window_1 = w1 #array of start and ending time for window of use #1
            self.window_2 = w2 #array of start and ending time for window of use #2
            self.window_3 = w3 #array of start and ending time for window of use #3
            self.window_4 = w4 #array of start and ending time for window of use #4
            self.random_var_w = r_w #percentage of variability in the start and ending times of the windows
            self.daily_use = np.zeros(1440) #create an empty daily use profile
            self.daily_use[w1[0]:(w1[1])] = np.full(np.diff(w1),0.001) #fills the daily use profile with infinitesimal values that are just used to identify the functioning windows
            self.daily_use[w2[0]:(w2[1])] = np.full(np.diff(w2),0.001) #same as above for window2
            self.daily_use[w3[0]:(w3[1])] = np.full(np.diff(w3),0.001) #same as above for window3
            self.daily_use[w4[0]:(w4[1])] = np.full(np.diff(w4),0.001) #same as above for window4
            self.daily_use_masked = np.zeros_like(ma.masked_not_equal(self.daily_use,0.001)) #apply a python mask to the daily_use array to make only functioning windows 'visibile'
            self.random_var_1 = int(r_w*np.diff(w1)) #calculate the random variability of window1, i.e. the maximum range of time they can be enlarged or shortened
            self.random_var_2 = int(r_w*np.diff(w2)) #same as above
            self.random_var_3 = int(r_w*np.diff(w3)) #same as above
            self.random_var_4 = int(r_w*np.diff(w4)) #same as above
            self.room.App_list.append(self) #automatically appends the appliance to the room's appliance list
            
            #if needed, specific duty cycles can be defined for each Appliance, for a maximum of four different ones
        def specific_cycle_1(self, P_11 = 0, t_11 = 0, P_12 = 0, t_12 = 0, r_c1 = 0):
            self.P_11 = P_11 #power absorbed during first part of the duty cycle
            self.t_11 = t_11 #duration of first part of the duty cycle
            self.P_12 = P_12 #power absorbed during second part of the duty cycle
            self.t_12 = t_12 #duration of second part of the duty cycle
            self.r_c1 = r_c1 #random variability of duty cycle segments duration
            #self.fixed_cycle1 = np.concatenate(((np.ones(t_11)*P_11),(np.ones(t_12)*P_12))) #create numpy array representing the duty cycle
            self.fixed_cycle1 = np.concatenate(((np.ones(int(t_11))*P_11),(np.ones(int(t_12))*P_12)))
            
        def specific_cycle_2(self, P_21 = 0, t_21 = 0, P_22 = 0, t_22 = 0, r_c2 = 0):
            self.P_21 = P_21 #same as for cycle1
            self.t_21 = t_21
            self.P_22 = P_22
            self.t_22 = t_22
            self.r_c2 = r_c2
            self.fixed_cycle2 = np.concatenate(((np.ones(int(t_21))*P_21),(np.ones(int(t_22))*P_22)))
        
        def specific_cycle_3(self, P_31 = 0, t_31 = 0, P_32 = 0, t_32 = 0, r_c3 = 0):
            self.P_31 = P_31 #same as for cycle1
            self.t_31 = t_31
            self.P_32 = P_32
            self.t_32 = t_32
            self.r_c3 = r_c3
            self.fixed_cycle3 = np.concatenate(((np.ones(int(t_31))*P_31),(np.ones(int(t_32))*P_32)))
        
        def specific_cycle_4(self, P_41 = 0, t_41 = 0, P_42 = 0, t_42 = 0, r_c4 = 0):
            self.P_41 = P_41 #same as for cycle1
            self.t_41 = t_41
            self.P_42 = P_42
            self.t_42 = t_42
            self.r_c4 = r_c4
            self.fixed_cycle4 = np.concatenate(((np.ones(t_41)*P_41),(np.ones(t_42)*P_42)))
            
        #different time windows can be associated with different specific duty cycles
        def cycle_behaviour(self, cw11 = np.array([0,0]), cw12 = np.array([0,0]), cw21 = np.array([0,0]), cw22 = np.array([0,0]), cw31 = np.array([0,0]), cw32 = np.array([0,0]), cw41 = np.array([0,0]), cw42 = np.array([0,0])):
            self.cw11 = cw11 #first window associated with cycle1
            self.cw12 = cw12 #second window associated with cycle1
            self.cw21 = cw21 #same for cycle2
            self.cw22 = cw22
            self.cw31 = cw31 #same for cycle 3
            self.cw32 = cw32
            self.cw41 = cw41 #same for cycle 4
            self.cw42 = cw42
            
