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

ITLAB = Room("Computer Lab",N,RP)
Room_list.append(ITLAB)

df = pd.read_excel('input_files/Room inputfiles/Computer Lab/Computer Lab.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours (8:00 AM - 6:00 PM)

# Variability factors
# v0 = 0.1   # For timeframe
v1 = 0.2   # For eveything


# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for light

# nl = df.loc['Light','Number']                 # Number of the device
# l_ap = df.loc['Light','AP (W)']               # Active power of the device 
# l_sp = df.loc['Light','SP (W)']               # Stand-by power of the device
# l_apt_wd = df.loc['Light','APT-WD (mins)']    # Active power specific cycle time on weekdays 
# l_apt_we = df.loc['Light','APT-WE (mins)']    # Active power specific cycle time on weekend
# l_spt_wd = df.loc['Light','SPT-WD (mins)']    # Stand-by power specific cycle time on weekdays
# l_spt_we = df.loc['Light','SPT-WE (mins)']    # Stand-by power specific cycle time on weekend
# l_ft_wd = df.loc['Light','FT-WD (mins)']      # Total function time of the device on weekdays
# l_ft_we = df.loc['Light','FT-WE (mins)']      # Total function time of the device on weekend
# l_mt_wd = df.loc['Light','MT-WD (mins)']      # Minimum function time of the device on weekdays
# l_mt_we = df.loc['Light','MT-WE (mins)']      # Minimum function time of the device on weekend

# # Lights - Weekdays
# ITLAB_Lights = ITLAB.Appliance(ITLAB,nl,l_ap,ntf,l_ft_wd,v1,l_mt_wd, wd_we_type = 0, occasional_use = 0.6)
# ITLAB_Lights.windows(t1,t0,v1)

# Lights - Weekdays
# ITLAB_Lights = ITLAB.Appliance(ITLAB,nl,l_ap,ntf,l_ft_we,v1,l_mt_we, wd_we_type = 1, occasional_use = 0.2)
# ITLAB_Lights.windows(t1,t0,v1)



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
# ITLAB_projector = ITLAB.Appliance(ITLAB,nprj,prj_ap,ntf,prj_ft_wd,v1,prj_mt_wd, wd_we_type = 0, occasional_use = 0.4)
# ITLAB_projector.windows(t1,t0,v1)

# # Projector - Weekend
# ITLAB_projector = ITLAB.Appliance(ITLAB,nprj,prj_ap,ntf,prj_ft_we,v1,prj_mt_we, wd_we_type = 1, occasional_use = 0.2)
# ITLAB_projector.windows(t1,t0,v1)


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
# ITLAB_Comp = ITLAB.Appliance(ITLAB,ncomp,comp_ap,ntf,comp_ft_wd,v1,comp_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.4)
# ITLAB_Comp.windows(t1,t0,v1)
# ITLAB_Comp.specific_cycle_1(comp_ap,comp_apt_wd,comp_sp,comp_spt_wd,v1)
# ITLAB_Comp.cycle_behaviour(t1,t0)

# # Computer - Weekend
# ITLAB_Comp = ITLAB.Appliance(ITLAB,ncomp,comp_ap,ntf,comp_ft_we,v1,comp_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# ITLAB_Comp.windows(t1,t0,v1)
# ITLAB_Comp.specific_cycle_1(comp_ap,comp_apt_we,comp_sp,comp_spt_we,v1)
# ITLAB_Comp.cycle_behaviour(t1,t0)


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
# ITLAB_Moni = ITLAB.Appliance(ITLAB,nmon,mon_ap,ntf,mon_ft_wd,v1,mon_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.4)
# ITLAB_Moni.windows(t1,t0,v1)
# ITLAB_Moni.specific_cycle_1(mon_ap,mon_apt_wd,mon_sp,mon_spt_wd,v1)
# ITLAB_Moni.cycle_behaviour(t1,t0)

# # Monitor - Weekend
# ITLAB_Moni = ITLAB.Appliance(ITLAB,nmon,mon_ap,ntf,mon_ft_we,v1,mon_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# ITLAB_Moni.windows(t1,t0,v1)
# ITLAB_Moni.specific_cycle_1(mon_ap,mon_apt_we,mon_sp,mon_spt_we,v1)
# ITLAB_Moni.cycle_behaviour(t1,t0)


# 4. Laptop
# nlap = df.loc['Laptop','Number']
# lap_ap = df.loc['Laptop','AP (W)']
# lap_sp = df.loc['Laptop','SP (W)']
# lap_apt_wd = df.loc['Laptop','APT-WD (mins)']
# lap_apt_we = df.loc['Laptop','APT-WE (mins)']
# lap_spt_wd = df.loc['Laptop','SPT-WD (mins)']
# lap_spt_we = df.loc['Laptop','SPT-WE (mins)']
# lap_ft_wd = df.loc['Laptop','FT-WD (mins)']
# lap_ft_we = df.loc['Laptop','FT-WE (mins)']
# lap_mt_wd = df.loc['Laptop','MT-WD (mins)']
# lap_mt_we = df.loc['Laptop','MT-WE (mins)']

# # Laptop - Weekdays
# ITLAB_Lap = ITLAB.Appliance(ITLAB,nlap,lap_ap,ntf,lap_ft_wd,v1,lap_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.6)
# ITLAB_Lap.windows(t1,t0,v1)
# ITLAB_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
# ITLAB_Lap.cycle_behaviour(t1,t0)

# Laptop - Weekend
# ITLAB_Lap = ITLAB.Appliance(ITLAB,nlap,lap_ap,ntf,lap_ft_we,v1,lap_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.2)
# ITLAB_Lap.windows(t1,t0,v1)
# ITLAB_Lap.specific_cycle_1(lap_ap,lap_apt_we,lap_sp,lap_spt_we,v1)
# ITLAB_Lap.cycle_behaviour(t1,t0)


# 5. Mobile
# nmob = df.loc['Mobile','Number']
# mob_ap = df.loc['Mobile','AP (W)']
# mob_sp = df.loc['Mobile','SP (W)']
# mob_apt_wd = df.loc['Mobile','APT-WD (mins)']
# mob_apt_we = df.loc['Mobile','APT-WE (mins)']
# mob_spt_wd = df.loc['Mobile','SPT-WD (mins)']
# mob_spt_we = df.loc['Mobile','SPT-WE (mins)']
# mob_ft_wd = df.loc['Mobile','FT-WD (mins)']
# mob_ft_we = df.loc['Mobile','FT-WE (mins)']
# mob_mt_wd = df.loc['Mobile','MT-WD (mins)']
# mob_mt_we = df.loc['Mobile','MT-WE (mins)']

# # Mobile - Weekdays
# ITLAB_Mobile = ITLAB.Appliance(ITLAB,nmob,mob_ap,ntf,mob_ft_wd,v1,mob_mt_wd, wd_we_type = 0, occasional_use = 0.6)
# ITLAB_Mobile.windows(t1,t0,v1)

# Mobile - Weekend
# ITLAB_Mobile = ITLAB.Appliance(ITLAB,nmob,mob_ap,ntf,mob_ft_we,v1,mob_mt_we, wd_we_type = 1, occasional_use = 0.2)
# ITLAB_Mobile.windows(t1,t0,v1)
