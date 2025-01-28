# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:47:32 2024

@author: Romit
"""

"For Winter sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

PR = Room("Personal Room",N,RP)
Room_list.append(PR)

df = pd.read_excel('input_files/Room inputfiles/Personal Room/Personal Room.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf1 = 3         # Number of timeframes used
ntf2 = 2
t0 = [0,0]
t1 = [0,480]     # 00:00 AM - 8:00 PM
t2 = [480,960]   # 8:00 AM - 4:00 PM
t3 = [960,1440]  # 4:00 PM - 00:00 AM
t4 = [0,1440]    # The whole day for duty cycles

# Variability factors
v0 = 0.2   # For timeframe
v1 = 0.4   # For all

# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for light

nl = df.loc['Light','Number']                 # Number of the device
l_ap = df.loc['Light','AP (W)']               # Active power of the device 
l_sp = df.loc['Light','SP (W)']               # Stand-by power of the device
l_apt_wd = df.loc['Light','APT (mins)']       # Active power specific cycle time 
l_spt_wd = df.loc['Light','SPT (mins)']       # Stand-by power specific cycle time 
l_ft_wd = df.loc['Light','FT (mins)']         # Total function time of the device 
l_mt_wd = df.loc['Light','MT (mins)']         # Minimum function time of the device 

# Light - Allday
PR_Light = PR.Appliance(PR,nl,l_ap,ntf1,l_ft_wd,v1,l_mt_wd, wd_we_type = 2, occasional_use = 0.85)
PR_Light.windows(t3,t1,v0,t2)


# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# 1. Laptop
nlap = df.loc['Laptop','Number']
lap_ap = df.loc['Laptop','AP (W)']
lap_sp = df.loc['Laptop','SP (W)']
lap_apt_wd = df.loc['Laptop','APT (mins)']
lap_spt_wd = df.loc['Laptop','SPT (mins)']
lap_ft_wd = df.loc['Laptop','FT (mins)']
lap_mt_wd = df.loc['Laptop','MT (mins)']

# Laptop - Allday
PR_Lap = PR.Appliance(PR,nlap,lap_ap,ntf1,lap_ft_wd,v1,lap_mt_wd, fixed_cycle = 1, wd_we_type = 2, occasional_use = 0.85)
PR_Lap.windows(t3,t1,v0,t2)
PR_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
PR_Lap.cycle_behaviour(t4,t0)



# 2. Mobile
nmob = df.loc['Mobile','Number']
mob_ap = df.loc['Mobile','AP (W)']
mob_sp = df.loc['Mobile','SP (W)']
mob_apt_wd = df.loc['Mobile','APT (mins)']
mob_spt_wd = df.loc['Mobile','SPT (mins)']
mob_ft_wd = df.loc['Mobile','FT (mins)']
mob_mt_wd = df.loc['Mobile','MT (mins)']

# Mobile - Allday
PR_Mobile = PR.Appliance(PR,nmob,mob_ap,ntf2,mob_ft_wd,v0,mob_mt_wd, wd_we_type = 2, occasional_use = 1)
PR_Mobile.windows(t4,t0,v0)


# 3. Fan
# nfan = df.loc['Fan','Number']
# fan_ap = df.loc['Fan','AP (W)']
# fan_sp = df.loc['Fan','SP (W)']
# fan_apt_wd = df.loc['Fan','APT (mins)']
# fan_spt_wd = df.loc['Fan','SPT (mins)']
# fan_ft_wd = df.loc['Fan','FT (mins)']
# fan_mt_wd = df.loc['Fan','MT (mins)']

# # Fan - Allday
# PR_fan = PR.Appliance(PR,nfan,fan_ap,ntf,fan_ft_wd,v1,fan_mt_wd, wd_we_type = 2, occasional_use = 0.8)
# PR_fan.windows(t1,t3,v0,t2)
