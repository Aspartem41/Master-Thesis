# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:35:47 2024

@author: Romit
"""

"For Winter sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100    # Total number of room to be considered
RP = 0     # Room preference

BT = Room("Bathroom",N,RP)
Room_list.append(BT)

df = pd.read_excel('input_files/Room inputfiles/Bathroom/Bathroom.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf = 3           # Number of timeframes used
t0 = [0,0] 
t1 = [300,540]     # 05:00 AM - 09:00 AM
t2 = [600,1020]    # 10:00 AM - 05:00 PM
t3 = [1080,1320]   # 06:00 PM - 10:00 PM
 
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
BT_Light = BT.Appliance(BT,nl,l_ap,ntf,l_ft,v1,l_mt, wd_we_type = 2, occasional_use = 1)
BT_Light.windows(t1,t2,v0,t3)


# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# 1. Hairdryer
nhdry = df.loc['Hairdryer','Number']
hdry_ap = df.loc['Hairdryer','AP (W)']
hdry_ft = df.loc['Hairdryer','FT (mins)']
hdry_mt = df.loc['Hairdryer','MT (mins)']


# Hairdryer - Alldays
BT_Hairdryer = BT.Appliance(BT,nhdry,hdry_ap,ntf,hdry_ft,v0,hdry_mt, wd_we_type = 2, occasional_use = 0.5)
BT_Hairdryer.windows(t1,t2,v0,t3)
