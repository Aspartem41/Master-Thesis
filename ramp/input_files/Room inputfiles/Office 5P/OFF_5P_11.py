# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:22:29 2024

@author: Romit
"""

"For Winter sem - Break"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100    # Total number of 5 person office to be considered
RP = 0     # Room preference

OFF_5P = Room("Office 5P",N,RP)
Room_list.append(OFF_5P)

df = pd.read_excel('input_files/Room inputfiles/Office 5P/Office 5P.xlsx', sheet_name = 'WS_Break' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours ( 8:00 AM - 6:00 PM)
t3 = [960,1140]  # For Desk Lamp (4:00 PM - 7:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For laptop time and For duty cycles


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
OFF_5P_Lights = OFF_5P.Appliance(OFF_5P,nl,l_ap,ntf,l_ft_wd,v0,l_mt_wd, wd_we_type = 0, occasional_use = 1)
OFF_5P_Lights.windows(t1,t0,v0)

# Lights - Weekend
# OFF_5P_Lights = OFF_5P.Appliance(OFF_5P,nl,ap,2,tt_we,v0,mt_we, wd_we_type = 1)
# OFF_5P_Lights.windows(t1,t0,v0)


# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# 1. Computer
ncomp = df.loc['Computer','Number']
comp_ap = df.loc['Computer','AP (W)']
comp_sp = df.loc['Computer','SP (W)']
comp_apt_wd = df.loc['Computer','APT-WD (mins)']
comp_apt_we = df.loc['Computer','APT-WE (mins)']
comp_spt_wd = df.loc['Computer','SPT-WD (mins)']
comp_spt_we = df.loc['Computer','SPT-WE (mins)']
comp_ft_wd = df.loc['Computer','FT-WD (mins)']
comp_ft_we = df.loc['Computer','FT-WE (mins)']
comp_mt_wd = df.loc['Computer','MT-WD (mins)']
comp_mt_we = df.loc['Computer','MT-WE (mins)']

# Computer - Weekdays
OFF_5P_Comp = OFF_5P.Appliance(OFF_5P,ncomp,comp_ap,ntf,comp_ft_wd,v0,comp_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 1)
OFF_5P_Comp.windows(t1,t0,v0)
OFF_5P_Comp.specific_cycle_1(comp_ap,comp_apt_wd,comp_sp,comp_apt_wd,v1)
OFF_5P_Comp.cycle_behaviour(t1,t0)

# Computer - Weekend
# OFF_5P_Comp = OFF_5P.Appliance(OFF_5P,ncomp,comp_ap,ntf,comp_ft_we,v0,comp_mt_we, wd_we_type = 1, occasional_use = 0.6)
# OFF_5P_Comp.windows(t1,t0,v0)
# OFF_5P_Comp.specific_cycle_1(comp_ap,comp_apt_we,comp_sp,comp_spt_we,v1)
# OFF_5P_Comp.cycle_behaviour(t1,t0)


# 2. Monitor
nmon = df.loc['Monitor','Number']
mon_ap = df.loc['Monitor','AP (W)']
mon_sp = df.loc['Monitor','SP (W)']
mon_apt_wd = df.loc['Monitor','APT-WD (mins)']
mon_apt_we = df.loc['Monitor','APT-WE (mins)']
mon_spt_wd = df.loc['Monitor','SPT-WD (mins)']
mon_spt_we = df.loc['Monitor','SPT-WE (mins)']
mon_ft_wd = df.loc['Monitor','FT-WD (mins)']
mon_ft_we = df.loc['Monitor','FT-WE (mins)']
mon_mt_wd = df.loc['Monitor','MT-WD (mins)']
mon_mt_we = df.loc['Monitor','MT-WE (mins)']

# Monitor - Weekdays
OFF_5P_Moni = OFF_5P.Appliance(OFF_5P,nmon,mon_ap,ntf,mon_ft_wd,v0,mon_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 1)
OFF_5P_Moni.windows(t1,t0,v0)
OFF_5P_Moni.specific_cycle_1(mon_ap,mon_apt_wd,mon_sp,mon_spt_wd,v1)
OFF_5P_Moni.cycle_behaviour(t1,t0)

# Monitor - Weekend
# OFF_5P_Moni = OFF_5P.Appliance(OFF_5P,nmon,mon_ap,ntf,mon_ft_we,v0,mon_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.6)
# OFF_5P_Moni.windows(t1,t0,v0)
# OFF_5P_Moni.specific_cycle_1(mon_ap,mon_apt_we,mon_sp,mon_spt_we,v1)
# OFF_5P_Moni.cycle_behaviour(t1,t0)


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
OFF_5P_Lap = OFF_5P.Appliance(OFF_5P,nlap,lap_ap,ntf,lap_ft_wd,v0,lap_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 1)
OFF_5P_Lap.windows(t1,t0,v0)
OFF_5P_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
OFF_5P_Lap.cycle_behaviour(t1,t0)

# Laptop - Weekend
# OFF_5P_Lap = OFF_5P.Appliance(OFF_5P,nlap,lap_ap,ntf,lap_ft_we,v0,lap_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.6)
# OFF_5P_Lap.windows(t1,t0,v0)
# OFF_5P_Lap.specific_cycle_1(lap_ap,lap_apt_we,lap_sp,lap_spt_we,v1)
# OFF_5P_Lap.cycle_behaviour(t1,t0)


# 4. Mobile
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
OFF_5P_Mobile = OFF_5P.Appliance(OFF_5P,nmob,mob_ap,ntf,mob_ft_wd,v0,mob_mt_wd, wd_we_type = 0, occasional_use = 1)
OFF_5P_Mobile.windows(t1,t0,v0)

# Mobile - Weekend
# OFF_5P_Mobile = OFF_5P.Appliance(OFF_5P,nmob,mob_ap,ntf,mob_ft_we,v0,mob_mt_we, wd_we_type = 1, occasional_use = 0.6)
# OFF_5P_Mobile.windows(t1,t0,v0)


# 5. Lamp
nlmp = df.loc['Lamp','Number']
lmp_ap = df.loc['Lamp','AP (W)']
lmp_sp = df.loc['Lamp','SP (W)']
lmp_apt_wd = df.loc['Lamp','APT-WD (mins)']
lmp_apt_we = df.loc['Lamp','APT-WE (mins)']
lmp_spt_wd = df.loc['Lamp','SPT-WD (mins)']
lmp_spt_we = df.loc['Lamp','SPT-WE (mins)']
lmp_ft_wd = df.loc['Lamp','FT-WD (mins)']
lmp_ft_we = df.loc['Lamp','FT-WE (mins)']
lmp_mt_wd = df.loc['Lamp','MT-WD (mins)']
lmp_mt_we = df.loc['Lamp','MT-WE (mins)']

# Lamp - Weekdays
OFF_5P_Lamp = OFF_5P.Appliance(OFF_5P,nlmp,lmp_ap,ntf,lmp_ft_wd,v0,lmp_mt_wd, wd_we_type = 0, occasional_use = 0.4)
OFF_5P_Lamp.windows(t3,t0,v0)

# Lamp - Weekend
# OFF_5P_Lamp = OFF_5P.Appliance(OFF_5P,nlmp,lmp_ap,ntf,lmp_ft_we,v0,lmp_mt_we, wd_we_type = 1, occasional_use = 0.2)
# OFF_5P_Lamp.windows(t3,t0,v0)

