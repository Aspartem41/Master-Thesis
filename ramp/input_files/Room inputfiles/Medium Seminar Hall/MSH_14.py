# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:22:27 2024

@author: Romit
"""

"For Winter sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

MSH = Room("Medium Seminar Hall",N,RP)
Room_list.append(MSH)

df = pd.read_excel('input_files/Room inputfiles/Medium Seminar Hall/Medium Seminar Hall.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours ( 8:00 AM - 6:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For laptop time and For duty cycles

# ----------------------------------------------------------------------------------------------------------------------------------
# 1. Medium Seminar Hall of -- m^2
# ----------------------------------------------------------------------------------------------------------------------------------

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
MSH_Lights = MSH.Appliance(MSH,nl,l_ap,ntf,l_ft_wd,v0,l_mt_wd, wd_we_type = 0, occasional_use = 0.6)
MSH_Lights.windows(t1,t0,v0)

#LIghts - Weekend
# MSH_Lights = MSH.Appliance(MSH,nl,l_ap,ntf,l_ft_we,v0,l_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MSH_Lights.windows(t1,t0,v0)



# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# # 1. Projector
# nprj = df.loc['Projector','Number']
# prj_ap = df.loc['Projector','AP (W)']
# prj_sp = df.loc['Projector','SP (W)']
# prj_apt_wd = df.loc['Projector','APT-WD (mins)']
# prj_apt_we = df.loc['Projector','APT-WE (mins)']
# prj_spt_wd = df.loc['Projector','SPT-WD (mins)']
# prj_spt_we = df.loc['Projector','SPT-WE (mins)']
# prj_ft_wd = df.loc['Projector','FT-WD (mins)']
# prj_ft_we = df.loc['Projector','FT-WE (mins)']
# prj_mt_wd = df.loc['Projector','MT-WD (mins)']
# prj_mt_we = df.loc['Projector','MT-WE (mins)']

# # Projector - Weekdays
# MSH_projector = MSH.Appliance(MSH,nprj,prj_ap,ntf,prj_ft_wd,v0,prj_mt_wd, wd_we_type = 0, occasional_use = 0.8)
# MSH_projector.windows(t1,t0,v0)

# # Projector - Weekend
# MSH_projector = MSH.Appliance(MSH,nprj,prj_ap,ntf,prj_ft_we,v0,prj_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MSH_projector.windows(t1,t0,v0)


# 2. Laptop
nlap = df.loc['Laptop','Number']
lap_ap = df.loc['Laptop','AP (W)']
lap_sp = df.loc['Laptop','SP (W)']
lap_apt_wd = df.loc['Laptop','APT-WD (mins)']
lap_apt_we = df.loc['Laptop','APT-WE (mins)']
lap_spt_wd = df.loc['Laptop','SPT-WD (mins)']
lap_spt_we = df.loc['Laptop','SPT-WE (mins)']
lap_ft_wd = df.loc['Laptop','FT-WD (mins)']
lap_ft_we = df.loc['Laptop','FT-WE (mins)']
lap_mt_wd = df.loc['Laptop','MT-WD (mins)']
lap_mt_we = df.loc['Laptop','MT-WE (mins)']

# Laptop - Weekdays
MSH_Lap = MSH.Appliance(MSH,nlap,lap_ap,ntf,lap_ft_wd,v0,lap_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.6)
MSH_Lap.windows(t1,t0,v0)
MSH_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
MSH_Lap.cycle_behaviour(t1,t0)

# Laptop - Weekend
# MSH_Lap = MSH.Appliance(MSH,nlap,lap_ap,ntf,lap_ft_we,v0,lap_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# MSH_Lap.windows(t1,t0,v0)
# MSH_Lap.specific_cycle_1(lap_ap,lap_apt_we,lap_sp,lap_spt_we,v1)
# MSH_Lap.cycle_behaviour(t1,t0)


# 3. Mobile
nmob = df.loc['Mobile','Number']
mob_ap = df.loc['Mobile','AP (W)']
mob_sp = df.loc['Mobile','SP (W)']
mob_apt_wd = df.loc['Mobile','APT-WD (mins)']
mob_apt_we = df.loc['Mobile','APT-WE (mins)']
mob_spt_wd = df.loc['Mobile','SPT-WD (mins)']
mob_spt_we = df.loc['Mobile','SPT-WE (mins)']
mob_ft_wd = df.loc['Mobile','FT-WD (mins)']
mob_ft_we = df.loc['Mobile','FT-WE (mins)']
mob_mt_wd = df.loc['Mobile','MT-WD (mins)']
mob_mt_we = df.loc['Mobile','MT-WE (mins)']

# Mobile - Weekdays
MSH_Mobile = MSH.Appliance(MSH,nmob,mob_ap,ntf,mob_ft_wd,v0,mob_mt_wd, wd_we_type = 0, occasional_use = 0.6)
MSH_Mobile.windows(t1,t0,v0)

# Mobile - Weekend
# MSH_Mobile = MSH.Appliance(MSH,nmob,mob_ap,ntf,mob_ft_we,v0,mob_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MSH_Mobile.windows(t1,t0,v0)

