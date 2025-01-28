# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:35:47 2024

@author: Romit
"""

"For Winter sem - Exam"

import pandas as pd
from ramp.core.core import Room, np
Room_list = []

N = 100   # Total number of room to be considered
RP = 0     # Room preference

KI4 = Room("Kitchen 4P",N,RP)
Room_list.append(KI4)

df = pd.read_excel('input_files/Room inputfiles/Kitchen 4P/Kitchen 4P.xlsx', sheet_name = 'WS_Exam' , index_col=0)

# Timeframes
ntf1 = 2         # Number of timeframes used
ntf2 = 4        
t0 = [0,0]
t1 = [300,480]    # 05:00 AM - 08:00 AM
t2 = [660,840]    # 11:00 AM - 02:00 PM
t3 = [960,1080]   # 04:00 PM - 06:00 PM
t4 = [1140,1320]  # 07:00 PM - 10:00 PM
t5 = [0,1440]     # The whole day for duty cycles

# Timeframes for Fridge duty cycles
trf1 = [480,1200]
trf2 = [300,479]
trf3 = [0,299]
trf4 = [1201,1440]


# Variability factors
v0 = 0.1   # For timeframe and different devices
v1 = 0.2   # Duty cycles
v2 = 0.4   # For lights
 
# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for light

nl = df.loc['Light','Number']                 # Number of the device
l_ap = df.loc['Light','AP (W)']               # Active power of the device 
l_sp = df.loc['Light','SP (W)']               # Stand-by power of the device
l_apt = df.loc['Light','APT (mins)']          # Active power specific cycle time 
l_spt1 = df.loc['Light','SPT1 (mins)']        # Stand-by power specific cycle 1 time 
l_spt2 = df.loc['Light','SPT2 (mins)']        # Stand-by power specific cycle 2 time 
l_spt3 = df.loc['Light','SPT3 (mins)']        # Stand-by power specific cycle 3 time 
l_ft1 = df.loc['Light','FT1 (mins)']          # Total function time 1 of the device 
l_ft2 = df.loc['Light','FT2 (mins)']          # Total function time 2 of the device
l_mt1 = df.loc['Light','MT1 (mins)']          # Minimum function time 1 of the device 
l_mt2 = df.loc['Light','MT2 (mins)']          # Minimum function time 2 of the device 

# Light - Alldays
KI4_Light = KI4.Appliance(KI4,nl,l_ap,ntf2,l_ft1,v2,l_mt1, fixed = 'yes', wd_we_type = 2, occasional_use = 0.85)
KI4_Light.windows(t1,t2,v0,t3,t4)



# ----------------------------------------------------------------------------------------------------------------------------------
# Parameters for plug loads


# 1. Stove
nstv = df.loc['Stove','Number']                 
stv_ap = df.loc['Stove','AP (W)']               
stv_sp = df.loc['Stove','SP (W)']              
stv_apt = df.loc['Stove','APT (mins)']         
stv_spt1 = df.loc['Stove','SPT1 (mins)']        
stv_spt2 = df.loc['Stove','SPT2 (mins)']        
stv_spt3 = df.loc['Stove','SPT3 (mins)']        
stv_ft1 = df.loc['Stove','FT1 (mins)']         
stv_ft2 = df.loc['Stove','FT2 (mins)']          
stv_mt1 = df.loc['Stove','MT1 (mins)']         
stv_mt2 = df.loc['Stove','MT2 (mins)']          

# Stove - Alldays
KI4_Stove = KI4.Appliance(KI4,nstv,stv_ap,ntf1,stv_ft2,v1,stv_mt2, fixed_cycle = 1, wd_we_type = 2, occasional_use = 0.5)
KI4_Stove.windows(t1,t0,v0)
KI4_Stove.specific_cycle_1(stv_ap,stv_spt1,stv_sp,stv_spt2,v1)
KI4_Stove.cycle_behaviour(t1,t0)

KI4_Stove = KI4.Appliance(KI4,nstv,stv_ap,ntf1,stv_ft1,v1,stv_mt1, fixed_cycle = 1, wd_we_type = 2, occasional_use = 0.85)
KI4_Stove.windows(t2,t0,v0)
KI4_Stove.specific_cycle_1(stv_ap,stv_apt,stv_sp,stv_spt3,v1)
KI4_Stove.cycle_behaviour(t2,t0)

KI4_Stove = KI4.Appliance(KI4,nstv,stv_ap,ntf1,stv_ft2,v1,stv_mt2, fixed_cycle = 1, wd_we_type = 2, occasional_use = 0.2)
KI4_Stove.windows(t3,t0,v0)
KI4_Stove.specific_cycle_1(stv_ap,stv_spt1,stv_sp,stv_spt2,v1)
KI4_Stove.cycle_behaviour(t3,t0)

KI4_Stove = KI4.Appliance(KI4,nstv,stv_ap,ntf1,stv_ft1,v1,stv_mt1, fixed_cycle = 1, wd_we_type = 2, occasional_use = 0.85)
KI4_Stove.windows(t4,t0,v0)
KI4_Stove.specific_cycle_1(stv_ap,stv_apt,stv_sp,stv_spt3,v1)
KI4_Stove.cycle_behaviour(t4,t0)


# 2. Fridge 
nrfg = df.loc['Fridge','Number']                 
rfg_ap = df.loc['Fridge','AP (W)']               
rfg_sp = df.loc['Fridge','SP (W)']              
rfg_apt = df.loc['Fridge','APT (mins)']         
rfg_spt1 = df.loc['Fridge','SPT1 (mins)']        
rfg_spt2 = df.loc['Fridge','SPT2 (mins)']        
rfg_spt3 = df.loc['Fridge','SPT3 (mins)']        
rfg_ft1 = df.loc['Fridge','FT1 (mins)']         
rfg_ft2 = df.loc['Fridge','FT2 (mins)']          
rfg_mt1 = df.loc['Fridge','MT1 (mins)']         
rfg_mt2 = df.loc['Fridge','MT2 (mins)']             

# Fridge - Alldays
KI4_Fridge = KI4.Appliance(KI4,nrfg,rfg_ap,ntf1,rfg_ft1,v1,rfg_mt1, fixed_cycle = 3, wd_we_type = 2, occasional_use = 1)
KI4_Fridge.windows(t5,t0,v0)
KI4_Fridge.specific_cycle_1(rfg_ap,rfg_spt3,rfg_sp,rfg_spt1)
KI4_Fridge.specific_cycle_2(rfg_ap,rfg_spt2,rfg_sp,rfg_spt2)
KI4_Fridge.specific_cycle_3(rfg_ap,rfg_spt1,rfg_sp,rfg_spt3)
KI4_Fridge.cycle_behaviour(trf1,t0,trf2,t0,trf3,trf4)


# 3. Microwave
nmicw = df.loc['Microwave','Number']                 
micw_ap = df.loc['Microwave','AP (W)']               
micw_sp = df.loc['Microwave','SP (W)']              
micw_apt = df.loc['Microwave','APT (mins)']         
micw_spt1 = df.loc['Microwave','SPT1 (mins)']        
micw_spt2 = df.loc['Microwave','SPT2 (mins)']        
micw_spt3 = df.loc['Microwave','SPT3 (mins)']        
micw_ft1 = df.loc['Microwave','FT1 (mins)']         
micw_ft2 = df.loc['Microwave','FT2 (mins)']          
micw_mt1 = df.loc['Microwave','MT1 (mins)']         
micw_mt2 = df.loc['Microwave','MT2 (mins)']          

# Microwave - Alldays
KI4_Microwave = KI4.Appliance(KI4,nmicw,micw_ap,ntf2,micw_ft1,v1,micw_mt1, wd_we_type = 2, occasional_use = 0.5)
KI4_Microwave.windows(t1,t2,v0,t3,t4)



# 4. Toaster
ntstr = df.loc['Toaster','Number']                 
tstr_ap = df.loc['Toaster','AP (W)']               
tstr_sp = df.loc['Toaster','SP (W)']              
tstr_apt = df.loc['Toaster','APT (mins)']         
tstr_spt1 = df.loc['Toaster','SPT1 (mins)']        
tstr_spt2 = df.loc['Toaster','SPT2 (mins)']        
tstr_spt3 = df.loc['Toaster','SPT3 (mins)']        
tstr_ft1 = df.loc['Toaster','FT1 (mins)']         
tstr_ft2 = df.loc['Toaster','FT2 (mins)']          
tstr_mt1 = df.loc['Toaster','MT1 (mins)']         
tstr_mt2 = df.loc['Toaster','MT2 (mins)']          

# Toaster - Alldays
KI4_Toaster = KI4.Appliance(KI4,ntstr,tstr_ap,ntf2,tstr_ft1,v1,tstr_mt1, wd_we_type = 2, occasional_use = 0.5)
KI4_Toaster.windows(t1,t2,v0,t3,t4)


# 5. Oven
novn = df.loc['Oven','Number']                 
ovn_ap = df.loc['Oven','AP (W)']               
ovn_sp = df.loc['Oven','SP (W)']              
ovn_apt = df.loc['Oven','APT (mins)']         
ovn_spt1 = df.loc['Oven','SPT1 (mins)']        
ovn_spt2 = df.loc['Oven','SPT2 (mins)']        
ovn_spt3 = df.loc['Oven','SPT3 (mins)']        
ovn_ft1 = df.loc['Oven','FT1 (mins)']         
ovn_ft2 = df.loc['Oven','FT2 (mins)']          
ovn_mt1 = df.loc['Oven','MT1 (mins)']         
ovn_mt2 = df.loc['Oven','MT2 (mins)']          

# Oven - Alldays
KI4_Oven = KI4.Appliance(KI4,novn,ovn_ap,ntf2,ovn_ft1,v1,ovn_mt1, wd_we_type = 2, occasional_use = 0.5)
KI4_Oven.windows(t1,t2,v0,t3,t4)


# 6. Mixer
nmxr = df.loc['Mixer','Number']                 
mxr_ap = df.loc['Mixer','AP (W)']               
mxr_sp = df.loc['Mixer','SP (W)']              
mxr_apt = df.loc['Mixer','APT (mins)']         
mxr_spt1 = df.loc['Mixer','SPT1 (mins)']        
mxr_spt2 = df.loc['Mixer','SPT2 (mins)']        
mxr_spt3 = df.loc['Mixer','SPT3 (mins)']        
mxr_ft1 = df.loc['Mixer','FT1 (mins)']         
mxr_ft2 = df.loc['Mixer','FT2 (mins)']          
mxr_mt1 = df.loc['Mixer','MT1 (mins)']         
mxr_mt2 = df.loc['Mixer','MT2 (mins)']          

# Mixer - Alldays
KI4_Mixer = KI4.Appliance(KI4,nmxr,mxr_ap,ntf2,mxr_ft1,v1,mxr_mt1, wd_we_type = 2, occasional_use = 0.5)
KI4_Mixer.windows(t1,t2,v0,t3,t4)
