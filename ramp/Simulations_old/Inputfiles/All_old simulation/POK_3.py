# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:39:01 2023

@author: rbala

This infut file is for Summer
"""

from ramp.core.core import User, np
User_list = []


POK = User("Paar Ohne Kind",3,3)
User_list.append(POK)


t0 = [0,0]
t1 = [390,450]   # 6:30 - 7:30
t11 = [1260,1380]# 21:00 - 23:00
t12 = [1260,1440]# 21:00 - 00:00
t2 = [1140,1380] # 19:00 - 23:00
t22 = [1140,1440]# 19:00 - 00:00
v1 = 0.1
v2 = 0.2
#%%'

# POK Weekdays

POK_bulb_living_1_1= POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
POK_bulb_living_1_1.windows(t1,t0,v1)

POK_bulb_living_1_2 = POK.Appliance(POK,1,10,1,90,0,90, wd_we_type = 0)
POK_bulb_living_1_2.windows(t11,t0,v1)

POK_bulb_kitchen_1= POK.Appliance(POK,1,10,1,15,0,15, wd_we_type = 0)
POK_bulb_kitchen_1.windows(t1,t0,v1)

POK_bulb_kitchen_2= POK.Appliance(POK,1,10,1,45,0,45, wd_we_type = 0)
POK_bulb_kitchen_2.windows([1200,1290],t0,v1)

POK_bulb1_bedroom_1= POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
POK_bulb1_bedroom_1.windows(t1,t0,v1)

POK_bulb1_bedroom_2= POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
POK_bulb1_bedroom_2.windows(t11,t0,v1)

# POK_bulb2_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb2_bedroom_1.windows(t1,t0,v1)

# POK_bulb2_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb2_bedroom_2.windows([960,1140],t0,v1)

POK_bulb2_bedroom_3 = POK.Appliance(POK,1,10,1,5,0,5, wd_we_type = 0)
POK_bulb2_bedroom_3.windows(t11,t0,v1)

# POK_bulb3_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb3_bedroom_1.windows(t1,t0,v1)

# POK_bulb3_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb3_bedroom_2.windows(t11,t0,v1)

POK_bulb_BT_hallway_1 = POK.Appliance(POK,2,10,1,5,0,5, wd_we_type = 0)
POK_bulb_BT_hallway_1.windows(t1,t0,v1)

POK_bulb_BT_hallway_2 = POK.Appliance(POK,2,10,1,15,0,15, wd_we_type = 0)
POK_bulb_BT_hallway_2.windows(t11,t0,v1)

# POK_outdoor_bulb_1 = POK.Appliance(POK,2,13,1,5,v1,5, wd_we_type = 0)  
# POK_outdoor_bulb_1.windows([0,330],t0,0)

POK_outdoor_bulb_2 = POK.Appliance(POK,1,13,1,5,0,5, wd_we_type = 0)   
POK_outdoor_bulb_2.windows(t12,t0,0)

                              ###

# POK_TV_1= POK.Appliance(POK,1,60,1,30,v1,30, wd_we_type = 0)
# POK_TV_1.windows([540,720],t0,v1)

# POK_TV_2= POK.Appliance(POK,1,60,1,30,v1,30, wd_we_type = 0)
# POK_TV_2.windows([840,1020],t0,v1)

POK_TV_3= POK.Appliance(POK,1,60,1,90,v1,90, wd_we_type = 0)
POK_TV_3.windows(t2,t0,v1)

POK_Phone_charger_1 = POK.Appliance(POK,2,5,1,45,v1,45, wd_we_type = 0)
POK_Phone_charger_1.windows([390,450],t0,0)

POK_Phone_charger_2 = POK.Appliance(POK,2,5,1,15,v1,15, wd_we_type = 0)
POK_Phone_charger_2.windows(t2,t0,v1)

POK_Laptop_PC_charger_1 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 0)
POK_Laptop_PC_charger_1.windows([390,450],t0,0)

# POK_Laptop_PC_charger_2 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 0)
# POK_Laptop_PC_charger_2.windows([840,1020],t0,0)

POK_Laptop_PC_charger_3 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 0)
POK_Laptop_PC_charger_3.windows(t2,t0,v1)

POK_Herd = POK.Appliance(POK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
POK_Herd.windows([420,540],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,5,0.15)
POK_Herd.cycle_behaviour([480,600],t0)

# POK_Herd = POK.Appliance(POK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# POK_Herd.windows([660,780],t0,v1)
# POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
# POK_Herd.cycle_behaviour([660,780],t0)

# POK_Herd = POK.Appliance(POK,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# POK_Herd.windows([900,1020],t0,v1)
# POK_Herd.specific_cycle_1(1800,10,0.15)
# POK_Herd.cycle_behaviour([900,1020],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
POK_Herd.windows([1140,1260],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour([1140,1260],t0)


# POK Weekends/Holidays


POK_bulb_living_1_1= POK.Appliance(POK,1,10,1,120,0,120, wd_we_type = 1)
POK_bulb_living_1_1.windows(t12,t0,v1)

# POK_bulb_living_1_2 = POK.Appliance(POK,2,10,1,150,0,150, wd_we_type = 1)
# POK_bulb_living_1_2.windows([1080,1440],t0,0)

# POK_bulb_kitchen_1 = POK.Appliance(POK,2,10,1,30,0,30, wd_we_type = 1)
# POK_bulb_kitchen_1.windows(t11,t0,v1)

# POK_bulb_kitchen_2 = POK.Appliance(POK,2,10,1,30,0,30, wd_we_type = 1)
# POK_bulb_kitchen_2.windows([960,1140],t0,v1)

POK_bulb_kitchen_3 = POK.Appliance(POK,1,10,1,60,0,60, wd_we_type = 1)
POK_bulb_kitchen_3.windows([1200,1290],t0,v1)

POK_bulb1_bedroom_1 = POK.Appliance(POK,1,10,1,60,0,60, wd_we_type = 1)
POK_bulb1_bedroom_1.windows(t12,t0,v1)

# POK_bulb1_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb1_bedroom_2.windows([1320,1440],t0,v1)

POK_bulb2_bedroom_1 = POK.Appliance(POK,1,10,1,5,0,5, wd_we_type = 1)
POK_bulb2_bedroom_1.windows(t12,t0,v1)

# POK_bulb2_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb2_bedroom_2.windows([1080,1320],t0,0)

# POK_bulb2_bedroom_3 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# POK_bulb3_bedroom_1 = POK.Appliance(POK,1,10,1,60,0,60, wd_we_type = 1)
# POK_bulb3_bedroom_1.windows(t12,t0,v1)

# POK_bulb3_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb3_bedroom_2.windows([1320,1440],t0,v1)

POK_bulb_BT_hallway_1 = POK.Appliance(POK,2,10,1,20,0,20, wd_we_type = 1)
POK_bulb_BT_hallway_1.windows(t12,t0,v1)

# POK_bulb_BT_hallway_2 = POK.Appliance(POK,4,10,1,20,0,10, wd_we_type = 1)
# POK_bulb_BT_hallway_2.windows([1080,1440],t0,0)

# POK_outdoor_bulb_1 = POK.Appliance(POK,1,13,1,5,0,5, wd_we_type = 1)   
# POK_outdoor_bulb_1.windows([0,330],t0,0)

POK_outdoor_bulb_2 = POK.Appliance(POK,1,13,1,5,0,5, wd_we_type = 1)  
POK_outdoor_bulb_2.windows(t12,t0,v1)

                              ###

POK_TV_1= POK.Appliance(POK,1,60,1,30,v1,30, wd_we_type = 1)
POK_TV_1.windows([540,720],t0,v1)

POK_TV_2= POK.Appliance(POK,1,60,1,30,v1,30, wd_we_type = 1)
POK_TV_2.windows([840,1020],t0,v1)

POK_TV_3= POK.Appliance(POK,1,60,1,60,v1,60, wd_we_type = 1)
POK_TV_3.windows(t22,t0,0)

POK_Phone_charger_1 = POK.Appliance(POK,2,5,1,45,v1,45, wd_we_type = 1)
POK_Phone_charger_1.windows([540,720],t0,v1)

POK_Phone_charger_2 = POK.Appliance(POK,2,5,1,15,v1,15, wd_we_type = 1)
POK_Phone_charger_2.windows(t22,t0,0)

POK_Laptop_PC_charger_1 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 1)
POK_Laptop_PC_charger_1.windows([540,720],t0,v1)

POK_Laptop_PC_charger_2 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 1)
POK_Laptop_PC_charger_2.windows([840,1020],t0,v1)

POK_Laptop_PC_charger_3 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 1)
POK_Laptop_PC_charger_3.windows(t22,t0,0)

POK_Herd = POK.Appliance(POK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([480,600],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,5,0.15)
POK_Herd.cycle_behaviour([480,600],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([660,780],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour([660,780],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([900,1020],t0,v1)
POK_Herd.specific_cycle_1(1800,10,0.15)
POK_Herd.cycle_behaviour([900,1020],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([1140,1260],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour([1140,1260],t0)


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


# POK Occasional used devices


POK_Mixer = POK.Appliance(POK,1,50,2,15,0,10, occasional_use = 0.5)
POK_Mixer.windows([420,540],[1140,1260],v1)

POK_Toaster = POK.Appliance(POK,1,1000,2,10,0,10, occasional_use = 0.6)
POK_Toaster.windows([420,540],[1140,1260],v1)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0,15,occasional_use = 0.5)
POK_Haartrockner.windows([420,720],[960,1260],v1)

POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0,15,occasional_use = 0.33)
POK_Luftfritteuse.windows([420,540],[1140,1260], v1)

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,120,0,60, thermal_P_var = 0.2, occasional_use= 0.33)
POK_Spuelmaschine.windows([780,900],[1200,1320],v1)

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33)
POK_Waschmaschine.windows([540,720],[1020,1260],v1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5)
POK_Ofen.windows([420,540],[1140,1260],v1)

























# t0 = [0,0]
# t1 = [330,420]   # 5:30 - 7:00
# t2 = [1260,1440] # 21:00 - 00:00
# t3 = [1260,1380] # 21:00 - 23:00
# #%%'
# # Paar ohne Kind

# POK_bulb_living_1_1 = POK.Appliance(POK,1,10,1,30,0,30)
# POK_bulb_living_1_1.windows(t1,t0,0.1)

# POK_bulb_living_1_2 = POK.Appliance(POK,1,10,1,90,0,90)
# POK_bulb_living_1_2.windows(t3,t0,0.1)

# POK_bulb_kitchen_1= POK.Appliance(POK,1,10,1,15,0,15)
# POK_bulb_kitchen_1.windows(t1,t0,0.1)

# POK_bulb_kitchen_2= POK.Appliance(POK,1,10,1,45,0,45)
# POK_bulb_kitchen_2.windows([1200,1290],t0,0.1)

# POK_bulb1_bedroom_1= POK.Appliance(POK,1,10,1,30,0,30)
# POK_bulb1_bedroom_1.windows(t1,t0,0.1)

# POK_bulb1_bedroom_2= POK.Appliance(POK,1,10,1,30,0,30)
# POK_bulb1_bedroom_2.windows(t2,t0,0)

# POK_bulb2_bedroom_1 = POK.Appliance(POK,1,10,1,5,0,5)
# POK_bulb2_bedroom_1.windows(t2,t0,0)

# # POK_bulb2_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30)
# # POK_bulb2_bedroom_2.windows([1140,1290],t0,0.1)

# POK_bulb_BT_hallway_1 = POK.Appliance(POK,2,10,1,5,0,5)
# POK_bulb_BT_hallway_1.windows(t1,t0,0.1)

# POK_bulb_BT_hallway_2 = POK.Appliance(POK,2,10,1,15,0,15)
# POK_bulb_BT_hallway_2.windows(t3,t0,0.1)

# # POK_outdoor_bulb_1 = POK.Appliance(POK,1,13,1,5,0.1,5)   # Meistens mit Bewegungssensor, deswegen nur 15 minuten
# # POK_outdoor_bulb_1.windows([0,510],t0,0)

# POK_outdoor_bulb_2 = POK.Appliance(POK,1,13,1,5,0.1,5)   
# POK_outdoor_bulb_2.windows([1290,1440],t0,0)

# POK_TV = POK.Appliance(POK,1,60,1,90,0.1,75)
# POK_TV.windows([1170,1380],t0,0.1)

# POK_router = POK.Appliance(POK,1,7,1,1440,0.1)
# POK_router.windows([0,1440],t0)

# POK_Phone_charger_1 = POK.Appliance(POK,2,5,1,45,0.1,45)
# POK_Phone_charger_1.windows([330,450],t0,0)

# POK_Phone_charger_2 = POK.Appliance(POK,2,5,1,15,0.1,15)
# POK_Phone_charger_2.windows([1170,1440],t0,0)

# POK_Laptop_PC_charger_1 = POK.Appliance(POK,2,50,1,30,0.05,30)
# POK_Laptop_PC_charger_1.windows([330,450],t0,0)

# POK_Laptop_PC_charger_2 = POK.Appliance(POK,2,50,1,30,0.05,30)
# POK_Laptop_PC_charger_2.windows([1170,1440],t0,0)

# POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3)
# POK_Kuehlschrank.windows([0,1440],[0,0])
# POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
# POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
# POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
# POK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3)
# POK_Tiefkuehl.windows([0,1440],[0,0])
# POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
# POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
# POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
# POK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# POK_Mixer = POK.Appliance(POK,1,50,2,15,0.1,1, occasional_use = 0.33)
# POK_Mixer.windows([360,480],[1140,1260],0.1)

# POK_Toaster = POK.Appliance(POK,1,1000,2,10,0.1,5, occasional_use = 0.5)
# POK_Toaster.windows([360,480],[1140,1260],0.1)

# POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0.1,5,occasional_use =0.5)
# POK_Haartrockner.windows([420,720],[960,1260],0.10)

# POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0.1,15,occasional_use = 0.33)
# POK_Luftfritteuse.windows([360,420],[1200,1260], 0.1)

# POK_Herd = POK.Appliance(POK,1,1800,2,60,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
# POK_Herd.windows([360,480],[1140,1260],0.1)
# POK_Herd.specific_cycle_1(1800,10,750,60,0.15)
# POK_Herd.cycle_behaviour([720,900],[0,0])

# POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,75,0.1,60, thermal_P_var = 0.2, occasional_use=0.6)
# POK_Spuelmaschine.windows([420,540],[1200,1320],0.1)

# POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.5)
# POK_Waschmaschine.windows([540,720],[1020,1260],0.1)

# POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2)
# POK_Ofen.windows([360,480],[1140,1260],0.1)

# #%%'
# # Paar ohne Kind
# # POK_bulb_living_1 = POK.Appliance(POK,1,10,1,60,0,60, wd_we_type = 1)
# # POK_bulb_living_1.windows([450,570],t0,0.1)

# # POK_bulb_living_2 = POK.Appliance(POK,1,10,1,120,0,120, wd_we_type = 1)
# # POK_bulb_living_2.windows(t2,t0,0.1)

# POK_bulb_living_3 = POK.Appliance(POK,1,10,1,120,0,120, wd_we_type = 1)
# POK_bulb_living_3.windows(t2,t0,0)

# # POK_bulb_kitchen_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# # POK_bulb_kitchen_1.windows([450,540],t0,0.1)

# # POK_bulb_kitchen_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# # POK_bulb_kitchen_2.windows([960,1080],t0,0)

# POK_bulb_kitchen_3 = POK.Appliance(POK,1,10,1,60,0,60, wd_we_type = 1)
# POK_bulb_kitchen_3.windows([1200,1290],t0,0.1)

# POK_bulb1_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb1_bedroom_1.windows(t1,t0,0.1)

# POK_bulb1_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb1_bedroom_2.windows(t2,t0,0)

# POK_bulb2_bedroom_1 = POK.Appliance(POK,1,10,1,5,0,5, wd_we_type = 1)
# POK_bulb2_bedroom_1.windows(t2,t0,0)

# # POK_bulb2_bedroom_2 = POK.Appliance(POK,1,10,1,15,0,15, wd_we_type = 1)
# # POK_bulb2_bedroom_2.windows([960,1290],t0,0)

# POK_bulb_BT_hallway_1 = POK.Appliance(POK,2,10,1,5,0,5, wd_we_type = 1)
# POK_bulb_BT_hallway_1.windows(t1,t0,0.1)

# POK_bulb_BT_hallway_2 = POK.Appliance(POK,2,10,1,15,0,15, wd_we_type = 1)
# POK_bulb_BT_hallway_2.windows(t3,t0,0.1)

# # POK_outdoor_bulb_1 = POK.Appliance(POK,1,13,1,10,0,10, wd_we_type = 1)   
# # POK_outdoor_bulb_1.windows([0,510],t0,0)

# POK_outdoor_bulb_2 = POK.Appliance(POK,1,13,1,5,0,5, wd_we_type = 1)  
# POK_outdoor_bulb_2.windows([1290,1440],t0,0)

# POK_TV_1= POK.Appliance(POK,1,60,1,30,0.1,30, wd_we_type = 1)
# POK_TV_1.windows([540,720],t0,0.1)

# POK_TV_2= POK.Appliance(POK,1,60,1,30,0.1,30, wd_we_type = 1)
# POK_TV_2.windows([900,1080],t0,0.1)

# POK_TV_3= POK.Appliance(POK,1,60,1,60,0.1,45, wd_we_type = 1)
# POK_TV_3.windows([1170,1440],t0,0)

# POK_router = POK.Appliance(POK,1,7,1,1440,0.1, wd_we_type = 1)
# POK_router.windows([0,1440],t0)

# POK_Phone_charger_1 = POK.Appliance(POK,2,5,1,45,0.1,45, wd_we_type = 1)
# POK_Phone_charger_1.windows([600,780],t0,0.1)

# POK_Phone_charger_2 = POK.Appliance(POK,2,5,1,15,0.1,15, wd_we_type = 1)
# POK_Phone_charger_2.windows([1170,1440],t0,0.1)

# POK_Laptop_PC_charger_1 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 1)
# POK_Laptop_PC_charger_1.windows([600,780],t0,0.1)

# POK_Laptop_PC_charger_2 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 1)
# POK_Laptop_PC_charger_2.windows([840,1020],t0,0.1)

# POK_Laptop_PC_charger_3 = POK.Appliance(POK,2,50,1,30,0.05,30, wd_we_type = 1)
# POK_Laptop_PC_charger_3.windows([1170,1440],t0,0)

# POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3, wd_we_type = 1)
# POK_Kuehlschrank.windows([0,1440],[0,0])
# POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
# POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
# POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
# POK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3, wd_we_type = 1)
# POK_Tiefkuehl.windows([0,1440],[0,0])
# POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
# POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
# POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
# POK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# POK_Mixer = POK.Appliance(POK,1,50,2,15,0.1,1, occasional_use = 0.33, wd_we_type = 1)
# POK_Mixer.windows([660,750],[1140,1260],0.1)

# POK_Toaster = POK.Appliance(POK,1,1000,2,10,0.1,3, occasional_use = 0.5, wd_we_type = 1)
# POK_Toaster.windows([540,600],[900,1080],0.1)

# POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0.1,5,occasional_use =0.5, wd_we_type = 1)
# POK_Haartrockner.windows([420,720],[960,1260],0.10)

# POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0.1,1,occasional_use = 0.33, wd_we_type = 1)
# POK_Luftfritteuse.windows([660,780],[1140,1260], 0.1)

# POK_Herd = POK.Appliance(POK,1,1800,4,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
# POK_Herd.windows([540,600],[660,780],0.1,[900,1020],[1140,1260])
# POK_Herd.specific_cycle_1(1800,10,750,60,0.15)
# POK_Herd.cycle_behaviour([720,900],[0,0])

# POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.6, wd_we_type = 1)
# POK_Spuelmaschine.windows([780,900],[1200,1320],0.1)

# POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.5, wd_we_type = 1)
# POK_Waschmaschine.windows([540,720],[1020,1260],0.1)

# POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2, wd_we_type = 1)
# POK_Ofen.windows([660,780],[1140,1260],0.1)