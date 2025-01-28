# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:35:10 2024

@author: Romit
"""

"For Winter sem - Winter"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

DSR = Room("Design Room",N,RP)
Room_list.append(DSR)

df = pd.read_excel('input_files/Room inputfiles/Design Room/Design Room.xlsx', sheet_name = 'WS_Winter' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours (8:00 AM - 6:00 PM)


# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For every devices and duty cycles

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
DSR_Lights = DSR.Appliance(DSR,nl,l_ap,ntf,l_ft_wd,v1,l_mt_wd, fixed = 'yes', wd_we_type = 0, occasional_use = 0.4)
DSR_Lights.windows(t1,t0,v0)

# Lights - Weekend
# DSR_Lights = DSR.Appliance(DSR,nl,l_ap,ntf,l_ft_we,v1,l_mt_we, fixed = 'yes', wd_we_type = 1, occasional_use = 0.5)
# DSR_Lights.windows(t1,t0,v0)


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
DSR_comp = DSR.Appliance(DSR,ncomp,comp_ap,ntf,comp_ft_wd,v1,comp_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.4)
DSR_comp.windows(t1,t0,v0)
DSR_comp.specific_cycle_1(comp_ap,comp_apt_wd,comp_sp,comp_spt_wd,v1)
DSR_comp.cycle_behaviour(t1,t0)

# Computer - Weekend
# DSR_comp = DSR.Appliance(DSR,ncomp,p3d_ap,ntf,p3d_ft_we,v1,comp_mt_we, wd_we_type = 1, occasional_use = 0.6)
# DSR_comp.windows(t1,t0,v0)
# DSR_comp.specific_cycle_1(comp_ap,comp_apt_we,comp_sp,comp_spt_we,v1)
# DSR_comp.cycle_behaviour(t1,t0)


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
DSR_mon = DSR.Appliance(DSR,nmon,mon_ap,ntf,mon_ft_wd,v1,mon_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.4)
DSR_mon.windows(t1,t0,v0)
DSR_mon.specific_cycle_1(mon_ap,mon_apt_wd,mon_sp,mon_spt_wd,v1)
DSR_mon.cycle_behaviour(t1,t0)

# Monitor - Weekend
# DSR_mon = DSR.Appliance(DSR,nmon,mon_ap,ntf,mon_ft_we,v1,mon_mt_we, wd_we_type = 1, occasional_use = 0.6)
# DSR_mon.windows(t1,t0,v0)
# DSR_mon.specific_cycle_1(mon_ap,mon_apt_we,mon_sp,mon_spt_we,v1)
# DSR_mon.cycle_behaviour(t1,t0)


# 3. Printer
nprt = df.loc['Printer','Number']
prt_ap = df.loc['Printer','AP (W)']
prt_sp = df.loc['Printer','SP (W)']
prt_apt_wd = df.loc['Printer','APT-WD (mins)']
prt_apt_we = df.loc['Printer','APT-WE (mins)']
prt_spt_wd = df.loc['Printer','SPT-WD (mins)']
prt_spt_we = df.loc['Printer','SPT-WE (mins)']
prt_ft_wd = df.loc['Printer','FT-WD (mins)']
prt_ft_we = df.loc['Printer','FT-WE (mins)']
prt_mt_wd = df.loc['Printer','MT-WD (mins)']
prt_mt_we = df.loc['Printer','MT-WE (mins)']

# Printer - Weekdays
DSR_Printer = DSR.Appliance(DSR,nprt,prt_ap,ntf,prt_ft_wd,v1,prt_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.4)
DSR_Printer.windows(t1,t0,v0)
DSR_Printer.specific_cycle_1(prt_ap,prt_apt_wd,prt_sp,prt_spt_wd,v1)
DSR_Printer.cycle_behaviour(t1,t0)

# Printer - Weekend
# DSR_Printer = DSR.Appliance(DSR,nprt,prt_ap,ntf,prt_ft_we,v1,prt_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.6)
# DSR_Printer.windows(t1,t0,v0)
# DSR_Printer.specific_cycle_4(prt_ap,prt_apt_we,prt_sp,prt_spt_we,v1)
# DSR_Printer.cycle_behaviour(t1,t0)
