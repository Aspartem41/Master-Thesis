# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:46:53 2023

@author: Romit
"""

from ramp.core.core import User, np
User_list = []

EP = User("Einpersonen",10,3)
User_list.append(EP)

AE = User("Alleinerziehende",10,3)
User_list.append(AE)

POK = User("Paar Ohne Kind",10,3)
User_list.append(POK)

PMK = User("Paar Mit Kind",10,3)
User_list.append(PMK)

MP = User("Mehrpersonen",10,3)
User_list.append(MP)
 
# Windows for Lights and Charging/TV
t0 = [0,0]
t10 = [390,510]   # 6:30 - 8:30
t1 = [390,570]    # 6:30 - 9:30
t11 = [450,570]   # 7:30 - 9:30
t_out = [0,510]   # 00:00 - 8:30
t2 = [1320,1440]  # 22:00 - 00:00
t22 = [1140,1440] # 19:00 - 00:00
t3 = [960,1140]   # 16:00 - 19:00
CTF = [960,1440]  # 16:00 - 00:00
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
v3 = 0.3
#%%

# EP Weekdays

EP_bulb_living = EP.Appliance(EP,1,10,1,120,v3,120, wd_we_type = 0)
EP_bulb_living.windows(t1,t0,v1)

EP_bulb_living = EP.Appliance(EP,1,10,1,240,v3,240, wd_we_type = 0)
EP_bulb_living.windows(t22,t0,0)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,60,v3,60, wd_we_type = 0)
EP_bulb_kitchen.windows(t1,t0,v1)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,120,v3,120, wd_we_type = 0)
EP_bulb_kitchen.windows(t22,t0,v1)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 0)
EP_bulb1_bedroom.windows(t1,t0,v1)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 0)
EP_bulb1_bedroom.windows(t2,t0,v1)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,1,30,v3,15, wd_we_type = 0)
EP_bulb_BT_hallway.windows(t1,t0,v1)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,1,30,v3,15, wd_we_type = 0)
EP_bulb_BT_hallway.windows(t22,t0,0)

EP_outdoor_bulb = EP.Appliance(EP,1,13,1,10,v3,10, wd_we_type = 0)  
EP_outdoor_bulb.windows(t_out,t0,0)

EP_outdoor_bulb = EP.Appliance(EP,1,13,1,10,v3,10, wd_we_type = 0)   
EP_outdoor_bulb.windows(CTF,t0,0)

                        ###


EP_TV = EP.Appliance(EP,1,60,1,90,v1,90, wd_we_type = 0)
EP_TV.windows(t22,t0,v1)

EP_Phone_charger = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 0)
EP_Phone_charger.windows(t10,t0,0)

EP_Phone_charger = EP.Appliance(EP,1,5,1,15,v1,15, wd_we_type = 0)
EP_Phone_charger.windows(t22,t0,v1)

EP_Laptop_PC_charger = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
EP_Laptop_PC_charger.windows(t10,t0,0)

EP_Laptop_PC_charger = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
EP_Laptop_PC_charger.windows(t22,t0,v1)

EP_Herd = EP.Appliance(EP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
EP_Herd.windows(tc0,t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
EP_Herd.cycle_behaviour(tc0,t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
EP_Herd.windows(tc2,t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour(tc2,t0)

EP_Herd = EP.Appliance(EP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
EP_Herd.windows(tc3,t0,v1)
EP_Herd.specific_cycle_1(1800,10,0.15)
EP_Herd.cycle_behaviour(tc3,t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
EP_Herd.windows(tc4,t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour(tc4,t0)


# EP Weekends/Holidays


EP_bulb_living = EP.Appliance(EP,1,10,1,60,v3,60, wd_we_type = 1)
EP_bulb_living.windows(t11,t0,v1)

EP_bulb_living = EP.Appliance(EP,1,10,2,300,v3,300, wd_we_type = 1)
EP_bulb_living.windows(CTF,th,0)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 1)
EP_bulb_kitchen.windows(t11,t0,v1)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 1)
EP_bulb_kitchen.windows(t3,t0,v1)

EP_bulb_kitchen = EP.Appliance(EP,1,10,2,120,v3,120, wd_we_type = 1)
EP_bulb_kitchen.windows(t22,th,0)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 1)
EP_bulb1_bedroom.windows(t11,t0,0)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,2,30,v3,30, wd_we_type = 1)
EP_bulb1_bedroom.windows(t2,th,0)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,1,30,v3,15, wd_we_type = 1)
EP_bulb_BT_hallway.windows(t11,t0,v1)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,2,30,v3,15, wd_we_type = 1)
EP_bulb_BT_hallway.windows(CTF,th,0)

EP_outdoor_bulb = EP.Appliance(EP,1,13,1,10,v3,10, wd_we_type = 1)   
EP_outdoor_bulb.windows(t_out,t0,0)

EP_outdoor_bulb = EP.Appliance(EP,1,13,2,10,v3,10, wd_we_type = 1)  
EP_outdoor_bulb.windows(CTF,th,0)

                                ###


EP_TV = EP.Appliance(EP,1,60,1,60,v2,60, wd_we_type = 1)
EP_TV.windows(tc3,t0,v1)

EP_TV = EP.Appliance(EP,1,60,2,60,v2,60, wd_we_type = 1)
EP_TV.windows(t22,th,0)

EP_Phone_charger = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 1)
EP_Phone_charger.windows(tm0,t0,v1)

EP_Phone_charger = EP.Appliance(EP,1,5,2,15,v1,15, wd_we_type = 1)
EP_Phone_charger.windows(t22,th,0)

EP_Laptop_PC_charger = EP.Appliance(EP,1,50,1,30,v2,30, wd_we_type = 1)
EP_Laptop_PC_charger.windows(tm0,t0,v2)

EP_Laptop_PC_charger = EP.Appliance(EP,1,50,2,30,v2,30, wd_we_type = 1)
EP_Laptop_PC_charger.windows(t22,th,0)

EP_Herd = EP.Appliance(EP,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows(tc1,t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
EP_Herd.cycle_behaviour(tc1,t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows(tc2,t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour(tc2,t0)

EP_Herd = EP.Appliance(EP,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows(tc3,t0,v1)
EP_Herd.specific_cycle_1(1800,10,0.15)
EP_Herd.cycle_behaviour(tc3,t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows(tc4,t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour(tc4,t0)


# EP All time ON devices


EP_router = EP.Appliance(EP,1,7,1,1440,0)
EP_router.windows([0,1440],t0)

EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3)
EP_Kuehlschrank.windows([0,1440],t0)
EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
EP_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])



# EP Occasional_use devices



EP_Toaster = EP.Appliance(EP,1,1000,2,10,0,10, occasional_use = 0.5, wd_we_type = 0)
EP_Toaster.windows(tc0,tc4,v1)

EP_Toaster = EP.Appliance(EP,1,1000,4,10,0,10, occasional_use = 0.5, wd_we_type = 1)
EP_Toaster.windows(tc1,tc2,v1,tc3,tc4)

EP_Haartrockner = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5, wd_we_type = 0)
EP_Haartrockner.windows([420,720],[960,1260],v1)

EP_Haartrockner = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5, wd_we_type = 1)
EP_Haartrockner.windows(tm0,[960,1260],v1)

EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
EP_Luftfritteuse.windows(tc0,tc4,v1)

EP_Luftfritteuse = EP.Appliance(EP,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
EP_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
EP_Spuelmaschine.windows([420,660],[1020,1320],v1)

EP_Spuelmaschine = EP.Appliance(EP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
EP_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
EP_Waschmaschine.windows(tc0,[1020,1260],v1)

EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
EP_Waschmaschine.windows(tm0,[1020,1260],v1)

EP_Ofen = EP.Appliance(EP,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
EP_Ofen.windows(tc0,tc4,v1)

EP_Ofen = EP.Appliance(EP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
EP_Ofen.windows(tc1,tc2,v1,tc3,tc4)



#%%


# AE Weekdays

AE_bulb_living = AE.Appliance(AE,1,10,1,120,v3,120, wd_we_type = 0)
AE_bulb_living.windows(t1,t0,v1)

AE_bulb_living = AE.Appliance(AE,1,10,1,240,v3,240, wd_we_type = 0)
AE_bulb_living.windows(t22,t0,0)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,60,v3,60, wd_we_type = 0)
AE_bulb_kitchen.windows(t1,t0,v1)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,120,v3,120, wd_we_type = 0)
AE_bulb_kitchen.windows(t22,t0,v1)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb1_bedroom.windows(t1,t0,v1)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb1_bedroom.windows(t2,t0,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,1,30,v3,15, wd_we_type = 0)
AE_bulb_BT_hallway.windows(t1,t0,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,1,30,v3,15, wd_we_type = 0)
AE_bulb_BT_hallway.windows(t22,t0,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,1,10,v3,10, wd_we_type = 0)  
AE_outdoor_bulb.windows(t_out,t0,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,1,10,v3,10, wd_we_type = 0)   
AE_outdoor_bulb.windows(CTF,t0,0)

                        ###


AE_TV = AE.Appliance(AE,1,60,1,90,v1,90, wd_we_type = 0)
AE_TV.windows(t22,t0,v1)

AE_Phone_charger = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 0)
AE_Phone_charger.windows(t10,t0,0)

AE_Phone_charger = AE.Appliance(AE,2,5,1,15,v1,15, wd_we_type = 0)
AE_Phone_charger.windows(t22,t0,v1)

AE_Laptop_PC_charger = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
AE_Laptop_PC_charger.windows(t10,t0,0)

AE_Laptop_PC_charger = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
AE_Laptop_PC_charger.windows(t22,t0,v1)

AE_Herd = AE.Appliance(AE,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
AE_Herd.windows(tc0,t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
AE_Herd.cycle_behaviour(tc0,t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
AE_Herd.windows(tc2,t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour(tc2,t0)

AE_Herd = AE.Appliance(AE,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
AE_Herd.windows(tc3,t0,v1)
AE_Herd.specific_cycle_1(1800,10,0.15)
AE_Herd.cycle_behaviour(tc3,t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
AE_Herd.windows(tc4,t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour(tc4,t0)


# AE Weekends/Holidays


AE_bulb_living = AE.Appliance(AE,1,10,1,60,v3,60, wd_we_type = 1)
AE_bulb_living.windows(t11,t0,v1)

AE_bulb_living = AE.Appliance(AE,1,10,2,300,v3,300, wd_we_type = 1)
AE_bulb_living.windows(CTF,th,0)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb_kitchen.windows(t11,t0,v1)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb_kitchen.windows(t3,t0,v1)

AE_bulb_kitchen = AE.Appliance(AE,1,10,1,120,v3,120, wd_we_type = 1)
AE_bulb_kitchen.windows(t22,t0,0)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb1_bedroom.windows(t11,t0,v1)

AE_bulb1_bedroom = AE.Appliance(AE,1,10,2,30,v3,30, wd_we_type = 1)
AE_bulb1_bedroom.windows(t2,th,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,1,30,v3,15, wd_we_type = 1)
AE_bulb_BT_hallway.windows(t11,t0,v1)

AE_bulb_BT_hallway = AE.Appliance(AE,1,10,2,30,v3,15, wd_we_type = 1)
AE_bulb_BT_hallway.windows(CTF,th,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,1,10,v3,10, wd_we_type = 1)   
AE_outdoor_bulb.windows(t_out,t0,0)

AE_outdoor_bulb = AE.Appliance(AE,1,13,2,10,v3,10, wd_we_type = 1)  
AE_outdoor_bulb.windows(CTF,th,0)

                                ###

AE_TV = AE.Appliance(AE,1,60,1,30,v2,30, wd_we_type = 1)
AE_TV.windows(tm0,t0,v1)

AE_TV = AE.Appliance(AE,1,60,1,30,v2,30, wd_we_type = 1)
AE_TV.windows(tc3,t0,v1)

AE_TV = AE.Appliance(AE,1,60,2,60,v2,60, wd_we_type = 1)
AE_TV.windows(t22,th,0)

AE_Phone_charger = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 1)
AE_Phone_charger.windows(tm0,t0,v1)

AE_Phone_charger = AE.Appliance(AE,2,5,2,15,v1,15, wd_we_type = 1)
AE_Phone_charger.windows(t22,th,0)

AE_Laptop_PC_charger = AE.Appliance(AE,1,50,1,30,v2,30, wd_we_type = 1)
AE_Laptop_PC_charger.windows(tm0,t0,v1)

AE_Laptop_PC_charger = AE.Appliance(AE,1,50,2,30,v2,30, wd_we_type = 1)
AE_Laptop_PC_charger.windows(t22,th,0)

AE_Herd = AE.Appliance(AE,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows(tc1,t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
AE_Herd.cycle_behaviour(tc1,t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows(tc2,t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour(tc2,t0)

AE_Herd = AE.Appliance(AE,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows(tc3,t0,v1)
AE_Herd.specific_cycle_1(1800,10,0.15)
AE_Herd.cycle_behaviour(tc3,t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows(tc4,t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour(tc4,t0)


# AE All time ON devices


AE_router = AE.Appliance(AE,1,7,1,1440,0)
AE_router.windows([0,1440],t0)

AE_Kuehlschrank = AE.Appliance(AE,1,150,1,1440,0,30,'yes',3)
AE_Kuehlschrank.windows([0,1440],t0)
AE_Kuehlschrank.specific_cycle_1(150,20,5,10)
AE_Kuehlschrank.specific_cycle_2(150,15,5,15)
AE_Kuehlschrank.specific_cycle_3(150,10,5,20)
AE_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])



# AE Occasional_use devices



AE_Toaster = AE.Appliance(AE,1,1000,2,10,0,10, occasional_use = 0.6, wd_we_type = 0)
AE_Toaster.windows(tc0,tc4,v1)

AE_Toaster = AE.Appliance(AE,1,1000,4,10,0,10, occasional_use = 0.6, wd_we_type = 1)
AE_Toaster.windows(tc1,tc2,v1,tc3,tc4)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
AE_Haartrockner.windows([420,720],[960,1260],v1)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
AE_Haartrockner.windows(tm0,[960,1260],v1)

AE_Luftfritteuse = AE.Appliance(AE,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
AE_Luftfritteuse.windows(tc0,tc4,v1)

AE_Luftfritteuse = AE.Appliance(AE,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
AE_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
AE_Spuelmaschine.windows([420,660],[1020,1320],v1)

AE_Spuelmaschine = AE.Appliance(AE,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
AE_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
AE_Waschmaschine.windows(tc0,[1020,1260],v1)

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
AE_Waschmaschine.windows(tm0,[1020,1260],v1)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
AE_Ofen.windows(tc0,tc4,v1)

AE_Ofen = AE.Appliance(AE,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
AE_Ofen.windows(tc1,tc2,v1,tc3,tc4)



#%%


# POK Weekdays

POK_bulb_living = POK.Appliance(POK,2,10,1,120,v3,120, wd_we_type = 0)
POK_bulb_living.windows(t1,t0,v1)

POK_bulb_living = POK.Appliance(POK,2,10,1,240,v3,240, wd_we_type = 0)
POK_bulb_living.windows(t22,t0,0)

POK_bulb_kitchen = POK.Appliance(POK,1,10,1,60,v3,60, wd_we_type = 0)
POK_bulb_kitchen.windows(t1,t0,v1)

POK_bulb_kitchen = POK.Appliance(POK,1,10,1,120,v3,120, wd_we_type = 0)
POK_bulb_kitchen.windows(t22,t0,v1)

POK_bulb1_bedroom = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 0)
POK_bulb1_bedroom.windows(t1,t0,v1)

POK_bulb1_bedroom = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 0)
POK_bulb1_bedroom.windows(t2,t0,v1)

POK_bulb2_bedroom = POK.Appliance(POK,1,10,1,15,v3,15, wd_we_type = 0)
POK_bulb2_bedroom.windows(t1,t0,v1)

POK_bulb2_bedroom = POK.Appliance(POK,1,10,1,15,v3,15, wd_we_type = 0)
POK_bulb2_bedroom.windows([1140,1320],t0,v1)

POK_bulb_BT_hallway = POK.Appliance(POK,2,10,1,30,v3,15, wd_we_type = 0)
POK_bulb_BT_hallway.windows(t1,t0,v1)

POK_bulb_BT_hallway = POK.Appliance(POK,2,10,1,30,v3,15, wd_we_type = 0)
POK_bulb_BT_hallway.windows(t22,t0,0)

POK_outdoor_bulb = POK.Appliance(POK,1,13,1,10,v3,10, wd_we_type = 0)   
POK_outdoor_bulb.windows(t_out,t0,0)

POK_outdoor_bulb = POK.Appliance(POK,1,13,1,10,v3,10, wd_we_type = 0)   
POK_outdoor_bulb.windows(CTF,t0,0)

                        ###


POK_TV = POK.Appliance(POK,1,60,1,90,v1,90, wd_we_type = 0)
POK_TV.windows(t22,t0,v1)

POK_Phone_charger = POK.Appliance(POK,2,5,1,45,v1,45, wd_we_type = 0)
POK_Phone_charger.windows(t10,t0,0)

POK_Phone_charger = POK.Appliance(POK,2,5,1,15,v1,15, wd_we_type = 0)
POK_Phone_charger.windows(t22,t0,v1)

POK_Laptop_PC_charger = POK.Appliance(POK,2,50,1,30,v1,30, wd_we_type = 0)
POK_Laptop_PC_charger.windows(t10,t0,0)

POK_Laptop_PC_charger = POK.Appliance(POK,2,50,1,30,v1,30, wd_we_type = 0)
POK_Laptop_PC_charger.windows(t22,t0,v1)

POK_Herd = POK.Appliance(POK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
POK_Herd.windows(tc0,t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,5,0.15)
POK_Herd.cycle_behaviour(tc0,t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
POK_Herd.windows(tc2,t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour(tc2,t0)

POK_Herd = POK.Appliance(POK,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
POK_Herd.windows(tc3,t0,v1)
POK_Herd.specific_cycle_1(1800,10,0.15)
POK_Herd.cycle_behaviour(tc3,t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
POK_Herd.windows(tc4,t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour(tc4,t0)


# POK Weekends/Holidays


POK_bulb_living = POK.Appliance(POK,2,10,1,60,v3,60, wd_we_type = 1)
POK_bulb_living.windows(t11,t0,v1)

POK_bulb_living = POK.Appliance(POK,2,10,2,300,v3,300, wd_we_type = 1)
POK_bulb_living.windows(CTF,th,0)

POK_bulb_kitchen = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 1)
POK_bulb_kitchen.windows(t11,t0,v1)

POK_bulb_kitchen = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 1)
POK_bulb_kitchen.windows(t3,t0,v1)

POK_bulb_kitchen = POK.Appliance(POK,1,10,2,120,v3,120, wd_we_type = 1)
POK_bulb_kitchen.windows(t22,th,0)

POK_bulb1_bedroom = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 1)
POK_bulb1_bedroom.windows(t11,t0,v1)

POK_bulb1_bedroom = POK.Appliance(POK,1,10,2,30,v3,30, wd_we_type = 1)
POK_bulb1_bedroom.windows(t2,th,v1)

POK_bulb2_bedroom = POK.Appliance(POK,1,10,1,15,v3,15, wd_we_type = 1)
POK_bulb2_bedroom.windows(t11,t0,v1)

POK_bulb2_bedroom = POK.Appliance(POK,1,10,1,15,v3,15, wd_we_type = 1)
POK_bulb2_bedroom.windows([1140,1320],t0,v1)

POK_bulb_BT_hallway = POK.Appliance(POK,2,10,1,30,v3,15, wd_we_type = 1)
POK_bulb_BT_hallway.windows(t11,t0,v1)

POK_bulb_BT_hallway = POK.Appliance(POK,2,10,2,30,v3,15, wd_we_type = 1)
POK_bulb_BT_hallway.windows(CTF,th,0)

POK_outdoor_bulb = POK.Appliance(POK,1,13,1,10,v3,10, wd_we_type = 1)   
POK_outdoor_bulb.windows(t_out,t0,0)

POK_outdoor_bulb = POK.Appliance(POK,1,13,2,10,v3,10, wd_we_type = 1)  
POK_outdoor_bulb.windows(CTF,th,0)

                                ###

POK_TV = POK.Appliance(POK,1,60,1,30,v2,30, wd_we_type = 1)
POK_TV.windows(tm0,t0,v1)

POK_TV = POK.Appliance(POK,1,60,1,30,v2,30, wd_we_type = 1)
POK_TV.windows(tc3,t0,v1)

POK_TV = POK.Appliance(POK,1,60,2,60,v2,60, wd_we_type = 1)
POK_TV.windows(t22,th,0)

POK_Phone_charger = POK.Appliance(POK,2,5,1,45,v1,45, wd_we_type = 1)
POK_Phone_charger.windows(tm0,t0,v1)

POK_Phone_charger = POK.Appliance(POK,2,5,2,15,v1,15, wd_we_type = 1)
POK_Phone_charger.windows(t22,th,0)

POK_Laptop_PC_charger = POK.Appliance(POK,2,50,1,30,v2,30, wd_we_type = 1)
POK_Laptop_PC_charger.windows(tm0,t0,v1)

POK_Laptop_PC_charger = POK.Appliance(POK,2,50,1,30,v2,30, wd_we_type = 1)
POK_Laptop_PC_charger.windows(tc3,t0,v1)

POK_Laptop_PC_charger = POK.Appliance(POK,2,50,2,30,v2,30, wd_we_type = 1)
POK_Laptop_PC_charger.windows(t22,th,0)

POK_Herd = POK.Appliance(POK,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows(tc1,t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,5,0.15)
POK_Herd.cycle_behaviour(tc1,t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows(tc2,t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour(tc2,t0)

POK_Herd = POK.Appliance(POK,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows(tc3,t0,v1)
POK_Herd.specific_cycle_1(1800,10,0.15)
POK_Herd.cycle_behaviour(tc3,t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows(tc4,t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour(tc4,t0)


# POK All time ON devices


POK_router = POK.Appliance(POK,1,7,1,1440,0)
POK_router.windows([0,1440],t0)

POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3)
POK_Kuehlschrank.windows([0,1440],t0)
POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
POK_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3)
POK_Tiefkuehl.windows([0,1440],t0)
POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
POK_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# POK Occasional_use devices


POK_Mixer = POK.Appliance(POK,1,50,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
POK_Mixer.windows(tc0,tc4,v1)

POK_Mixer = POK.Appliance(POK,1,50,4,15,0,15, occasional_use = 0.5, wd_we_type = 1)
POK_Mixer.windows(tc1,tc2,v1,tc3,tc4)

POK_Toaster = POK.Appliance(POK,1,1000,2,10,0,10, occasional_use = 0.6, wd_we_type = 0)
POK_Toaster.windows(tc0,tc4,v1)

POK_Toaster = POK.Appliance(POK,1,1000,4,10,0,10, occasional_use = 0.6, wd_we_type = 1)
POK_Toaster.windows(tc1,tc2,v1,tc3,tc4)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
POK_Haartrockner.windows([420,720],[960,1260],v1)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
POK_Haartrockner.windows(tm0,[960,1260],v1)

POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
POK_Luftfritteuse.windows(tc0,tc4,v1)

POK_Luftfritteuse = POK.Appliance(POK,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
POK_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
POK_Spuelmaschine.windows([420,660],[1020,1320],v1)

POK_Spuelmaschine = POK.Appliance(POK,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
POK_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
POK_Waschmaschine.windows(tc0,[1020,1260],v1)

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
POK_Waschmaschine.windows(tm0,[1020,1260],v1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
POK_Ofen.windows(tc0,tc4,v1)

POK_Ofen = POK.Appliance(POK,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
POK_Ofen.windows(tc1,tc2,v1,tc3,tc4)

#%%


# PMK Weekdays

PMK_bulb_living = PMK.Appliance(PMK,3,10,1,60,v3,60, wd_we_type = 0)
PMK_bulb_living.windows(t1,t0,v1)

PMK_bulb_living = PMK.Appliance(PMK,3,10,1,300,v3,300, wd_we_type = 0)
PMK_bulb_living.windows(CTF,t0,0)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,10,1,60,v3,60, wd_we_type = 0)
PMK_bulb_kitchen.windows(t1,t0,v1)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,10,1,120,v3,120, wd_we_type = 0)
PMK_bulb_kitchen.windows(t22,t0,v1)

PMK_bulb1_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb1_bedroom.windows(t1,t0,v1)

PMK_bulb1_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb1_bedroom.windows(t2,t0,v1)

PMK_bulb2_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb2_bedroom.windows(t1,t0,v1)

PMK_bulb2_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb2_bedroom.windows(t3,t0,v1)

PMK_bulb2_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb2_bedroom.windows(t2,t0,v1)

PMK_bulb_BT_hallway = PMK.Appliance(PMK,2,10,1,30,v3,15, wd_we_type = 0)
PMK_bulb_BT_hallway.windows(t1,t0,v1)

PMK_bulb_BT_hallway = PMK.Appliance(PMK,2,10,1,30,v3,15, wd_we_type = 0)
PMK_bulb_BT_hallway.windows(t22,t0,0)

PMK_outdoor_bulb = PMK.Appliance(PMK,2,13,1,10,v3,10, wd_we_type = 0)  
PMK_outdoor_bulb.windows(t_out,t0,0)

PMK_outdoor_bulb = PMK.Appliance(PMK,2,13,1,10,v3,10, wd_we_type = 0)   
PMK_outdoor_bulb.windows(CTF,t0,0)

                        ###


PMK_TV = PMK.Appliance(PMK,1,60,1,30,v1,30, wd_we_type = 0)
PMK_TV.windows(tc3,t0,v1)

PMK_TV = PMK.Appliance(PMK,1,60,1,60,v1,60, wd_we_type = 0)
PMK_TV.windows(t22,t0,v1)

PMK_Phone_charger = PMK.Appliance(PMK,3,5,1,45,v1,45, wd_we_type = 0)
PMK_Phone_charger.windows(t10,t0,0)

PMK_Phone_charger = PMK.Appliance(PMK,3,5,1,15,v1,15, wd_we_type = 0)
PMK_Phone_charger.windows(t22,t0,v1)

PMK_Laptop_PC_charger = PMK.Appliance(PMK,2,50,1,30,v1,30, wd_we_type = 0)
PMK_Laptop_PC_charger.windows(t10,t0,0)

PMK_Laptop_PC_charger = PMK.Appliance(PMK,2,50,1,30,v1,30, wd_we_type = 0)
PMK_Laptop_PC_charger.windows(tc3,t0,0)

PMK_Laptop_PC_charger = PMK.Appliance(PMK,2,50,1,30,v1,30, wd_we_type = 0)
PMK_Laptop_PC_charger.windows(t22,t0,v1)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
PMK_Herd.windows(tc0,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,5,0.15)
PMK_Herd.cycle_behaviour(tc0,t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
PMK_Herd.windows(tc2,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour(tc2,t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, occasional_use = 0.3, wd_we_type = 0)
PMK_Herd.windows(tc3,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,0.15)
PMK_Herd.cycle_behaviour(tc3,t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
PMK_Herd.windows(tc4,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour(tc4,t0)


# PMK Weekends/Holidays


PMK_bulb_living = PMK.Appliance(PMK,3,10,1,60,v3,60, wd_we_type = 1)
PMK_bulb_living.windows(t11,t0,v1)

PMK_bulb_living = PMK.Appliance(PMK,3,10,2,300,v3,300, wd_we_type = 1)
PMK_bulb_living.windows(CTF,th,0)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb_kitchen.windows(t11,t0,v1)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb_kitchen.windows(t3,t0,v1)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,10,2,120,v3,120, wd_we_type = 1)
PMK_bulb_kitchen.windows(t22,th,0)

PMK_bulb1_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb1_bedroom.windows(t11,t0,v1)

PMK_bulb1_bedroom = PMK.Appliance(PMK,1,10,2,30,v3,30, wd_we_type = 1)
PMK_bulb1_bedroom.windows(t2,th,v1)

PMK_bulb2_bedroom = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb2_bedroom.windows(t11,t0,v1)

PMK_bulb2_bedroom = PMK.Appliance(PMK,1,10,1,60,v3,60, wd_we_type = 1)
PMK_bulb2_bedroom.windows([960,1320],t0,0)

PMK_bulb2_bedroom = PMK.Appliance(PMK,1,10,2,30,v3,30, wd_we_type = 1)
PMK_bulb2_bedroom.windows(t2,th,v1)

PMK_bulb_BT_hallway = PMK.Appliance(PMK,2,10,1,30,v3,15, wd_we_type = 1)
PMK_bulb_BT_hallway.windows(t11,t0,v1)

PMK_bulb_BT_hallway = PMK.Appliance(PMK,2,10,2,30,v3,15, wd_we_type = 1)
PMK_bulb_BT_hallway.windows(CTF,th,0)

PMK_outdoor_bulb = PMK.Appliance(PMK,1,13,1,10,v3,10, wd_we_type = 1)   
PMK_outdoor_bulb.windows(t_out,t0,0)

PMK_outdoor_bulb = PMK.Appliance(PMK,1,13,2,30,v3,30, wd_we_type = 1)  
PMK_outdoor_bulb.windows(CTF,th,0)

                                ###

PMK_TV = PMK.Appliance(PMK,1,60,1,30,v2,30, wd_we_type = 1)
PMK_TV.windows(tm0,t0,v1)

PMK_TV = PMK.Appliance(PMK,1,60,1,30,v2,30, wd_we_type = 1)
PMK_TV.windows(tc3,t0,v1)

PMK_TV = PMK.Appliance(PMK,1,60,2,60,v2,60, wd_we_type = 1)
PMK_TV.windows(t22,th,0)

PMK_Phone_charger = PMK.Appliance(PMK,3,5,1,45,v1,45, wd_we_type = 1)
PMK_Phone_charger.windows(tm0,t0,v1)

PMK_Phone_charger = PMK.Appliance(PMK,3,5,2,15,v1,15, wd_we_type = 1)
PMK_Phone_charger.windows(t22,th,0)

PMK_Laptop_PC_charger = PMK.Appliance(PMK,2,50,1,30,v2,30, wd_we_type = 1)
PMK_Laptop_PC_charger.windows(tm0,t0,v1)

PMK_Laptop_PC_charger = PMK.Appliance(PMK,2,50,1,60,v2,60, wd_we_type = 1)
PMK_Laptop_PC_charger.windows(tc3,t0,v1)

PMK_Laptop_PC_charger = PMK.Appliance(PMK,2,50,2,30,v2,30, wd_we_type = 1)
PMK_Laptop_PC_charger.windows(t22,th,0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows(tc1,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,5,0.15)
PMK_Herd.cycle_behaviour(tc1,t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows(tc2,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour(tc2,t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows(tc3,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,0.15)
PMK_Herd.cycle_behaviour(tc3,t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows(tc4,t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour(tc4,t0)


# PMK All time ON devices


PMK_router = PMK.Appliance(PMK,1,7,1,1440,0)
PMK_router.windows([0,1440],t0)

PMK_Kuehlschrank = PMK.Appliance(PMK,1,150,1,1440,0,30,'yes',3)
PMK_Kuehlschrank.windows([0,1440],t0)
PMK_Kuehlschrank.specific_cycle_1(150,20,5,10)
PMK_Kuehlschrank.specific_cycle_2(150,15,5,15)
PMK_Kuehlschrank.specific_cycle_3(150,10,5,20)
PMK_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

PMK_Tiefkuehl = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3)
PMK_Tiefkuehl.windows([0,1440],t0)
PMK_Tiefkuehl.specific_cycle_1(200,20,5,10)
PMK_Tiefkuehl.specific_cycle_2(200,15,5,15)
PMK_Tiefkuehl.specific_cycle_3(200,10,5,20)
PMK_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# PMK Occasional_use devices


PMK_Mixer = PMK.Appliance(PMK,1,50,3,15,0,15, occasional_use = 0.7, wd_we_type = 0)
PMK_Mixer.windows(tc0,tc3,v1,tc4)

PMK_Mixer = PMK.Appliance(PMK,1,50,4,15,0,15, occasional_use = 0.7, wd_we_type = 1)
PMK_Mixer.windows(tc1,tc2,v1,tc3,tc4)

PMK_Toaster = PMK.Appliance(PMK,1,1000,3,10,0,10, occasional_use = 0.8, wd_we_type = 0)
PMK_Toaster.windows(tc0,tc3,v1,tc4)

PMK_Toaster = PMK.Appliance(PMK,1,1000,4,10,0,10, occasional_use = 0.8, wd_we_type = 1)
PMK_Toaster.windows(tc1,tc2,v1,tc3,tc4)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
PMK_Haartrockner.windows([420,720],[960,1260],v1)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
PMK_Haartrockner.windows(tm0,[960,1260],v1)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,3,30,0,30, occasional_use = 0.5, wd_we_type = 0)
PMK_Luftfritteuse.windows(tc0,tc3,v1,tc4)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,4,30,0,30, occasional_use = 0.5, wd_we_type = 1)
PMK_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
PMK_Spuelmaschine.windows([420,660],[1020,1320],v1)

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
PMK_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.5, wd_we_type = 0)
PMK_Waschmaschine.windows(tc0,[1020,1260],v1)

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.5, wd_we_type = 1)
PMK_Waschmaschine.windows(tm0,[1020,1260],v1)

PMK_Ofen = PMK.Appliance(PMK,1,2150,3,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
PMK_Ofen.windows(tc0,tc3,v1,tc4)

PMK_Ofen = PMK.Appliance(PMK,1,2150,3,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
PMK_Ofen.windows(tc1,tc2,v1,tc3,tc4)




#%%


# MP Weekdays

MP_bulb_living = MP.Appliance(MP,4,10,1,60,v3,60, wd_we_type = 0)
MP_bulb_living.windows(t1,t0,v1)

MP_bulb_living = MP.Appliance(MP,4,10,1,300,v3,300, wd_we_type = 0)
MP_bulb_living.windows(CTF,t0,0)

MP_bulb_kitchen = MP.Appliance(MP,2,10,1,60,v3,60, wd_we_type = 0)
MP_bulb_kitchen.windows(t1,t0,v1)

MP_bulb_kitchen = MP.Appliance(MP,2,10,1,120,v3,120, wd_we_type = 0)
MP_bulb_kitchen.windows(t22,t0,v1)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb1_bedroom.windows(t1,t0,v1)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb1_bedroom.windows(t2,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom.windows(t1,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom.windows(t3,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom.windows(t2,t0,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb3_bedroom.windows(t1,t0,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb3_bedroom.windows(t2,t0,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,1,30,v3,15, wd_we_type = 0)
MP_bulb_BT_hallway.windows(t1,t0,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,1,30,v3,15, wd_we_type = 0)
MP_bulb_BT_hallway.windows(CTF,t0,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,1,10,v3,10, wd_we_type = 0)  
MP_outdoor_bulb.windows(t_out,t0,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,1,10,v3,10, wd_we_type = 0)   
MP_outdoor_bulb.windows(CTF,t0,0)

                        ###

MP_TV = MP.Appliance(MP,2,60,1,30,v1,30, wd_we_type = 0)
MP_TV.windows(tm0,t0,v1)

MP_TV = MP.Appliance(MP,2,60,1,30,v1,30, wd_we_type = 0)
MP_TV.windows(tc3,t0,v1)

MP_TV = MP.Appliance(MP,2,60,1,60,v1,60, wd_we_type = 0)
MP_TV.windows(t22,t0,v1)

MP_Phone_charger = MP.Appliance(MP,5,5,1,45,v1,45, wd_we_type = 0)
MP_Phone_charger.windows(t10,t0,0)

MP_Phone_charger = MP.Appliance(MP,5,5,1,15,v1,15, wd_we_type = 0)
MP_Phone_charger.windows(t22,t0,v1)

MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
MP_Laptop_PC_charger.windows(t10,t0,0)

MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
MP_Laptop_PC_charger.windows(tc3,t0,0)

MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
MP_Laptop_PC_charger.windows(t22,t0,v1)

MP_Herd = MP.Appliance(MP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows(tc0,t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,5,0.15)
MP_Herd.cycle_behaviour(tc0,t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows(tc2,t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour(tc2,t0)

MP_Herd = MP.Appliance(MP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows(tc3,t0,v1)
MP_Herd.specific_cycle_1(1800,10,0.15)
MP_Herd.cycle_behaviour(tc3,t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows(tc4,t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour(tc4,t0)


# MP Weekends/Holidays


MP_bulb_living = MP.Appliance(MP,4,10,1,60,v3,60, wd_we_type = 1)
MP_bulb_living.windows(t11,t0,v1)

MP_bulb_living = MP.Appliance(MP,4,10,2,300,v3,300, wd_we_type = 1)
MP_bulb_living.windows(CTF,th,0)

MP_bulb_kitchen = MP.Appliance(MP,2,10,1,30,v3,30, wd_we_type = 1)
MP_bulb_kitchen.windows(t11,t0,v1)

MP_bulb_kitchen = MP.Appliance(MP,2,10,1,30,v3,30, wd_we_type = 1)
MP_bulb_kitchen.windows(t3,t0,v1)

MP_bulb_kitchen = MP.Appliance(MP,2,10,2,120,v3,120, wd_we_type = 1)
MP_bulb_kitchen.windows(t22,th,0)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb1_bedroom.windows(t11,t0,v1)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,2,30,v3,30, wd_we_type = 1)
MP_bulb1_bedroom.windows(t2,th,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom.windows(t11,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,60,v3,60, wd_we_type = 1)
MP_bulb2_bedroom.windows([960,1320],t0,0)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,2,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom.windows(t2,th,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb3_bedroom.windows(t11,t0,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,2,30,v3,30, wd_we_type = 1)
MP_bulb3_bedroom.windows(t2,th,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,1,30,v3,15, wd_we_type = 1)
MP_bulb_BT_hallway.windows(t11,t0,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,2,30,v3,15, wd_we_type = 1)
MP_bulb_BT_hallway.windows(CTF,th,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,1,10,v3,10, wd_we_type = 1)   
MP_outdoor_bulb.windows(t_out,t0,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,2,30,v3,30, wd_we_type = 1)  
MP_outdoor_bulb.windows(CTF,th,0)

                                ###

MP_TV = MP.Appliance(MP,2,60,1,30,v2,30, wd_we_type = 1)
MP_TV.windows(tm0,t0,v1)

MP_TV = MP.Appliance(MP,2,60,1,60,v2,60, wd_we_type = 1)
MP_TV.windows(tc3,t0,v1)

MP_TV = MP.Appliance(MP,2,60,2,60,v2,60, wd_we_type = 1)
MP_TV.windows(t22,th,0)

MP_Phone_charger = MP.Appliance(MP,5,5,1,45,v1,45, wd_we_type = 1)
MP_Phone_charger.windows(tm0,t0,v1)

MP_Phone_charger = MP.Appliance(MP,5,5,2,15,v1,15, wd_we_type = 1)
MP_Phone_charger.windows(t22,th,0)

MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v2,30, wd_we_type = 1)
MP_Laptop_PC_charger.windows(tm0,t0,v1)

MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,60,v2,60, wd_we_type = 1)
MP_Laptop_PC_charger.windows(tc3,t0,v1)

MP_Laptop_PC_charger = MP.Appliance(MP,2,50,2,30,v2,30, wd_we_type = 1)
MP_Laptop_PC_charger.windows(t22,th,0)

MP_Herd = MP.Appliance(MP,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows(tc1,t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,5,0.15)
MP_Herd.cycle_behaviour(tc1,t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows(tc2,t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour(tc2,t0)

MP_Herd = MP.Appliance(MP,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows(tc3,t0,v1)
MP_Herd.specific_cycle_1(1800,10,0.15)
MP_Herd.cycle_behaviour(tc3,t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows(tc4,t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour(tc4,t0)


# MP All time ON devices


MP_router = MP.Appliance(MP,1,7,1,1440,0)
MP_router.windows([0,1440],t0)

MP_Kuehlschrank = MP.Appliance(MP,1,150,1,1440,0,30,'yes',3)
MP_Kuehlschrank.windows([0,1440],t0)
MP_Kuehlschrank.specific_cycle_1(150,20,5,10)
MP_Kuehlschrank.specific_cycle_2(150,15,5,15)
MP_Kuehlschrank.specific_cycle_3(150,10,5,20)
MP_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

MP_Tiefkuehl = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3)
MP_Tiefkuehl.windows([0,1440],t0)
MP_Tiefkuehl.specific_cycle_1(200,20,5,10)
MP_Tiefkuehl.specific_cycle_2(200,15,5,15)
MP_Tiefkuehl.specific_cycle_3(200,10,5,20)
MP_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# MP Occasional_use devices


MP_Mixer = MP.Appliance(MP,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 0)
MP_Mixer.windows(tc0,tc2,v1,tc3,tc4)

MP_Mixer = MP.Appliance(MP,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 1)
MP_Mixer.windows(tc1,tc2,v1,tc3,tc4)

MP_Toaster = MP.Appliance(MP,1,1000,4,10,0,10, occasional_use = 1, wd_we_type = 0)
MP_Toaster.windows(tc0,tc2,v1,tc3,tc4)

MP_Toaster = MP.Appliance(MP,1,1000,4,10,0,10, occasional_use = 1, wd_we_type = 1)
MP_Toaster.windows(tc1,tc2,v1,tc3,tc4)

MP_Haartrockner = MP.Appliance(MP,1,1000,2,15,0,15, occasional_use = 1, wd_we_type = 0)
MP_Haartrockner.windows([420,720],[960,1260],v1)

MP_Haartrockner = MP.Appliance(MP,1,1000,2,15,0,15, occasional_use = 1, wd_we_type = 1)
MP_Haartrockner.windows(tm0,[960,1260],v1)

MP_Luftfritteuse = MP.Appliance(MP,1,50,4,30,0,30, occasional_use = 1, wd_we_type = 0)
MP_Luftfritteuse.windows(tc0,tc2,v1,tc3,tc4)

MP_Luftfritteuse = MP.Appliance(MP,1,50,4,30,0,30, occasional_use = 1, wd_we_type = 1)
MP_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

MP_Spuelmaschine = MP.Appliance(MP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 0)
MP_Spuelmaschine.windows([420,660],[780,960],v1,[1020,1320])

MP_Spuelmaschine = MP.Appliance(MP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 1)
MP_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 0)
MP_Waschmaschine.windows(tc0,[1020,1260],v1)

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 1)
MP_Waschmaschine.windows(tm0,[1020,1260],v1)

MP_Ofen = MP.Appliance(MP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 0)
MP_Ofen.windows(tc0,tc2,v1,tc3,tc4)

MP_Ofen = MP.Appliance(MP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 1)
MP_Ofen.windows(tc1,tc2,v1,tc3,tc4)




