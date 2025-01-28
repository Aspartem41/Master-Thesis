# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:19:26 2024

@author: Romit
"""

"For Summer sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

MLH = Room("Medium Lecture Hall",N,RP)
Room_list.append(MLH)

df = pd.read_excel('input_files/Room inputfiles/Medium Lecture Hall/Medium Lecture Hall.xlsx', sheet_name = 'SS_Exam' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours ( 8:00 AM - 6:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For laptop time and For duty cycles

# ----------------------------------------------------------------------------------------------------------------------------------
# 1. Medium Lecture Hall of -- m^2
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
MLH_Lights = MLH.Appliance(MLH,nl,l_ap,ntf,l_ft_wd,v0,l_mt_wd, wd_we_type = 0, occasional_use = 0.6)
MLH_Lights.windows(t1,t0,v0)

#LIghts - Weekend
# MLH_Lights = MLH.Appliance(MLH,nl,l_ap,ntf,l_ft_we,v0,l_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MLH_Lights.windows(t1,t0,v0)



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
# MLH_projector = MLH.Appliance(MLH,nprj,prj_ap,ntf,prj_ft_wd,v0,prj_mt_wd, wd_we_type = 0, occasional_use = 0.4)
# MLH_projector.windows(t1,t0,v0)

# # Projector - Weekend
# MLH_projector = MLH.Appliance(MLH,nprj,prj_ap,ntf,prj_ft_we,v0,prj_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MLH_projector.windows(t1,t0,v0)


# # 2. Computer
# ncomp = df.loc['Computer','Number']
# comp_ap = df.loc['Computer','AP (W)']
# comp_sp = df.loc['Computer','SP (W)']
# comp_apt_wd = df.loc['Computer','APT-WD (mins)']
# comp_apt_we = df.loc['Computer','APT-WE (mins)']
# comp_spt_wd = df.loc['Computer','SPT-WD (mins)']
# comp_spt_we = df.loc['Computer','SPT-WE (mins)']
# comp_ft_wd = df.loc['Computer','FT-WD (mins)']
# comp_ft_we = df.loc['Computer','FT-WE (mins)']
# comp_mt_wd = df.loc['Computer','MT-WD (mins)']
# comp_mt_we = df.loc['Computer','MT-WE (mins)']

# # Computer - Weekdays
# MLH_Comp = MLH.Appliance(MLH,ncomp,comp_ap,ntf,comp_ft_wd,v0,comp_mt_wd, wd_we_type = 0, occasional_use = 0.4)
# MLH_Comp.windows(t1,t0,v0)
# MLH_Comp.specific_cycle_1(comp_ap,comp_apt_wd,comp_sp,comp_spt_wd,v1)
# MLH_Comp.cycle_behaviour(t1,t0)

# # Computer - Weekend
# MLH_Comp = MLH.Appliance(MLH,ncomp,comp_ap,ntf,comp_ft_we,v0,comp_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MLH_Comp.windows(t1,t0,v0)
# MLH_Comp.specific_cycle_1(comp_ap,comp_apt_we,comp_sp,comp_spt_we,v1)
# MLH_Comp.cycle_behaviour(t1,t0)


# # 3. Monitor
# nmon = df.loc['Monitor','Number']
# mon_ap = df.loc['Monitor','AP (W)']
# mon_sp = df.loc['Monitor','SP (W)']
# mon_apt_wd = df.loc['Monitor','APT-WD (mins)']
# mon_apt_we = df.loc['Monitor','APT-WE (mins)']
# mon_spt_wd = df.loc['Monitor','SPT-WD (mins)']
# mon_spt_we = df.loc['Monitor','SPT-WE (mins)']
# mon_ft_wd = df.loc['Monitor','FT-WD (mins)']
# mon_ft_we = df.loc['Monitor','FT-WE (mins)']
# mon_mt_wd = df.loc['Monitor','MT-WD (mins)']
# mon_mt_we = df.loc['Monitor','MT-WE (mins)']

# # Monitor - Weekdays
# MLH_Moni = MLH.Appliance(MLH,nmon,mon_ap,ntf,mon_ft_wd,v0,mon_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.4)
# MLH_Moni.windows(t1,t0,v0)
# MLH_Moni.specific_cycle_1(mon_ap,mon_apt_wd,mon_sp,mon_spt_wd,v1)
# MLH_Moni.cycle_behaviour(t1,t0)

# # Monitor - Weekend
# MLH_Moni = MLH.Appliance(MLH,nmon,mon_ap,ntf,mon_ft_we,v0,mon_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# MLH_Moni.windows(t1,t0,v0)
# MLH_Moni.specific_cycle_1(mon_ap,mon_apt_we,mon_sp,mon_spt_we,v1)
# MLH_Moni.cycle_behaviour(t1,t0)


# 4. Laptop
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
MLH_Lap = MLH.Appliance(MLH,nlap,lap_ap,ntf,lap_ft_wd,v0,lap_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.6)
MLH_Lap.windows(t1,t0,v0)
MLH_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
MLH_Lap.cycle_behaviour(t1,t0)

# Laptop - Weekend
# MLH_Lap = MLH.Appliance(MLH,nlap,lap_ap,ntf,lap_ft_we,v0,lap_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# MLH_Lap.windows(t1,t0,v0)
# MLH_Lap.specific_cycle_1(lap_ap,lap_apt_we,lap_sp,lap_spt_we,v1)
# MLH_Lap.cycle_behaviour(t1,t0)


# 5. Mobile
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
MLH_Mobile = MLH.Appliance(MLH,nmob,mob_ap,ntf,mob_ft_wd,v0,mob_mt_wd, wd_we_type = 0, occasional_use = 0.6)
MLH_Mobile.windows(t1,t0,v0)

# Mobile - Weekend
# MLH_Mobile = MLH.Appliance(MLH,nmob,mob_ap,ntf,mob_ft_we,v0,mob_mt_we, wd_we_type = 1, occasional_use = 0.2)
# MLH_Mobile.windows(t1,t0,v0)
