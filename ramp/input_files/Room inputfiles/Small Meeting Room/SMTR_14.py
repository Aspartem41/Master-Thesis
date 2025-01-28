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

SMTR = Room("Small Meeting Room",N,RP)
Room_list.append(SMTR)

df = pd.read_excel('input_files/Room inputfiles/Small Meeting Room/Small Meeting Room.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours ( 8:00 AM - 6:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For laptop time and For duty cycles

# ----------------------------------------------------------------------------------------------------------------------------------
# 1. Small Meeting Room of -- m^2
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
SMTR_Lights = SMTR.Appliance(SMTR,nl,l_ap,ntf,l_ft_wd,v0,l_mt_wd, fixed = 'yes', wd_we_type = 0, occasional_use = 1)
SMTR_Lights.windows(t1,t0,v0)

# Lights - Weekend
# SMTR_Lights = SMTR.Appliance(SMTR,nl,l_ap,ntf,l_ft_we,v0,l_mt_we, fixed = 'yes', wd_we_type = 1, occasional_use = 0.2)
# SMTR_Lights.windows(t1,t0,v0)



# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# 1. TV
ntv = df.loc['TV','Number']
tv_ap = df.loc['TV','AP (W)']
tv_sp = df.loc['TV','SP (W)']
tv_apt_wd = df.loc['TV','APT-WD (mins)']
tv_apt_we = df.loc['TV','APT-WE (mins)']
tv_spt_wd = df.loc['TV','SPT-WD (mins)']
tv_spt_we = df.loc['TV','SPT-WE (mins)']
tv_ft_wd = df.loc['TV','FT-WD (mins)']
tv_ft_we = df.loc['TV','FT-WE (mins)']
tv_mt_wd = df.loc['TV','MT-WD (mins)']
tv_mt_we = df.loc['TV','MT-WE (mins)']

# TV - Weekdays
SMTR_TV = SMTR.Appliance(SMTR,ntv,tv_ap,ntf,tv_ft_wd,v0,tv_mt_wd, wd_we_type = 0, occasional_use = 0.8)
SMTR_TV.windows(t1,t0,v0)

# TV - Weekend
# SMTR_TV = SMTR.Appliance(SMTR,ntv,tv_ap,ntf,tv_ft_we,v0,tv_mt_we, wd_we_type = 1, occasional_use = 0.2)
# SMTR_TV.windows(t1,t0,v0)



# 2. Camera
ncmr = df.loc['Camera','Number']
cmr_ap = df.loc['Camera','AP (W)']
cmr_sp = df.loc['Camera','SP (W)']
cmr_apt_wd = df.loc['Camera','APT-WD (mins)']
cmr_apt_we = df.loc['Camera','APT-WE (mins)']
cmr_spt_wd = df.loc['Camera','SPT-WD (mins)']
cmr_spt_we = df.loc['Camera','SPT-WE (mins)']
cmr_ft_wd = df.loc['Camera','FT-WD (mins)']
cmr_ft_we = df.loc['Camera','FT-WE (mins)']
cmr_mt_wd = df.loc['Camera','MT-WD (mins)']
cmr_mt_we = df.loc['Camera','MT-WE (mins)']

# Camera - Weekdays
SMTR_Camera = SMTR.Appliance(SMTR,ncmr,cmr_ap,ntf,cmr_ft_wd,v0,cmr_mt_wd, wd_we_type = 0, occasional_use = 0.8)
SMTR_Camera.windows(t1,t0,v0)

# Camera - Weekend
# SMTR_Camera = SMTR.Appliance(SMTR,ncmr,cmr_ap,ntf,cmr_ft_we,v0,cmr_mt_we, wd_we_type = 1, occasional_use = 0.2)
# SMTR_Camera.windows(t1,t0,v0)



# 3. Laptop
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
SMTR_Lap = SMTR.Appliance(SMTR,nlap,lap_ap,ntf,lap_ft_wd,v1,lap_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.8)
SMTR_Lap.windows(t1,t0,v0)
SMTR_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
SMTR_Lap.cycle_behaviour(t1,t0)

# Laptop - Weekend
# SMTR_Lap = SMTR.Appliance(SMTR,nlap,lap_ap,ntf,lap_ft_we,v1,lap_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# SMTR_Lap.windows(t1,t0,v0)
# SMTR_Lap.specific_cycle_1(lap_ap,lap_apt_we,lap_sp,lap_spt_we,v1)
# SMTR_Lap.cycle_behaviour(t1,t0)
