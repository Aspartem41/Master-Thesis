# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:22:20 2023

@author: vrush
"""


from ramp.core.core import User, np
User_list = []


AE = User("Alleinerziehende",3,3)
User_list.append(AE)


t0 = [0,0]
t1 = [390,510]   # 6:30 - 8:30
t11 = [450,510]  # 7:30 - 8:30
t2 = [1140,1380] # 19:00 - 23:00
t22 = [1140,1440]# 19:00 - 00:00
v1 = 0.1
v2 = 0.2
#%%'

# AE Weekdays

AE_bulb_living_1_1= AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
AE_bulb_living_1_1.windows(t1,t0,v1)

AE_bulb_living_1_2 = AE.Appliance(AE,1,10,1,150,0,150, wd_we_type = 0)
AE_bulb_living_1_2.windows(t2,t0,0)

AE_bulb_kitchen_1= AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
AE_bulb_kitchen_1.windows(t1,t0,v1)

AE_bulb_kitchen_2= AE.Appliance(AE,1,10,1,70,0,70, wd_we_type = 0)
AE_bulb_kitchen_2.windows(t2,t0,v1)

AE_bulb1_bedroom_1= AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
AE_bulb1_bedroom_1.windows(t1,t0,v1)

AE_bulb1_bedroom_2= AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
AE_bulb1_bedroom_2.windows([1320,1380],t0,v1)

# AE_bulb2_bedroom_1 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
# AE_bulb2_bedroom_1.windows(t1,t0,v1)

# AE_bulb2_bedroom_2 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
# AE_bulb2_bedroom_2.windows([960,1140],t0,v1)

# AE_bulb2_bedroom_3 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
# AE_bulb2_bedroom_3.windows([1320,1380],t0,v1)

# AE_bulb3_bedroom_1 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
# AE_bulb3_bedroom_1.windows(t1,t0,v1)

# AE_bulb3_bedroom_2 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 0)
# AE_bulb3_bedroom_2.windows([1320,1380],t0,v1)

AE_bulb_BT_hallway_1 = AE.Appliance(AE,1,10,1,30,0,15, wd_we_type = 0)
AE_bulb_BT_hallway_1.windows(t1,t0,v1)

AE_bulb_BT_hallway_2 = AE.Appliance(AE,1,10,1,30,0,15, wd_we_type = 0)
AE_bulb_BT_hallway_2.windows(t2,t0,0)

AE_outdoor_bulb_1 = AE.Appliance(AE,1,13,1,5,0,5, wd_we_type = 0)   
AE_outdoor_bulb_1.windows([0,510],t0,0)

AE_outdoor_bulb_2 = AE.Appliance(AE,1,13,1,5,0,5, wd_we_type = 0)   
AE_outdoor_bulb_2.windows(t22,t0,0)

                                ### 

# AE_TV_1= AE.Appliance(AE,1,60,1,30,v1,30, wd_we_type = 0)
# AE_TV_1.windows([540,720],t0,v1)

# AE_TV_2= AE.Appliance(AE,1,60,1,30,v1,30, wd_we_type = 0)
# AE_TV_2.windows([840,1020],t0,v1)

AE_TV_3= AE.Appliance(AE,1,60,1,90,v1,90, wd_we_type = 0)
AE_TV_3.windows(t2,t0,v1)

AE_Phone_charger_1 = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 0)
AE_Phone_charger_1.windows([390,450],t0,0)

AE_Phone_charger_2 = AE.Appliance(AE,2,5,1,15,v1,15, wd_we_type = 0)
AE_Phone_charger_2.windows(t2,t0,v1)

AE_Laptop_PC_charger_1 = AE.Appliance(AE,1,50,1,30,0.05,30, wd_we_type = 0)
AE_Laptop_PC_charger_1.windows([390,450],t0,0)

# AE_Laptop_PC_charger_2 = AE.Appliance(AE,1,50,1,30,0.05,30, wd_we_type = 0)
# AE_Laptop_PC_charger_2.windows([840,1020],t0,0)

AE_Laptop_PC_charger_3 = AE.Appliance(AE,1,50,1,30,0.05,30, wd_we_type = 0)
AE_Laptop_PC_charger_3.windows(t2,t0,v1)

AE_Herd = AE.Appliance(AE,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
AE_Herd.windows([420,540],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
AE_Herd.cycle_behaviour([480,600],t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# AE_Herd.windows([660,780],t0,v1)
# AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
# AE_Herd.cycle_behaviour([660,780],t0)

# AE_Herd = AE.Appliance(AE,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# AE_Herd.windows([900,1020],t0,v1)
# AE_Herd.specific_cycle_1(1800,10,0.15)
# AE_Herd.cycle_behaviour([900,1020],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
AE_Herd.windows([1140,1260],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour([1140,1260],t0)


# AE Weekends/Holidays


AE_bulb_living_1_1= AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
AE_bulb_living_1_1.windows(t11,t0,v1)

AE_bulb_living_1_2 = AE.Appliance(AE,1,10,1,150,0,150, wd_we_type = 1)
AE_bulb_living_1_2.windows([1080,1440],t0,0)

# AE_bulb_kitchen_1 = AE.Appliance(AE,2,10,1,30,0,30, wd_we_type = 1)
# AE_bulb_kitchen_1.windows(t11,t0,v1)

# AE_bulb_kitchen_2 = AE.Appliance(AE,2,10,1,30,0,30, wd_we_type = 1)
# AE_bulb_kitchen_2.windows([960,1140],t0,v1)

AE_bulb_kitchen_3 = AE.Appliance(AE,1,10,1,100,0,100, wd_we_type = 1)
AE_bulb_kitchen_3.windows(t22,t0,v1)

AE_bulb1_bedroom_1 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
AE_bulb1_bedroom_1.windows(t11,t0,v1)

AE_bulb1_bedroom_2 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
AE_bulb1_bedroom_2.windows([1320,1440],t0,v1)

# AE_bulb2_bedroom_1 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
# AE_bulb2_bedroom_1.windows(t11,t0,v1)

# AE_bulb2_bedroom_2 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
# AE_bulb2_bedroom_2.windows([1080,1320],t0,0)

# AE_bulb2_bedroom_3 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
# AE_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# AE_bulb3_bedroom_1 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
# AE_bulb3_bedroom_1.windows(t11,t0,v1)

# AE_bulb3_bedroom_2 = AE.Appliance(AE,1,10,1,30,0,30, wd_we_type = 1)
# AE_bulb3_bedroom_2.windows([1320,1440],t0,v1)

AE_bulb_BT_hallway_1 = AE.Appliance(AE,1,10,1,30,0,15, wd_we_type = 1)
AE_bulb_BT_hallway_1.windows(t11,t0,v1)

AE_bulb_BT_hallway_2 = AE.Appliance(AE,1,10,1,30,0,15, wd_we_type = 1)
AE_bulb_BT_hallway_2.windows([1080,1440],t0,0)

AE_outdoor_bulb_1 = AE.Appliance(AE,1,13,1,5,0,5, wd_we_type = 1)   
AE_outdoor_bulb_1.windows([0,510],t0,0)

AE_outdoor_bulb_2 = AE.Appliance(AE,1,13,1,15,0,15, wd_we_type = 1)  
AE_outdoor_bulb_2.windows([1080,1440],t0,0)

                              ###

AE_TV_1= AE.Appliance(AE,1,60,1,30,v1,30, wd_we_type = 1)
AE_TV_1.windows([540,720],t0,v1)

AE_TV_2= AE.Appliance(AE,1,60,1,30,v1,30, wd_we_type = 1)
AE_TV_2.windows([840,1020],t0,v1)

AE_TV_3= AE.Appliance(AE,1,60,1,60,v1,60, wd_we_type = 1)
AE_TV_3.windows(t22,t0,0)

AE_Phone_charger_1 = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 1)
AE_Phone_charger_1.windows([540,720],t0,v1)

AE_Phone_charger_2 = AE.Appliance(AE,2,5,1,15,v1,15, wd_we_type = 1)
AE_Phone_charger_2.windows(t22,t0,0)

AE_Laptop_PC_charger_1 = AE.Appliance(AE,1,50,1,30,0.05,30, wd_we_type = 1)
AE_Laptop_PC_charger_1.windows([540,720],t0,v1)

# AE_Laptop_PC_charger_2 = AE.Appliance(AE,1,50,1,60,0.05,60, wd_we_type = 1)
# AE_Laptop_PC_charger_2.windows([840,1020],t0,v1)

AE_Laptop_PC_charger_3 = AE.Appliance(AE,1,50,1,30,0.05,30, wd_we_type = 1)
AE_Laptop_PC_charger_3.windows(t22,t0,0)

AE_Herd = AE.Appliance(AE,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([480,600],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
AE_Herd.cycle_behaviour([480,600],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([660,780],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour([660,780],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([900,1020],t0,v1)
AE_Herd.specific_cycle_1(1800,10,0.15)
AE_Herd.cycle_behaviour([900,1020],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([1140,1260],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour([1140,1260],t0)


# AE All time ON devices


AE_router = AE.Appliance(AE,1,7,1,1440,0)
AE_router.windows([0,1440],t0)

AE_Kuehlschrank = AE.Appliance(AE,1,150,1,1440,0,30,'yes',3)
AE_Kuehlschrank.windows([0,1440],t0)
AE_Kuehlschrank.specific_cycle_1(150,20,5,10)
AE_Kuehlschrank.specific_cycle_2(150,15,5,15)
AE_Kuehlschrank.specific_cycle_3(150,10,5,20)
AE_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# AE_Tiefkuehl = AE.Appliance(AE,1,200,1,1440,0,30,'yes',3)
# AE_Tiefkuehl.windows([0,1440],t0)
# AE_Tiefkuehl.specific_cycle_1(200,20,5,10)
# AE_Tiefkuehl.specific_cycle_2(200,15,5,15)
# AE_Tiefkuehl.specific_cycle_3(200,10,5,20)
# AE_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# AE Occasional used devices


# AE_Mixer = AE.Appliance(AE,1,50,2,15,0,10, occasional_use = 1)
# AE_Mixer.windows([420,540],[1140,1260],v1)

AE_Toaster = AE.Appliance(AE,1,1000,2,10,0,10, occasional_use = 0.6)
AE_Toaster.windows([420,540],[1140,1260],v1)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,15,0,15,occasional_use = 0.5)
AE_Haartrockner.windows([420,720],[960,1260],v1)

AE_Luftfritteuse = AE.Appliance(AE,1,50,2,30,0,15,occasional_use = 0.33)
AE_Luftfritteuse.windows([420,540],[1140,1260], v1)

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,120,0,60, thermal_P_var = 0.2, occasional_use= 0.33)
AE_Spuelmaschine.windows([780,900],[1200,1320],v1)

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33)
AE_Waschmaschine.windows([540,720],[1020,1260],v1)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5)
AE_Ofen.windows([420,540],[1140,1260],v1)

