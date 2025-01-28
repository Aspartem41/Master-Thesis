# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:49:12 2024

@author: Romit
"""

"For Summer sem - Break"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100    # Total number of room to be considered
RP = 0     # Room preference

HKL = Room("Hike Lab",N,RP)
Room_list.append(HKL)

df = pd.read_excel('input_files/Room inputfiles/Hike Lab/Hike Lab.xlsx', sheet_name = 'SS_Break' , index_col=0)

# Timeframes
ntf = 2          # Number of timeframes used
t0 = [0,0]
t1 = [480,1080]  # Working hours (8:00 AM - 6:00 PM)
t2 = [0,1440]    # For Hydroponic (00:00 - 24:00)

# Variability factors
v0 = 0.1   # For timeframe
v1 = 0.2   # For laptop time and duty cycles


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
HKL_Lights = HKL.Appliance(HKL,nl,l_ap,ntf,l_ft_wd,v0,l_mt_wd, fixed = 'yes', wd_we_type = 0, occasional_use = 0.5)
HKL_Lights.windows(t1,t0,v0)

# Lights - Weekend
# HKL_Lights = HKL.Appliance(HKL,nl,l_ap,ntf,l_ft_we,v0,l_mt_we, fixed = 'yes', wd_we_type = 1)
# HKL_Lights.windows(t1,t0,v0)


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
HKL_Comp = HKL.Appliance(HKL,ncomp,comp_ap,ntf,comp_ft_wd,v0,comp_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 1)
HKL_Comp.windows(t1,t0,v0)
HKL_Comp.specific_cycle_1(comp_ap,comp_apt_wd,comp_sp,comp_spt_wd,v1)
HKL_Comp.cycle_behaviour(t1,t0)

# Computer - Weekend
# HKL_Comp = HKL.Appliance(HKL,ncomp,comp_ap,ntf,comp_ft_we,v0,comp_mt_we, wd_we_type = 1, occasional_use = 0.6)
# HKL_Comp.windows(t1,t0,v0)
# HKL_Comp.specific_cycle_1(comp_ap,comp_apt_we,comp_sp,comp_spt_we,v1)
# HKL_Comp.cycle_behaviour(t1,t0)


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
HKL_Moni = HKL.Appliance(HKL,nmon,mon_ap,ntf,mon_ft_wd,v0,mon_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 1)
HKL_Moni.windows(t1,t0,v0)
HKL_Moni.specific_cycle_1(mon_ap,mon_apt_wd,mon_sp,mon_spt_wd,v1)
HKL_Moni.cycle_behaviour(t1,t0)

# Monitor - Weekend
# HKL_Moni = HKL.Appliance(HKL,nmon,mon_ap,ntf,mon_ft_we,v0,mon_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.6)
# HKL_Moni.windows(t1,t0,v0)
# HKL_Moni.specific_cycle_1(mon_ap,mon_apt_we,mon_sp,mon_spt_we,v1)
# HKL_Moni.cycle_behaviour(t1,t0)


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
HKL_Lap = HKL.Appliance(HKL,nlap,lap_ap,ntf,lap_ft_wd,v1,lap_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.8)
HKL_Lap.windows(t1,t0,v0)
HKL_Lap.specific_cycle_1(lap_ap,lap_apt_wd,lap_sp,lap_spt_wd,v1)
HKL_Lap.cycle_behaviour(t1,t0)

# Laptop - Weekend
# HKL_Lap = HKL.Appliance(HKL,nlap,lap_ap,ntf,lap_ft_we,v1,lap_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.6)
# HKL_Lap.windows(t1,t0,v0)
# HKL_Lap.specific_cycle_1(lap_ap,lap_apt_we,lap_sp,lap_spt_we,v1)
# HKL_Lap.cycle_behaviour(t1,t0)


# 4. Printer
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
HKL_Printer = HKL.Appliance(HKL,nprt,prt_ap,ntf,prt_ft_wd,v0,prt_mt_wd, fixed_cycle = 1, wd_we_type = 0, occasional_use = 0.8)
HKL_Printer.windows(t1,t0,v0)
HKL_Printer.specific_cycle_1(prt_ap,prt_apt_wd,prt_sp,prt_spt_wd,v1)
HKL_Printer.cycle_behaviour(t1,t0)

# Printer - Weekend
# HKL_Printer = HKL.Appliance(HKL,nprt,prt_ap,ntf,prt_ft_we,v0,prt_mt_we, fixed_cycle = 1, wd_we_type = 1, occasional_use = 0.6)
# HKL_Printer.windows(t1,t0,v0)
# HKL_Printer.specific_cycle_4(prt_ap,prt_apt_we,prt_sp,prt_spt_we,v1)
# HKL_Printer.cycle_behaviour(t1,t0)


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
HKL_Mobile = HKL.Appliance(HKL,nmob,mob_ap,ntf,mob_ft_wd,v0,mob_mt_wd, wd_we_type = 0, occasional_use = 0.8)
HKL_Mobile.windows(t1,t0,v0)

# Mobile - Weekend
# HKL_Mobile = HKL.Appliance(HKL,nmob,mob_ap,ntf,mob_ft_we,v0,mob_mt_we, wd_we_type = 1, occasional_use = 0.6)
# HKL_Mobile.windows(t1,t0,v0)


# 6. Coffee_Maker
ncofm = df.loc['Coffee_Maker','Number']
cofm_ap = df.loc['Coffee_Maker','AP (W)']
cofm_sp = df.loc['Coffee_Maker','SP (W)']
cofm_apt_wd = df.loc['Coffee_Maker','APT-WD (mins)']
cofm_apt_we = df.loc['Coffee_Maker','APT-WE (mins)']
cofm_spt_wd = df.loc['Coffee_Maker','SPT-WD (mins)']
cofm_spt_we = df.loc['Coffee_Maker','SPT-WE (mins)']
cofm_ft_wd = df.loc['Coffee_Maker','FT-WD (mins)']
cofm_ft_we = df.loc['Coffee_Maker','FT-WE (mins)']
cofm_mt_wd = df.loc['Coffee_Maker','MT-WD (mins)']
cofm_mt_we = df.loc['Coffee_Maker','MT-WE (mins)']

# Coffee_Maker - Weekdays
HKL_Coffee_Maker = HKL.Appliance(HKL,ncofm,cofm_ap,ntf,cofm_ft_wd,v0,cofm_mt_wd, wd_we_type = 0, occasional_use = 0.8)
HKL_Coffee_Maker.windows(t1,t0,v0)

# Coffee_Maker - Weekend
# HKL_Coffee_Maker = HKL.Appliance(HKL,ncofm,cofm_ap,ntf,cofm_ft_we,v0,cofm_mt_we, wd_we_type = 1, occasional_use = 0.2)
# HKL_Coffee_Maker.windows(t3,t0,v0)


# 7. TV
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
HKL_TV = HKL.Appliance(HKL,ntv,tv_ap,ntf,tv_ft_wd,v0,tv_mt_wd, wd_we_type = 0, occasional_use = 0.4)
HKL_TV.windows(t1,t0,v0)

# TV - Weekend
# HKL_TV = HKL.Appliance(HKL,ntv,tv_ap,ntf,tv_ft_we,v0,tv_mt_we, wd_we_type = 1, occasional_use = 0.2)
# HKL_TV.windows(t1,t0,v0)


# 8. Hydroponic
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
HKL_Hydroponic = HKL.Appliance(HKL,nhydp,hydp_ap,ntf,hydp_ft_wd,v0,hydp_mt_wd, wd_we_type = 2, occasional_use = 0.8)
HKL_Hydroponic.windows(t2,t0,v0)
