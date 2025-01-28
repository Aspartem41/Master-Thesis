# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:39:01 2023

@author: rbala

This infut file is for Autumn
"""

from ramp.core.core import User, np
User_list = []



PMK = User("Paar Mit Kind",3,3)
User_list.append(PMK)


t0 = [0,0]
t1 = [390,510]   # 6:30 - 8:30
t11 = [450,510]  # 7:30 - 8:30
t2 = [1140,1380] # 19:00 - 23:00
t22 = [1140,1440]# 19:00 - 00:00
v1 = 0.1
v2 = 0.2
#%%'

#  PMK Weekdays


PMK_bulb_living_1_1= PMK.Appliance(PMK,2,10,1,60,0,60, wd_we_type = 0)
PMK_bulb_living_1_1.windows(t1,t0,v1)

PMK_bulb_living_1_2 = PMK.Appliance(PMK,2,10,1,210,0,210, wd_we_type = 0)
PMK_bulb_living_1_2.windows([1020,1380],t0,0)

PMK_bulb_kitchen_1= PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
PMK_bulb_kitchen_1.windows(t1,t0,v1)

PMK_bulb_kitchen_2= PMK.Appliance(PMK,1,10,1,120,0,120, wd_we_type = 0)
PMK_bulb_kitchen_2.windows(t2,t0,v1)

PMK_bulb1_bedroom_1= PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
PMK_bulb1_bedroom_1.windows(t1,t0,v1)

PMK_bulb1_bedroom_2= PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
PMK_bulb1_bedroom_2.windows([1320,1380],t0,v1)

PMK_bulb2_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
PMK_bulb2_bedroom_1.windows(t1,t0,v1)

PMK_bulb2_bedroom_2 = PMK.Appliance(PMK,1,10,1,15,0,15, wd_we_type = 0)
PMK_bulb2_bedroom_2.windows([1020,1140],t0,v1)

PMK_bulb2_bedroom_3 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
PMK_bulb2_bedroom_3.windows([1320,1380],t0,v1)

# PMK_bulb3_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
# PMK_bulb3_bedroom_1.windows(t1,t0,v1)

# PMK_bulb3_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
# PMK_bulb3_bedroom_2.windows([1320,1380],t0,v1)

PMK_bulb_BT_hallway_1 = PMK.Appliance(PMK,3,10,1,15,0,10, wd_we_type = 0)
PMK_bulb_BT_hallway_1.windows(t1,t0,v1)

PMK_bulb_BT_hallway_2 = PMK.Appliance(PMK,3,10,1,20,0,10, wd_we_type = 0)
PMK_bulb_BT_hallway_2.windows([1020,1380],t0,0)

PMK_outdoor_bulb_1 = PMK.Appliance(PMK,2,13,1,5,0,5, wd_we_type = 0)  
PMK_outdoor_bulb_1.windows([0,510],t0,0)

PMK_outdoor_bulb_2 = PMK.Appliance(PMK,2,13,1,10,0,10, wd_we_type = 0)   
PMK_outdoor_bulb_2.windows(t22,t0,0)

                                  ###

# PMK_TV_1= PMK.Appliance(PMK,1,60,1,30,v1,30, wd_we_type = 0)
# PMK_TV_1.windows([540,720],t0,v1)

PMK_TV_2= PMK.Appliance(PMK,1,60,1,30,v1,30, wd_we_type = 0)
PMK_TV_2.windows([840,1020],t0,v1)

PMK_TV_3= PMK.Appliance(PMK,1,60,1,60,v1,60, wd_we_type = 0)
PMK_TV_3.windows(t2,t0,v1)

PMK_Phone_charger_1 = PMK.Appliance(PMK,3,5,1,45,v1,45, wd_we_type = 0)
PMK_Phone_charger_1.windows([390,450],t0,0)

PMK_Phone_charger_2 = PMK.Appliance(PMK,3,5,1,15,v1,15, wd_we_type = 0)
PMK_Phone_charger_2.windows(t2,t0,v1)

PMK_Laptop_PC_charger_1 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 0)
PMK_Laptop_PC_charger_1.windows([390,450],t0,0)

PMK_Laptop_PC_charger_2 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 0)
PMK_Laptop_PC_charger_2.windows([840,1020],t0,0)

PMK_Laptop_PC_charger_3 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 0)
PMK_Laptop_PC_charger_3.windows(t2,t0,v1)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
PMK_Herd.windows([420,540],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,5,0.15)
PMK_Herd.cycle_behaviour([480,600],t0)

# PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# PMK_Herd.windows([660,780],t0,v1)
# PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
# PMK_Herd.cycle_behaviour([660,780],t0)

# PMK_Herd = PMK.Appliance(PMK,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# PMK_Herd.windows([900,1020],t0,v1)
# PMK_Herd.specific_cycle_1(1800,10,0.15)
# PMK_Herd.cycle_behaviour([900,1020],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
PMK_Herd.windows([1140,1260],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour([1140,1260],t0)



# PMK Weekends/Holidays


PMK_bulb_living_1_1= PMK.Appliance(PMK,2,10,1,60,0,60, wd_we_type = 1)
PMK_bulb_living_1_1.windows(t11,t0,v1)

PMK_bulb_living_1_2 = PMK.Appliance(PMK,2,10,1,210,0,210, wd_we_type = 1)
PMK_bulb_living_1_2.windows([1020,1440],t0,0)

PMK_bulb_kitchen_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
PMK_bulb_kitchen_1.windows(t11,t0,v1)

# PMK_bulb_kitchen_2 = PMK.Appliance(PMK,2,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb_kitchen_2.windows([960,1140],t0,v1)

PMK_bulb_kitchen_3 = PMK.Appliance(PMK,1,10,1,120,0,120, wd_we_type = 1)
PMK_bulb_kitchen_3.windows(t22,t0,v1)

PMK_bulb1_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
PMK_bulb1_bedroom_1.windows(t11,t0,v1)

PMK_bulb1_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
PMK_bulb1_bedroom_2.windows([1320,1440],t0,v1)

PMK_bulb2_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
PMK_bulb2_bedroom_1.windows(t11,t0,v1)

PMK_bulb2_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
PMK_bulb2_bedroom_2.windows([1020,1320],t0,0)

PMK_bulb2_bedroom_3 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
PMK_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# PMK_bulb3_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb3_bedroom_1.windows(t11,t0,v1)

# PMK_bulb3_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb3_bedroom_2.windows([1320,1440],t0,v1)

PMK_bulb_BT_hallway_1 = PMK.Appliance(PMK,3,10,1,15,0,10, wd_we_type = 1)
PMK_bulb_BT_hallway_1.windows(t11,t0,v1)

PMK_bulb_BT_hallway_2 = PMK.Appliance(PMK,3,10,1,20,0,10, wd_we_type = 1)
PMK_bulb_BT_hallway_2.windows([1020,1440],t0,0)

PMK_outdoor_bulb_1 = PMK.Appliance(PMK,2,13,1,10,0,10, wd_we_type = 1)   
PMK_outdoor_bulb_1.windows([0,510],t0,0)

PMK_outdoor_bulb_2 = PMK.Appliance(PMK,2,13,1,15,0,15, wd_we_type = 1)  
PMK_outdoor_bulb_2.windows([1020,1440],t0,0)

                              ###

PMK_TV_1= PMK.Appliance(PMK,1,60,1,30,v1,30, wd_we_type = 1)
PMK_TV_1.windows([540,720],t0,v1)

PMK_TV_2= PMK.Appliance(PMK,1,60,1,30,v1,30, wd_we_type = 1)
PMK_TV_2.windows([840,1020],t0,v1)

PMK_TV_3= PMK.Appliance(PMK,1,60,1,60,v1,60, wd_we_type = 1)
PMK_TV_3.windows(t22,t0,0)

PMK_Phone_charger_1 = PMK.Appliance(PMK,3,5,1,45,v1,45, wd_we_type = 1)
PMK_Phone_charger_1.windows([540,720],t0,v1)

PMK_Phone_charger_2 = PMK.Appliance(PMK,3,5,1,15,v1,15, wd_we_type = 1)
PMK_Phone_charger_2.windows(t22,t0,0)

PMK_Laptop_PC_charger_1 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 1)
PMK_Laptop_PC_charger_1.windows([540,720],t0,v1)

PMK_Laptop_PC_charger_2 = PMK.Appliance(PMK,2,50,1,60,0.05,60, wd_we_type = 1)
PMK_Laptop_PC_charger_2.windows([840,1020],t0,v1)

PMK_Laptop_PC_charger_3 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 1)
PMK_Laptop_PC_charger_3.windows(t22,t0,0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([480,600],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,5,0.15)
PMK_Herd.cycle_behaviour([480,600],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([660,780],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour([660,780],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([900,1020],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,0.15)
PMK_Herd.cycle_behaviour([900,1020],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([1140,1260],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour([1140,1260],t0)


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


# PMK Occasional used devices


PMK_Mixer = PMK.Appliance(PMK,1,50,2,15,0,10, occasional_use = 0.7)
PMK_Mixer.windows([420,540],[1140,1260],v1)

PMK_Toaster = PMK.Appliance(PMK,1,1000,2,10,0,10, occasional_use = 0.8)
PMK_Toaster.windows([420,540],[1140,1260],v1)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,15,0,15,occasional_use = 0.5)
PMK_Haartrockner.windows([420,720],[960,1260],v1)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,2,30,0,15,occasional_use = 0.5)
PMK_Luftfritteuse.windows([420,540],[1140,1260], v1)

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,120,0,60, thermal_P_var = 0.2, occasional_use= 0.5)
PMK_Spuelmaschine.windows([780,900],[1200,1320],v1)

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.5)
PMK_Waschmaschine.windows([540,720],[1020,1260],v1)

PMK_Ofen = PMK.Appliance(PMK,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5)
PMK_Ofen.windows([420,540],[1140,1260],v1)












































# PMK = User("Paar Mit Kind",1,3)
# User_list.append(PMK)

# t0 = [0,0]
# t1 = [330,450] # 5:30 - 7:30
# t2 = [330,510] # 5:30 - 8:30
# #%%'
# # Paar Mit Kind

# PMK_bulb_living_1_1 = PMK.Appliance(PMK,2,10,1,60,0,60)
# PMK_bulb_living_1_1.windows(t2,t0,0.1)

# PMK_bulb_living_1_2 = PMK.Appliance(PMK,2,10,1,210,0,210)
# PMK_bulb_living_1_2.windows([1140,1380],t0,0)

# PMK_bulb_kitchen_1= PMK.Appliance(PMK,1,10,1,30,0,30)
# PMK_bulb_kitchen_1.windows(t1,t0,0.1)

# PMK_bulb_kitchen_2= PMK.Appliance(PMK,1,10,1,120,0,120)
# PMK_bulb_kitchen_2.windows([1140,1290],t0,0.1)

# PMK_bulb1_bedroom_1= PMK.Appliance(PMK,1,10,1,30,0,30)
# PMK_bulb1_bedroom_1.windows(t2,t0,0.1)

# PMK_bulb1_bedroom_2= PMK.Appliance(PMK,1,10,1,30,0,30)
# PMK_bulb1_bedroom_2.windows([1320,1440],t0,0.1)

# PMK_bulb2_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30)
# PMK_bulb2_bedroom_1.windows(t2,t0,0.1)

# PMK_bulb2_bedroom_2 = PMK.Appliance(PMK,1,10,1,15,0,15)
# PMK_bulb2_bedroom_2.windows([1140,1320],t0,0.1)

# PMK_bulb2_bedroom_3 = PMK.Appliance(PMK,1,10,1,30,0,30)
# PMK_bulb2_bedroom_3.windows([1320,1440],t0,0.1)

# PMK_bulb_BT_hallway_1 = PMK.Appliance(PMK,3,10,1,15,0,15)
# PMK_bulb_BT_hallway_1.windows(t1,t0,0.1)

# PMK_bulb_BT_hallway_2 = PMK.Appliance(PMK,3,10,1,20,0,20)
# PMK_bulb_BT_hallway_2.windows([1140,1380],t0,0)

# PMK_outdoor_bulb_1 = PMK.Appliance(PMK,2,13,1,5,0.1,5)   # Meistens mit Bewegungssensor, deswegen nur 15 minuten
# PMK_outdoor_bulb_1.windows([0,510],t0,0)

# PMK_outdoor_bulb_2 = PMK.Appliance(PMK,2,13,1,10,0.1,10)   
# PMK_outdoor_bulb_2.windows([1140,1440],t0,0)

# PMK_TV_1 = PMK.Appliance(PMK,1,60,1,30,0.1,30)
# PMK_TV_1.windows([840,1020],t0,0.1)

# PMK_TV_2 = PMK.Appliance(PMK,1,60,1,60,0.1,60)
# PMK_TV_2.windows([1170,1380],t0,0.1)

# PMK_router = PMK.Appliance(PMK,1,7,1,1440,0.1)
# PMK_router.windows([0,1440],t0)

# PMK_Phone_charger_1 = PMK.Appliance(PMK,3,5,1,45,0.1,45)
# PMK_Phone_charger_1.windows(t1,t0,0)

# PMK_Phone_charger_2 = PMK.Appliance(PMK,3,5,1,15,0.1,15)
# PMK_Phone_charger_2.windows([1170,1440],t0,0)

# PMK_Laptop_PC_charger_1 = PMK.Appliance(PMK,2,50,1,30,0.05,30)
# PMK_Laptop_PC_charger_1.windows(t1,t0,0)

# PMK_Laptop_PC_charger_2 = PMK.Appliance(PMK,2,50,1,30,0.05,30)
# PMK_Laptop_PC_charger_2.windows([840,1020],t0,0)

# PMK_Laptop_PC_charger_3 = PMK.Appliance(PMK,2,50,1,30,0.05,30)
# PMK_Laptop_PC_charger_3.windows([1170,1440],t0,0)

# # PMK_Kuehlschrank = PMK.Appliance(PMK,1,150,1,1440,0,30,'yes',3)
# # PMK_Kuehlschrank.windows([0,1440],t0)
# # PMK_Kuehlschrank.specific_cycle_1(150,20,5,10)
# # PMK_Kuehlschrank.specific_cycle_2(150,15,5,15)
# # PMK_Kuehlschrank.specific_cycle_3(150,10,5,20)
# # PMK_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# # PMK_Tiefkuehl = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3)
# # PMK_Tiefkuehl.windows([0,1440],t0)
# # PMK_Tiefkuehl.specific_cycle_1(200,20,5,10)
# # PMK_Tiefkuehl.specific_cycle_2(200,15,5,15)
# # PMK_Tiefkuehl.specific_cycle_3(200,10,5,20)
# # PMK_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# # PMK_Mixer = PMK.Appliance(PMK,1,50,2,15,0.1,1, occasional_use = 0.33)
# # PMK_Mixer.windows([360,480],[1140,1260],0.1)

# # PMK_Toaster = PMK.Appliance(PMK,1,1000,2,10,0.1,5, occasional_use = 0.5)
# # PMK_Toaster.windows([360,480],[1140,1260],0.1)

# # PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,15,0.1,5,occasional_use = 0.5)
# # PMK_Haartrockner.windows([420,720],[960,1260],0.10)

# # PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,2,30,0.1,15,occasional_use = 0.33)
# # PMK_Luftfritteuse.windows([360,420],[1200,1260], 0.1)

# # PMK_Herd = PMK.Appliance(PMK,1,1800,2,60,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
# # PMK_Herd.windows([360,480],[1140,1260],0.1)
# # PMK_Herd.specific_cycle_1(1800,10,750,60,0.15)
# # PMK_Herd.cycle_behaviour([720,900],t0)

# # PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,75,0.1,60, thermal_P_var = 0.2, occasional_use=0.6)
# # PMK_Spuelmaschine.windows([420,540],[1200,1320],0.1)

# # PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.48)
# # PMK_Waschmaschine.windows([540,720],[1020,1260],0.1)

# # PMK_Ofen = PMK.Appliance(PMK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2)
# # PMK_Ofen.windows([360,480],[1140,1260],0.1)

# #%%'
# # Paar Mit Kind
# PMK_bulb_living_1 = PMK.Appliance(PMK,2,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb_living_1.windows([450,510],t0,0.1)

# PMK_bulb_living_2 = PMK.Appliance(PMK,1,10,1,60,0,60, wd_we_type = 1)
# PMK_bulb_living_2.windows([1020,1140],t0,0.1)

# PMK_bulb_living_3 = PMK.Appliance(PMK,2,10,1,180,0,180, wd_we_type = 1)
# PMK_bulb_living_3.windows([1140,1440],t0,0)

# # PMK_bulb_kitchen_1 = PMK.Appliance(PMK,1,7,1,30,0,30, wd_we_type = 1)
# # PMK_bulb_kitchen_1.windows([450,540],t0,0.1)

# # PMK_bulb_kitchen_2 = PMK.Appliance(PMK,1,10,1,15,0,15, wd_we_type = 1)
# # PMK_bulb_kitchen_2.windows([1080,1110],t0,0.1)

# PMK_bulb_kitchen_3 = PMK.Appliance(PMK,1,10,1,150,0,150, wd_we_type = 1)
# PMK_bulb_kitchen_3.windows([1140,1320],t0,0.1)

# PMK_bulb1_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb1_bedroom_1.windows([420,510],t0,0.1)

# PMK_bulb1_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb1_bedroom_2.windows([1320,1440],t0,0.1)

# PMK_bulb2_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb2_bedroom_1.windows([420,510],t0,0.1)

# PMK_bulb2_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb2_bedroom_2.windows([1020,1320],t0,0)

# PMK_bulb2_bedroom_3 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb2_bedroom_3.windows([1320,1440],t0,0.1)

# PMK_bulb_BT_hallway_1 = PMK.Appliance(PMK,3,10,1,15,0,15, wd_we_type = 1)
# PMK_bulb_BT_hallway_1.windows([450,510],t0,0.1)

# PMK_bulb_BT_hallway_2 = PMK.Appliance(PMK,3,10,1,20,0,20, wd_we_type = 1)
# PMK_bulb_BT_hallway_2.windows([1020,1380],t0,0)

# PMK_outdoor_bulb_1 = PMK.Appliance(PMK,1,13,1,10,0.1,10, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 15 minuten
# PMK_outdoor_bulb_1.windows([0,510],t0,0)

# PMK_outdoor_bulb_2 = PMK.Appliance(PMK,1,13,1,15,0.1,15, wd_we_type = 1)  
# PMK_outdoor_bulb_2.windows([1020,1440],t0,0)

# PMK_TV_1 = PMK.Appliance(PMK,1,60,1,30,0.1,30, wd_we_type = 1)
# PMK_TV_1.windows([540,720],t0,0.1)

# PMK_TV_2 = PMK.Appliance(PMK,1,60,1,30,0.1,30, wd_we_type = 1)
# PMK_TV_2.windows([900,1080],t0,0.1)

# PMK_TV_3 = PMK.Appliance(PMK,1,60,1,60,0.1,60, wd_we_type = 1)
# PMK_TV_3.windows([1170,1440],t0,0)

# PMK_router = PMK.Appliance(PMK,1,7,1,1440,0.1, wd_we_type = 1)
# PMK_router.windows([0,1440],t0)

# PMK_Phone_charger_1 = PMK.Appliance(PMK,3,5,1,45,0.1,45, wd_we_type = 1)
# PMK_Phone_charger_1.windows([600,780],t0,0.1)

# PMK_Phone_charger_2 = PMK.Appliance(PMK,3,5,1,15,0.1,15, wd_we_type = 1)
# PMK_Phone_charger_2.windows([1170,1440],t0,0.1)

# PMK_Laptop_PC_charger_1 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 1)
# PMK_Laptop_PC_charger_1.windows([600,780],t0,0.1)

# PMK_Laptop_PC_charger_2 = PMK.Appliance(PMK,2,50,1,60,0.05,60, wd_we_type = 1)
# PMK_Laptop_PC_charger_2.windows([840,1020],t0,0.1)

# PMK_Laptop_PC_charger_3 = PMK.Appliance(PMK,2,50,1,30,0.05,30, wd_we_type = 1)
# PMK_Laptop_PC_charger_3.windows([1170,1440],t0,0)

# # PMK_Kuehlschrank = PMK.Appliance(PMK,1,150,1,1440,0,30,'yes',3, wd_we_type = 1)
# # PMK_Kuehlschrank.windows([0,1440],t0)
# # PMK_Kuehlschrank.specific_cycle_1(150,20,5,10)
# # PMK_Kuehlschrank.specific_cycle_2(150,15,5,15)
# # PMK_Kuehlschrank.specific_cycle_3(150,10,5,20)
# # PMK_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# # PMK_Tiefkuehl = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3, wd_we_type = 1)
# # PMK_Tiefkuehl.windows([0,1440],t0)
# # PMK_Tiefkuehl.specific_cycle_1(200,20,5,10)
# # PMK_Tiefkuehl.specific_cycle_2(200,15,5,15)
# # PMK_Tiefkuehl.specific_cycle_3(200,10,5,20)
# # PMK_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# # PMK_Mixer = PMK.Appliance(PMK,1,50,2,15,0.1,1, occasional_use = 0.33, wd_we_type = 1)
# # PMK_Mixer.windows([660,750],[1140,1260],0.1)

# # PMK_Toaster = PMK.Appliance(PMK,1,1000,2,10,0.1,3, occasional_use = 0.5, wd_we_type = 1)
# # PMK_Toaster.windows([540,600],[900,1080],0.1)

# # PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,15,0.1,5,occasional_use = 0.5, wd_we_type = 1)
# # PMK_Haartrockner.windows([420,720],[960,1260],0.10)

# # PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,2,30,0.1,1,occasional_use = 0.33, wd_we_type = 1)
# # PMK_Luftfritteuse.windows([660,780],[1140,1260], 0.1)

# # PMK_Herd = PMK.Appliance(PMK,1,1800,4,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
# # PMK_Herd.windows([540,600],[660,780],0.1,[900,1020],[1140,1260])
# # PMK_Herd.specific_cycle_1(1800,10,750,60,0.15)
# # PMK_Herd.cycle_behaviour([720,900],t0)

# # PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.6, wd_we_type = 1)
# # PMK_Spuelmaschine.windows([780,900],[1200,1320],0.1)

# # PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.48, wd_we_type = 1)
# # PMK_Waschmaschine.windows([540,720],[1020,1260],0.1)

# # PMK_Ofen = PMK.Appliance(PMK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2, wd_we_type = 1)
# # PMK_Ofen.windows([660,780],[1140,1260],0.1)

