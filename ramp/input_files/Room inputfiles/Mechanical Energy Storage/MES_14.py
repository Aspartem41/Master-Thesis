# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:35:47 2024

@author: Romit
"""

"For Winter sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

MES = Room("Mechanical Energy Storage",N,RP)
Room_list.append(MES)

df = pd.read_excel('input_files/Room inputfiles/Mechanical Energy Storage/Mechanical Energy Storage.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours ( 8:00 AM - 6:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.4   # For lights

# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for light

nl = df.loc['Light','Number']                 # Number of the device
l_ap = df.loc['Light','AP (W)']               # Active power of the device 
l_sp = df.loc['Light','SP (W)']               # Stand-by power of the device
l_apt_wd = df.loc['Light','APT-WD (mins)']    # Active power specific cycle time on weekdays 
l_apt_we = df.loc['Light','APT-WE (mins)']    # Active power specific cycle time on weekend
l_spt_wd = df.loc['Light','SPT-WD (mins)']    # Stand-by power specific cycle time on weekdays
l_spt_we = df.loc['Light','SPT-WE (mins)']    # Stand-by power specific cycle time on weekend
l_ft_wd = df.loc['Light','FT-WD (mins)']      # Total function time of the device on weekdays
l_ft_we = df.loc['Light','FT-WE (mins)']      # Total function time of the device on weekend
l_mt_wd = df.loc['Light','MT-WD (mins)']      # Minimum function time of the device on weekdays
l_mt_we = df.loc['Light','MT-WE (mins)']      # Minimum function time of the device on weekend

# Lights - Weekdays
MES_Lights = MES.Appliance(MES,nl,l_ap,ntf,l_ft_wd,v1,l_mt_wd, fixed = 'yes', wd_we_type = 0, occasional_use = 1)
MES_Lights.windows(t1,t0,v0)

#LIghts - Weekend
MES_Lights = MES.Appliance(MES,nl,l_ap,ntf,l_ft_we,v1,l_mt_we, fixed = 'yes', wd_we_type = 1, occasional_use = 0.2)
MES_Lights.windows(t1,t0,v0)