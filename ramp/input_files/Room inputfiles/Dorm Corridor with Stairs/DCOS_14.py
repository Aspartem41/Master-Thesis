# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:30:33 2024

@author: Romit
"""

"For Winter sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

DCOS = Room("Dorm Corridor with Stairs",N,RP)
Room_list.append(DCOS)

df = pd.read_excel('input_files/Room inputfiles/Dorm Corridor with Stairs/Dorm Corridor with Stairs.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf = 2           # Number of timeframes used
t0 = [0,0] 
t1 = [0,540]       # 00:00 AM - 09:00 AM
t2 = [1020,1440]   # 04:00 PM - 00:00 AM
 
# Variability factors
v0 = 0.1   # For timeframe and Hairdryer
v1 = 0.2   # For lights

# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for light

nl = df.loc['Light','Number']                 # Number of the device
l_ap = df.loc['Light','AP (W)']               # Active power of the device 
l_ft = df.loc['Light','FT (mins)']            # Total function time of the device 
l_mt = df.loc['Light','MT (mins)']            # Minimum function time of the device 


# Light - Alldays
DCOS_Light = DCOS.Appliance(DCOS,nl,l_ap,ntf,l_ft,v1,l_mt, fixed = 'yes', wd_we_type = 2, occasional_use = 1)
DCOS_Light.windows(t1,t2,v0)
