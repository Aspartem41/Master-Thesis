# -*- coding: utf-8 -*-

#%% Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%% Post-processing
'''
Just some additional code lines to calculate useful indicators and generate plots
'''
def Profile_formatting(stoch_profiles):
    Profile_avg = np.zeros(1440)
    for pr in stoch_profiles:
        Profile_avg = Profile_avg + pr
    Profile_avg = Profile_avg/len(stoch_profiles)
    
    Profile_kW = []
    for kW in stoch_profiles:
        Profile_kW.append(kW/1000)
    
    Profile_series = np.array([])
    for iii in stoch_profiles:
        Profile_series = np.append(Profile_series,iii)
    
    return (Profile_avg, Profile_kW, Profile_series)

def Profiles_room_formatting(stoch_profiles):
    Profiles_room_format = {}
    for rm_type in stoch_profiles[0]:
        Profiles_room_format[rm_type] = []
        for day in range(len(stoch_profiles)):
            try:
                temp = np.stack(stoch_profiles[day][rm_type], axis=-1)
            except:
                temp = np.zeros((1440,1))
            Profiles_room_format[rm_type].append(temp)
            #rm_type_list =  Profiles_room_format[rm_type]
        Profiles_room_format[rm_type] = np.vstack(Profiles_room_format[rm_type])
    return Profiles_room_format

def Profile_cloud_plot(stoch_profiles,stoch_profiles_avg):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    for n in stoch_profiles:
        plt.plot(np.arange(1440),n,'#b0c4de')
        plt.xlabel('Time (hours)')
        plt.ylabel('Power (W)')
        plt.ylim(ymin=0)
        #plt.ylim(ymax=5000)
        plt.margins(x=0)
        plt.margins(y=0)
    plt.plot(np.arange(1440),stoch_profiles_avg,'#4169e1')
    plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()
    
def Room_formatting(stoch_rooms):
    Room_avg = np.zeros(1440)
    for r in stoch_rooms:
        Room_avg = Room_avg + r
    Room_avg = Room_avg/len(stoch_rooms)
    
    Room_kW = []
    for kW in stoch_rooms:
        Room_kW.append(kW/1000)
    
    Room_series = np.array([])
    for iii in stoch_rooms:
        Room_series = np.append(Room_series,iii)
    
    return (Room_avg, Room_kW, Room_series)
    
def Room_cloud_plot(stoch_rooms,stoch_rooms_avg):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    for n in stoch_rooms:
        plt.plot(np.arange(1440),n,'#b0c4de')
        plt.xlabel('Time (hours)')
        plt.ylabel('Power (W)')
        plt.ylim(ymin=0)
        #plt.ylim(ymax=5000)
        plt.margins(x=0)
        plt.margins(y=0)
    plt.plot(np.arange(1440),stoch_rooms_avg,'#4169e1')
    plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    plt.title('Average of N Rooms', fontsize=14)
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()


def Profile_series_plot(stoch_profiles_series):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    plt.plot(np.arange(len(stoch_profiles_series)),stoch_profiles_series,'#4169e1')
    #plt.xlabel('Time (hours)')
    plt.ylabel('Power (W)')
    plt.ylim(ymin=0)
    #plt.ylim(ymax=5000)
    plt.margins(x=0)
    plt.margins(y=0)
    #plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()

def Resample(df):
    
    df = df.resample('H').mean()
    
    return df
#%% Export individual profiles
'''
for i in range (len(Profile)):
    np.save('p0%d.npy' % (i), Profile[i])
'''

# Export Profiles

def export_series(stoch_profiles_series, j):
    series_frame = pd.DataFrame(stoch_profiles_series)
    #series_frame.to_csv('Romit_results_old/output_file_%d.csv' % (j))