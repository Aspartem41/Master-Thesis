# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:36:03 2024

@author: Romit
"""

"For Summer sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

LCOS = Room("Large Corridor with Stairs",N,RP)
Room_list.append(LCOS)

df = pd.read_excel('input_files/Room inputfiles/Large Corridor with Stairs/Large Corridor with Stairs.xlsx', sheet_name = 'SS_Exam' , index_col=0)

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
LCOS_Lights = LCOS.Appliance(LCOS,nl,l_ap,ntf,l_ft_wd,v1,l_mt_wd, wd_we_type = 0, occasional_use = 1)
LCOS_Lights.windows(t1,t0,v0)

# Lights - Weekend
# LCOS_Lights = LCOS.Appliance(LCOS,nl,l_ap,ntf,l_ft_we,v1,l_mt_we, wd_we_type = 1, occasional_use = 0.2)
# LCOS_Lights.windows(t1,t0,v0)