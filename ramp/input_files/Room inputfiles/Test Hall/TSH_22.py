# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:37:16 2024

@author: Romit
"""

"For Summer sem - Spring"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 1   # Total number of room to be considered
RP = 0     # Room preference

TSH = Room("Test Hall",N,RP)
Room_list.append(TSH)

df = pd.read_excel('input_files/Room inputfiles/Test Hall/Test Hall.xlsx', sheet_name = 'SS_Spring' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours (8:00 AM - 6:00 PM)
t2 = [960,1200]  # Wind Tunnel experiment (4:00 PM - 8:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For all devices/loads

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
TSH_Lights = TSH.Appliance(TSH,nl,l_ap,ntf,l_ft_wd,v1,l_mt_wd, fixed = 'yes', wd_we_type = 0, occasional_use = 0.8)
TSH_Lights.windows(t1,t0,v0)

# Lights - Weekend
# TSH_Lights = TSH.Appliance(TSH,nl,l_ap,ntf,l_ft_we,v1,l_mt_we, fixed = 'yes', wd_we_type = 1, occasional_use = 0.2)
# TSH_Lights.windows(t1,t0,v0)



# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads

# # 1. Solar Thermal
# nslth = df.loc['Solar Thermal','Number']
# slth_ap = df.loc['Solar Thermal','AP (W)']
# slth_sp = df.loc['Solar Thermal','SP (W)']
# slth_apt_wd = df.loc['Solar Thermal','APT-WD (mins)']
# slth_apt_we = df.loc['Solar Thermal','APT-WE (mins)']
# slth_spt_wd = df.loc['Solar Thermal','SPT-WD (mins)']
# slth_spt_we = df.loc['Solar Thermal','SPT-WE (mins)']
# slth_ft_wd = df.loc['Solar Thermal','FT-WD (mins)']
# slth_ft_we = df.loc['Solar Thermal','FT-WE (mins)']
# slth_mt_wd = df.loc['Solar Thermal','MT-WD (mins)']
# slth_mt_we = df.loc['Solar Thermal','MT-WE (mins)']

# # Solar Thermal - Weekdays
# TSH_slth = TSH.Appliance(TSH,nslth,slth_ap,ntf,slth_ft_wd,v1,slth_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# TSH_slth.windows(t1,t0,v0)
# TSH_slth.specific_cycle_1(slth_ap,slth_apt_wd,slth_sp,slth_spt_wd,v1)
# TSH_slth.cycle_behaviour(t1,t0)

# # Solar Thermal - Weekend
# # TSH_slth = TSH.Appliance(TSH,nslth,slth_ap,ntf,slth_ft_we,v1,slth_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # TSH_slth.windows(t1,t0,v0)
# # TSH_slth.specific_cycle_1(slth_ap,slth_apt_we,slth_sp,slth_spt_we,v1)
# # TSH_slth.cycle_behaviour(t1,t0)



# # 2. Temperature Unit
# ntmpu = df.loc['Temperature Unit','Number']
# tmpu_ap = df.loc['Temperature Unit','AP (W)']
# tmpu_sp = df.loc['Temperature Unit','SP (W)']
# tmpu_apt_wd = df.loc['Temperature Unit','APT-WD (mins)']
# tmpu_apt_we = df.loc['Temperature Unit','APT-WE (mins)']
# tmpu_spt_wd = df.loc['Temperature Unit','SPT-WD (mins)']
# tmpu_spt_we = df.loc['Temperature Unit','SPT-WE (mins)']
# tmpu_ft_wd = df.loc['Temperature Unit','FT-WD (mins)']
# tmpu_ft_we = df.loc['Temperature Unit','FT-WE (mins)']
# tmpu_mt_wd = df.loc['Temperature Unit','MT-WD (mins)']
# tmpu_mt_we = df.loc['Temperature Unit','MT-WE (mins)']

# # Temperature Unit - Weekdays
# TSH_tmpui = TSH.Appliance(TSH,ntmpu,tmpu_ap,ntf,tmpu_ft_wd,v1,tmpu_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# TSH_tmpui.windows(t1,t0,v0)

# # Temperature Unit - Weekend
# # TSH_tmpui = TSH.Appliance(TSH,ntmpu,tmpu_ap,ntf,tmpu_ft_we,v1,tmpu_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # TSH_tmpui.windows(t1,t0,v0)



# 3. Wind Tunnel
nwntl = df.loc['Wind Tunnel','Number']
wntl_ap = df.loc['Wind Tunnel','AP (W)']
wntl_sp = df.loc['Wind Tunnel','SP (W)']
wntl_apt_wd = df.loc['Wind Tunnel','APT-WD (mins)']
wntl_apt_we = df.loc['Wind Tunnel','APT-WE (mins)']
wntl_spt_wd = df.loc['Wind Tunnel','SPT-WD (mins)']
wntl_spt_we = df.loc['Wind Tunnel','SPT-WE (mins)']
wntl_ft_wd = df.loc['Wind Tunnel','FT-WD (mins)']
wntl_ft_we = df.loc['Wind Tunnel','FT-WE (mins)']
wntl_mt_wd = df.loc['Wind Tunnel','MT-WD (mins)']
wntl_mt_we = df.loc['Wind Tunnel','MT-WE (mins)']

# Wind Tunnel - Weekdays
TSH_wntl = TSH.Appliance(TSH,nwntl,wntl_ap,ntf,wntl_ft_wd,v1,wntl_mt_wd, wd_we_type = 0, occasional_use = 0.4)
TSH_wntl.windows(t2,t0,v0)
TSH_wntl.specific_cycle_1(wntl_ap,wntl_apt_wd,wntl_sp,wntl_spt_wd,v1)
TSH_wntl.cycle_behaviour(t2,t0)

# Wind Tunnel - Weekend
# TSH_wntl = TSH.Appliance(TSH,nwntl,wntl_ap,ntf,wntl_ft_we,v1,wntl_mt_we, wd_we_type = 1, occasional_use = 0.2)
# TSH_wntl.windows(t2,t0,v0)
# TSH_wntl.specific_cycle_1(wntl_ap,wntl_apt_we,wntl_sp,wntl_spt_we,v1)
# TSH_wntl.cycle_behaviour(t2,t0)


# # 4. Climatic Chamber
# ncchmbr = df.loc['Climatic Chamber','Number']
# cchmbr_ap = df.loc['Climatic Chamber','AP (W)']
# cchmbr_sp = df.loc['Climatic Chamber','SP (W)']
# cchmbr_apt_wd = df.loc['Climatic Chamber','APT-WD (mins)']
# cchmbr_apt_we = df.loc['Climatic Chamber','APT-WE (mins)']
# cchmbr_spt_wd = df.loc['Climatic Chamber','SPT-WD (mins)']
# cchmbr_spt_we = df.loc['Climatic Chamber','SPT-WE (mins)']
# cchmbr_ft_wd = df.loc['Climatic Chamber','FT-WD (mins)']
# cchmbr_ft_we = df.loc['Climatic Chamber','FT-WE (mins)']
# cchmbr_mt_wd = df.loc['Climatic Chamber','MT-WD (mins)']
# cchmbr_mt_we = df.loc['Climatic Chamber','MT-WE (mins)']

# # Climatic Chamber - Weekdays
# TSH_cchmbr = TSH.Appliance(TSH,ncchmbr,cchmbr_ap,ntf,cchmbr_ft_wd,v1,cchmbr_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# TSH_cchmbr.windows(t1,t0,v0)

# # Climatic Chamber - Weekend
# # TSH_Climatic Chamber = TSH.Appliance(TSH,ncchmbr,cchmbr_ap,ntf,cchmbr_ft_we,v1,cchmbr_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # TSH_Climatic Chamber.windows(t1,t0,v0)
