# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:36:31 2024

@author: Romit
"""

"For Summer sem - Break"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100    # Total number of room to be considered
RP = 0     # Room preference

WKS = Room("Workshop",N,RP)
Room_list.append(WKS)

df = pd.read_excel('input_files/Room inputfiles/Workshop/Workshop.xlsx', sheet_name = 'SS_Break' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours (8:00 AM - 6:00 PM)
t2 = [0,1440]    # For Hydroponic (00:00 - 24:00)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For Printer and Cutter

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
WKS_Lights = WKS.Appliance(WKS,nl,l_ap,ntf,l_ft_wd,v0,l_mt_wd, fixed = 'yes', wd_we_type = 0, occasional_use = 0.4)
WKS_Lights.windows(t1,t0,v0)

# Lights - Weekend
# WKS_Lights = WKS.Appliance(WKS,nl,l_ap,ntf,l_ft_we,v0,l_mt_we, fixed = 'yes', wd_we_type = 1, occasional_use = 0.5)
# WKS_Lights.windows(t1,t0,v0)


# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# 1. 3D_Printer
np3d = df.loc['3D_Printer','Number']
p3d_ap = df.loc['3D_Printer','AP (W)']
p3d_sp = df.loc['3D_Printer','SP (W)']
p3d_apt_wd = df.loc['3D_Printer','APT-WD (mins)']
p3d_apt_we = df.loc['3D_Printer','APT-WE (mins)']
p3d_spt_wd = df.loc['3D_Printer','SPT-WD (mins)']
p3d_spt_we = df.loc['3D_Printer','SPT-WE (mins)']
p3d_ft_wd = df.loc['3D_Printer','FT-WD (mins)']
p3d_ft_we = df.loc['3D_Printer','FT-WE (mins)']
p3d_mt_wd = df.loc['3D_Printer','MT-WD (mins)']
p3d_mt_we = df.loc['3D_Printer','MT-WE (mins)']

# 3D_Printer - Weekdays
WKS_p3d = WKS.Appliance(WKS,np3d,p3d_ap,ntf,p3d_ft_wd,v1,p3d_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.8)
WKS_p3d.windows(t1,t0,v0)
WKS_p3d.specific_cycle_1(p3d_ap,p3d_apt_wd,p3d_sp,p3d_spt_wd,v1)
WKS_p3d.cycle_behaviour(t1,t0)

# 3D_Printer - Weekend
# WKS_p3d = WKS.Appliance(WKS,np3d,p3d_ap,ntf,p3d_ft_we,v1,p3d_mt_we, wd_we_type = 1, occasional_use = 0.6)
# WKS_p3d.windows(t1,t0,v0)
# WKS_p3d.specific_cycle_1(p3d_ap,p3d_apt_we,p3d_sp,p3d_spt_we,v1)
# WKS_p3d.cycle_behaviour(t1,t0)


# 2. Laser_Cutter
nlsc = df.loc['Laser_Cutter','Number']
lsc_ap = df.loc['Laser_Cutter','AP (W)']
lsc_sp = df.loc['Laser_Cutter','SP (W)']
lsc_apt_wd = df.loc['Laser_Cutter','APT-WD (mins)']
lsc_apt_we = df.loc['Laser_Cutter','APT-WE (mins)']
lsc_spt_wd = df.loc['Laser_Cutter','SPT-WD (mins)']
lsc_spt_we = df.loc['Laser_Cutter','SPT-WE (mins)']
lsc_ft_wd = df.loc['Laser_Cutter','FT-WD (mins)']
lsc_ft_we = df.loc['Laser_Cutter','FT-WE (mins)']
lsc_mt_wd = df.loc['Laser_Cutter','MT-WD (mins)']
lsc_mt_we = df.loc['Laser_Cutter','MT-WE (mins)']

# Laser_Cutter - Weekdays
WKS_lsc = WKS.Appliance(WKS,nlsc,lsc_ap,ntf,lsc_ft_wd,v1,lsc_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.6)
WKS_lsc.windows(t1,t0,v0)
WKS_lsc.specific_cycle_1(lsc_ap,lsc_apt_wd,lsc_sp,lsc_spt_wd,v1)
WKS_lsc.cycle_behaviour(t1,t0)

# Laser_Cutter - Weekend
# WKS_lsc = WKS.Appliance(WKS,nlsc,lsc_ap,ntf,lsc_ft_we,v1,lsc_mt_we, wd_we_type = 1, occasional_use = 0.6)
# WKS_lsc.windows(t1,t0,v0)
# WKS_lsc.specific_cycle_1(lsc_ap,lsc_apt_we,lsc_sp,lsc_spt_we,v1)
# WKS_lsc.cycle_behaviour(t1,t0)


# 3. Hydroponic
nhydp = df.loc['Hydroponic','Number']
hydp_ap = df.loc['Hydroponic','AP (W)']
hydp_sp = df.loc['Hydroponic','SP (W)']
hydp_apt_wd = df.loc['Hydroponic','APT-WD (mins)']
hydp_apt_we = df.loc['Hydroponic','APT-WE (mins)']
hydp_spt_wd = df.loc['Hydroponic','SPT-WD (mins)']
hydp_spt_we = df.loc['Hydroponic','SPT-WE (mins)']
hydp_ft_wd = df.loc['Hydroponic','FT-WD (mins)']
hydp_ft_we = df.loc['Hydroponic','FT-WE (mins)']
hydp_mt_wd = df.loc['Hydroponic','MT-WD (mins)']
hydp_mt_we = df.loc['Hydroponic','MT-WE (mins)']

# Hydroponic - Everyday
WKS_Hydroponic = WKS.Appliance(WKS,nhydp,hydp_ap,ntf,hydp_ft_wd,v0,hydp_mt_wd, wd_we_type = 2, occasional_use = 0.8)
WKS_Hydroponic.windows(t2,t0,v0)