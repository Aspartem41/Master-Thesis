# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:25:28 2023

@author: Romit
"""


from ramp.core.core import User, np
User_list = []


AE = User("Alleinerziehende",10,3)
User_list.append(AE)

# Windows for Lights and Charging/TV
t0 = [0,0]
t1 = [390,510]    # 6:30 - 8:30
t11 = [450,510]   # 7:30 - 8:30
t1_out = [0,510]  # 00:00 - 8:30
t2 = [1320,1440]  # 22:00 - 00:00
t22 = [1140,1440] # 19:00 - 00:00
CTF = [1080,1440] # 18:00 - 00:00
th = [0,60]       # 00:00 - 1:00 (One hour of late night next day for weekend)

# Windows for Coocking devices and Machines/TV
tc0 = [420,540]    # 7:00 - 9:00
tc1 = [540,660]    # 9:00 - 11:00
tc2 = [660,840]    # 11:00 - 14:00
tc3 = [840,1020]   # 14:00 - 17:00
tc4 = [1140,1260]  # 19:00 - 21:00
tm0 = [540,720]    # 9:00 - 12:00


# Variability factors
v1 = 0.1
v2 = 0.4           
v3 = 0.2
#%%'

#  AE Weekdays

AE_bulb_living = AE.Appliance(AE,1,10,1,60,v3,60, wd_we_type = 0)
AE_bulb_living.windows(t1,t0,v1)

AE_bulb_living = AE.Appliance(AE,1,10,1,210,v3,210, wd_we_type = 0)
AE_bulb_living.windows(t22,t0,0)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb_kitchen.windows(t1,t0,v1)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,120,v3,120, wd_we_type = 0)
AE_bulb_kitchen.windows(t22,t0,v1)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb1_bedroom.windows(t1,t0,v1)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb1_bedroom.windows(t2,t0,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,1,30,0.3,15, wd_we_type = 0)
AE_bulb_BT_hallway.windows(t1,t0,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,1,30,0.3,15, wd_we_type = 0)
AE_bulb_BT_hallway.windows(t22,t0,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,1,5,v3,5, wd_we_type = 0)   
AE_outdoor_bulb.windows(t1_out,t0,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,1,10,v3,10, wd_we_type = 0)   
AE_outdoor_bulb.windows(CTF,t0,0)

                                  ###


# AE_TV = AE.Appliance(AE,1,60,1,90,v1,90, wd_we_type = 0)
# AE_TV.windows(t22,t0,v1)

# AE_Phone_charger = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 0)
# AE_Phone_charger.windows(t1,t0,0)

# AE_Phone_charger = AE.Appliance(AE,2,5,1,15,v1,15, wd_we_type = 0)
# AE_Phone_charger.windows(t22,t0,v1)

# AE_Laptop_PC_charger = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
# AE_Laptop_PC_charger.windows(t1,t0,0)

# AE_Laptop_PC_charger = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
# AE_Laptop_PC_charger.windows(t22,t0,v1)

# AE_Herd = AE.Appliance(AE,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# AE_Herd.windows(tc0,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
# AE_Herd.cycle_behaviour(tc0,t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# AE_Herd.windows(tc2,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
# AE_Herd.cycle_behaviour(tc2,t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# AE_Herd.windows(tc3,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,0.15)
# AE_Herd.cycle_behaviour(tc3,t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# AE_Herd.windows(tc4,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
# AE_Herd.cycle_behaviour(tc4,t0)



# AE Weekends/Holidays


AE_bulb_living = AE.Appliance(AE,1,10,1,60,v3,60, wd_we_type = 1)
AE_bulb_living.windows(t11,t0,v1)

AE_bulb_living = AE.Appliance(AE,1,10,2,210,v3,210, wd_we_type = 1)
AE_bulb_living.windows(CTF,th,0)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb_kitchen.windows(t11,t0,v1)

AE_bulb_kitchen = AE.Appliance(AE,1,10,2,120,v3,120, wd_we_type = 1)
AE_bulb_kitchen.windows(t22,th,0)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb1_bedroom.windows(t11,t0,v1)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,2,30,v3,30, wd_we_type = 1)
AE_bulb1_bedroom.windows(t2,th,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,1,30,0.3,15, wd_we_type = 1)
AE_bulb_BT_hallway.windows(t11,t0,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,2,30,0.3,15, wd_we_type = 1)
AE_bulb_BT_hallway.windows(CTF,th,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,1,10,v3,10, wd_we_type = 1)   
AE_outdoor_bulb.windows(t1_out,t0,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,2,10,v3,10, wd_we_type = 1)  
AE_outdoor_bulb.windows(CTF,th,0)

                              ###

# AE_TV = AE.Appliance(AE,1,60,1,30,v2,30, wd_we_type = 1)
# AE_TV.windows(tm0,t0,v1)

# AE_TV = AE.Appliance(AE,1,60,1,30,v2,30, wd_we_type = 1)
# AE_TV.windows(tc3,t0,v1)

# AE_TV = AE.Appliance(AE,1,60,2,60,v2,60, wd_we_type = 1)
# AE_TV.windows(t22,th,0)

# AE_Phone_charger = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 1)
# AE_Phone_charger.windows(tm0,t0,v1)

# AE_Phone_charger = AE.Appliance(AE,2,5,2,15,v1,15, wd_we_type = 1)
# AE_Phone_charger.windows(t22,th,0)

# AE_Laptop_PC_charger = AE.Appliance(AE,1,50,1,30,v2,30, wd_we_type = 1)
# AE_Laptop_PC_charger.windows(tm0,t0,v1)

# AE_Laptop_PC_charger = AE.Appliance(AE,1,50,2,30,v2,30, wd_we_type = 1)
# AE_Laptop_PC_charger.windows(t22,th,0)

# AE_Herd = AE.Appliance(AE,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# AE_Herd.windows(tc1,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
# AE_Herd.cycle_behaviour(tc1,t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# AE_Herd.windows(tc2,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
# AE_Herd.cycle_behaviour(tc2,t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# AE_Herd.windows(tc3,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,0.15)
# AE_Herd.cycle_behaviour(tc3,t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# AE_Herd.windows(tc4,t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
# AE_Herd.cycle_behaviour(tc4,t0)


# # AE All time ON devices


# AE_router = AE.Appliance(AE,1,7,1,1440,0)
# AE_router.windows([0,1440],t0)

# AE_Kuehlschrank = AE.Appliance(AE,1,150,1,1440,0,30,'yes',3)
# AE_Kuehlschrank.windows([0,1440],t0)
# AE_Kuehlschrank.specific_cycle_1(150,20,5,10)
# AE_Kuehlschrank.specific_cycle_2(150,15,5,15)
# AE_Kuehlschrank.specific_cycle_3(150,10,5,20)
# AE_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# # AE Occasional_use devices



# AE_Toaster = AE.Appliance(AE,1,1000,2,10,0,10, occasional_use = 0.6, wd_we_type = 0)
# AE_Toaster.windows(tc0,tc4,v1)

# AE_Toaster = AE.Appliance(AE,1,1000,4,10,0,10, occasional_use = 0.6, wd_we_type = 1)
# AE_Toaster.windows(tc1,tc2,v1,tc3,tc4)

# AE_Haartrockner = AE.Appliance(AE,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
# AE_Haartrockner.windows([420,720],[960,1260],v1)

# AE_Haartrockner = AE.Appliance(AE,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
# AE_Haartrockner.windows(tm0,[960,1260],v1)

# AE_Luftfritteuse = AE.Appliance(AE,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
# AE_Luftfritteuse.windows(tc0,tc4,v1)

# AE_Luftfritteuse = AE.Appliance(AE,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
# AE_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

# AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
# AE_Spuelmaschine.windows([420,660],[1020,1320],v1)

# AE_Spuelmaschine = AE.Appliance(AE,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
# AE_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

# AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
# AE_Waschmaschine.windows(tc0,[1020,1260],v1)

# AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
# AE_Waschmaschine.windows(tm0,[1020,1260],v1)

# AE_Ofen = AE.Appliance(AE,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
# AE_Ofen.windows(tc0,tc4,v1)

# AE_Ofen = AE.Appliance(AE,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
# AE_Ofen.windows(tc1,tc2,v1,tc3,tc4)