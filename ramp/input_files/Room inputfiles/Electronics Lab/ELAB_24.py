# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:19:26 2024

@author: Romit
"""

"For Summer sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 1   # Total number of room to be considered
RP = 0     # Room preference

ELAB = Room("Electronics Lab",N,RP)
Room_list.append(ELAB)

df = pd.read_excel('input_files/Room inputfiles/Electronics Lab/Electronics Lab.xlsx', sheet_name = 'SS_Exam' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [720,1080]  # Working hours (12:00 PM - 6:00 PM)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For Devices

# ----------------------------------------------------------------------------------------------------------------------------------
# 1. Electronics Lab of -- m^2
# ----------------------------------------------------------------------------------------------------------------------------------

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
# ELAB_Lights = ELAB.Appliance(ELAB,nl,l_ap,ntf,l_ft_wd,v1,l_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Lights.windows(t1,t0,v0)

# # Lights - Weekend
# # ELAB_Lights = ELAB.Appliance(ELAB,nl,l_ap,ntf,l_ft_we,v1,l_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Lights.windows(t1,t0,v0)



# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads

# # 1. Computer
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
# ELAB_Comp = ELAB.Appliance(ELAB,ncomp,comp_ap,ntf,comp_ft_wd,v1,comp_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Comp.windows(t1,t0,v0)

# # Computer - Weekend
# # ELAB_Comp = ELAB.Appliance(ELAB,ncomp,comp_ap,ntf,comp_ft_we,v1,comp_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Comp.windows(t1,t0,v0)



# # 2. Monitor
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
# ELAB_Moni = ELAB.Appliance(ELAB,nmon,mon_ap,ntf,mon_ft_wd,v1,mon_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Moni.windows(t1,t0,v0)

# # Monitor - Weekend
# # ELAB_Moni = ELAB.Appliance(ELAB,nmon,mon_ap,ntf,mon_ft_we,v1,mon_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Moni.windows(t1,t0,v0)


# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for other loads


# # 3. Basic Load
# nbl = df.loc['Basic','Number']
# bl_ap = df.loc['Basic','AP (W)']
# bl_sp = df.loc['Basic','SP (W)']
# bl_apt_wd = df.loc['Basic','APT-WD (mins)']
# bl_apt_we = df.loc['Basic','APT-WE (mins)']
# bl_spt_wd = df.loc['Basic','SPT-WD (mins)']
# bl_spt_we = df.loc['Basic','SPT-WE (mins)']
# bl_ft_wd = df.loc['Basic','FT-WD (mins)']
# bl_ft_we = df.loc['Basic','FT-WE (mins)']
# bl_mt_wd = df.loc['Basic','MT-WD (mins)']
# bl_mt_we = df.loc['Basic','MT-WE (mins)']

# # Basic Load - Weekdays
# ELAB_Basic = ELAB.Appliance(ELAB,nbl,bl_ap,ntf,bl_ft_wd,v1,bl_mt_wd, wd_we_type = 0, occasional_use = 0.4)
# ELAB_Basic.windows(t1,t0,v0)

# # Basic Load - Weekend
# # ELAB_Basic = ELAB.Appliance(ELAB,nbl,bl_ap,ntf,bl_ft_we,v1,bl_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Basic.windows(t1,t0,v0)


# # 4. Experiment_1
# nex1 = df.loc['Experiment_1','Number']
# ex1_ap = df.loc['Experiment_1','AP (W)']
# ex1_sp = df.loc['Experiment_1','SP (W)']
# ex1_apt_wd = df.loc['Experiment_1','APT-WD (mins)']
# ex1_apt_we = df.loc['Experiment_1','APT-WE (mins)']
# ex1_spt_wd = df.loc['Experiment_1','SPT-WD (mins)']
# ex1_spt_we = df.loc['Experiment_1','SPT-WE (mins)']
# ex1_ft_wd = df.loc['Experiment_1','FT-WD (mins)']
# ex1_ft_we = df.loc['Experiment_1','FT-WE (mins)']
# ex1_mt_wd = df.loc['Experiment_1','MT-WD (mins)']
# ex1_mt_we = df.loc['Experiment_1','MT-WE (mins)']

# # Experiment_1 - Weekdays
# ELAB_Experiment_1 = ELAB.Appliance(ELAB,nex1,ex1_ap,ntf,ex1_ft_wd,v1,ex1_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Experiment_1.windows(t1,t0,v0)

# # Experiment_1 - Weekend
# # ELAB_Experiment_1 = ELAB.Appliance(ELAB,nex1,ex1_ap,ntf,ex1_ft_we,v1,ex1_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Experiment_1.windows(t1,t0,v0)


# # 5. Experiment_2
# nex2 = df.loc['Experiment_2','Number']
# ex2_ap = df.loc['Experiment_2','AP (W)']
# ex2_sp = df.loc['Experiment_2','SP (W)']
# ex2_apt_wd = df.loc['Experiment_2','APT-WD (mins)']
# ex2_apt_we = df.loc['Experiment_2','APT-WE (mins)']
# ex2_spt_wd = df.loc['Experiment_2','SPT-WD (mins)']
# ex2_spt_we = df.loc['Experiment_2','SPT-WE (mins)']
# ex2_ft_wd = df.loc['Experiment_2','FT-WD (mins)']
# ex2_ft_we = df.loc['Experiment_2','FT-WE (mins)']
# ex2_mt_wd = df.loc['Experiment_2','MT-WD (mins)']
# ex2_mt_we = df.loc['Experiment_2','MT-WE (mins)']

# # Experiment_2 - Weekdays
# ELAB_Experiment_2 = ELAB.Appliance(ELAB,nex2,ex2_ap,ntf,ex2_ft_wd,v1,ex2_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Experiment_2.windows(t1,t0,v0)

# # Experiment_2 - Weekend
# # ELAB_Experiment_2 = ELAB.Appliance(ELAB,nex2,ex2_ap,ntf,ex2_ft_we,v1,ex2_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Experiment_2.windows(t1,t0,v0)


# # 6. Experiment_3
# nex3 = df.loc['Experiment_3','Number']
# ex3_ap = df.loc['Experiment_3','AP (W)']
# ex3_sp = df.loc['Experiment_3','SP (W)']
# ex3_apt_wd = df.loc['Experiment_3','APT-WD (mins)']
# ex3_apt_we = df.loc['Experiment_3','APT-WE (mins)']
# ex3_spt_wd = df.loc['Experiment_3','SPT-WD (mins)']
# ex3_spt_we = df.loc['Experiment_3','SPT-WE (mins)']
# ex3_ft_wd = df.loc['Experiment_3','FT-WD (mins)']
# ex3_ft_we = df.loc['Experiment_3','FT-WE (mins)']
# ex3_mt_wd = df.loc['Experiment_3','MT-WD (mins)']
# ex3_mt_we = df.loc['Experiment_3','MT-WE (mins)']

# # Experiment_3 - Weekdays
# ELAB_Experiment_3 = ELAB.Appliance(ELAB,nex3,ex3_ap,ntf,ex3_ft_wd,v1,ex3_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Experiment_3.windows(t1,t0,v0)

# # Experiment_3 - Weekend
# # ELAB_Experiment_3 = ELAB.Appliance(ELAB,nex3,ex3_ap,ntf,ex3_ft_we,v1,ex3_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Experiment_3.windows(t1,t0,v0)


# # 7. Project
# npro = df.loc['Project','Number']
# pro_ap = df.loc['Project','AP (W)']
# pro_sp = df.loc['Project','SP (W)']
# pro_apt_wd = df.loc['Project','APT-WD (mins)']
# pro_apt_we = df.loc['Project','APT-WE (mins)']
# pro_spt_wd = df.loc['Project','SPT-WD (mins)']
# pro_spt_we = df.loc['Project','SPT-WE (mins)']
# pro_ft_wd = df.loc['Project','FT-WD (mins)']
# pro_ft_we = df.loc['Project','FT-WE (mins)']
# pro_mt_wd = df.loc['Project','MT-WD (mins)']
# pro_mt_we = df.loc['Project','MT-WE (mins)']

# # Project - Weekdays
# ELAB_Project = ELAB.Appliance(ELAB,npro,pro_ap,ntf,pro_ft_wd,v1,pro_mt_wd, wd_we_type = 0, occasional_use = 0.2)
# ELAB_Project.windows(t1,t0,v0)

# # Project - Weekend
# # ELAB_Project = ELAB.Appliance(ELAB,npro,pro_ap,ntf,pro_ft_we,v1,pro_mt_we, wd_we_type = 1, occasional_use = 0.2)
# # ELAB_Project.windows(t1,t0,v0)