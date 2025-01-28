# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:53:07 2023

@author: vrush
"""

from ramp.core.core import User, np
User_list = []

EP = User("Einpersonen",38,3)
User_list.append(EP)

AE = User("Alleinerziehende",10,3)
User_list.append(AE)

POK = User("Paar Ohne Kind",31,3)
User_list.append(POK)

PMK = User("Paar Mit Kind",25,3)
User_list.append(PMK)

MP = User("Mehrpersonen",3,3)
User_list.append(MP)


t0 = [0,0]
t1 = [390,510]   # 6:30 - 8:30
t11 = [450,510]  # 7:30 - 8:30
t2 = [1140,1380] # 19:00 - 23:00
t22 = [1140,1440]# 19:00 - 00:00
v1 = 0.1
v2 = 0.4
v3 = 0.16
#%%

# EP Weekdays

EP_bulb_living_1_1= EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 0)
EP_bulb_living_1_1.windows(t1,t0,v1)

EP_bulb_living_1_2 = EP.Appliance(EP,1,10,1,150,v3,150, wd_we_type = 0)
EP_bulb_living_1_2.windows(t2,t0,0)

EP_bulb_kitchen_1= EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 0)
EP_bulb_kitchen_1.windows(t1,t0,v1)

EP_bulb_kitchen_2= EP.Appliance(EP,1,10,1,70,v3,70, wd_we_type = 0)
EP_bulb_kitchen_2.windows(t2,t0,v1)

EP_bulb1_bedroom_1= EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 0)
EP_bulb1_bedroom_1.windows(t1,t0,v1)

EP_bulb1_bedroom_2= EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 0)
EP_bulb1_bedroom_2.windows([1320,1380],t0,v1)

# EP_bulb2_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb2_bedroom_1.windows(t1,t0,v1)

# EP_bulb2_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb2_bedroom_2.windows([960,1140],t0,v1)

# EP_bulb2_bedroom_3 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb2_bedroom_3.windows([1320,1380],t0,v1)

# EP_bulb3_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb3_bedroom_1.windows(t1,t0,v1)

# EP_bulb3_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb3_bedroom_2.windows([1320,1380],t0,v1)

EP_bulb_BT_hallway_1 = EP.Appliance(EP,1,10,1,30,0.25,15, wd_we_type = 0)
EP_bulb_BT_hallway_1.windows(t1,t0,v1)

EP_bulb_BT_hallway_2 = EP.Appliance(EP,1,10,1,30,0.25,15, wd_we_type = 0)
EP_bulb_BT_hallway_2.windows(t2,t0,0)

EP_outdoor_bulb_1 = EP.Appliance(EP,1,13,1,5,v3,5, wd_we_type = 0)  
EP_outdoor_bulb_1.windows([0,510],t0,0)

EP_outdoor_bulb_2 = EP.Appliance(EP,1,13,1,5,v3,5, wd_we_type = 0)   
EP_outdoor_bulb_2.windows(t22,t0,0)

                        ###

# EP_TV_1= EP.Appliance(EP,1,60,1,30,v1,30, wd_we_type = 0)
# EP_TV_1.windows([540,720],t0,v1)

# EP_TV_2= EP.Appliance(EP,1,60,1,30,v1,30, wd_we_type = 0)
# EP_TV_2.windows([840,1020],t0,v1)

EP_TV_3= EP.Appliance(EP,1,60,1,90,v1,90, wd_we_type = 0)
EP_TV_3.windows(t2,t0,v1)

EP_Phone_charger_1 = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 0)
EP_Phone_charger_1.windows([390,450],t0,0)

EP_Phone_charger_2 = EP.Appliance(EP,1,5,1,15,v1,15, wd_we_type = 0)
EP_Phone_charger_2.windows(t2,t0,v1)

EP_Laptop_PC_charger_1 = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
EP_Laptop_PC_charger_1.windows([390,450],t0,0)

# EP_Laptop_PC_charger_2 = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
# EP_Laptop_PC_charger_2.windows([840,1020],t0,0)

EP_Laptop_PC_charger_3 = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
EP_Laptop_PC_charger_3.windows(t2,t0,v1)

EP_Herd = EP.Appliance(EP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
EP_Herd.windows([420,540],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
EP_Herd.cycle_behaviour([420,540],t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# EP_Herd.windows([660,780],t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# EP_Herd.cycle_behaviour([660,780],t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# EP_Herd.windows([900,1020],t0,v1)
# EP_Herd.specific_cycle_1(1800,10,0.15)
# EP_Herd.cycle_behaviour([900,1020],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
EP_Herd.windows([1140,1260],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour([1140,1260],t0)


# EP Weekends/Holidays


EP_bulb_living_1_1= EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 1)
EP_bulb_living_1_1.windows(t11,t0,v1)

EP_bulb_living_1_2 = EP.Appliance(EP,1,10,1,150,v3,150, wd_we_type = 1)
EP_bulb_living_1_2.windows(t22,t0,0)

# EP_bulb_kitchen_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb_kitchen_1.windows(t11,t0,v1)

# EP_bulb_kitchen_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb_kitchen_2.windows([960,1140],t0,v1)

EP_bulb_kitchen_3 = EP.Appliance(EP,1,10,1,100,v3,100, wd_we_type = 1)
EP_bulb_kitchen_3.windows(t22,t0,0)

EP_bulb1_bedroom_1 = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 1)
EP_bulb1_bedroom_1.windows(t11,t0,v1)

EP_bulb1_bedroom_2 = EP.Appliance(EP,1,10,1,30,v3,30, wd_we_type = 1)
EP_bulb1_bedroom_2.windows([1320,1440],t0,v1)

# EP_bulb2_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb2_bedroom_1.windows(t11,t0,v1)

# EP_bulb2_bedroom_2 = EP.Appliance(EP,1,10,1,60,0,60, wd_we_type = 1)
# EP_bulb2_bedroom_2.windows([960,1320],t0,0)

# EP_bulb2_bedroom_3 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# EP_bulb3_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb3_bedroom_1.windows(t11,t0,v1)

# EP_bulb3_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb3_bedroom_2.windows([1320,1440],t0,v1)

EP_bulb_BT_hallway_1 = EP.Appliance(EP,1,10,1,30,0.25,15, wd_we_type = 1)
EP_bulb_BT_hallway_1.windows(t11,t0,v1)

EP_bulb_BT_hallway_2 = EP.Appliance(EP,1,10,1,30,0.25,15, wd_we_type = 1)
EP_bulb_BT_hallway_2.windows(t22,t0,0)

EP_outdoor_bulb_1 = EP.Appliance(EP,1,13,1,5,v3,5, wd_we_type = 1)   
EP_outdoor_bulb_1.windows([0,510],t0,0)

EP_outdoor_bulb_2 = EP.Appliance(EP,1,13,1,10,v3,10, wd_we_type = 1)  
EP_outdoor_bulb_2.windows(t22,t0,0)

                                ###

# EP_TV_1= EP.Appliance(EP,1,60,1,30,v1,30, wd_we_type = 1)
# EP_TV_1.windows([540,720],t0,v1)

EP_TV_2= EP.Appliance(EP,1,60,1,60,v2,60, wd_we_type = 1)
EP_TV_2.windows([840,1020],t0,v1)

EP_TV_3= EP.Appliance(EP,1,60,1,60,v2,60, wd_we_type = 1)
EP_TV_3.windows(t22,t0,0)

EP_Phone_charger_1 = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 1)
EP_Phone_charger_1.windows([540,720],t0,v1)

EP_Phone_charger_2 = EP.Appliance(EP,1,5,1,15,v1,15, wd_we_type = 1)
EP_Phone_charger_2.windows(t22,t0,0)

EP_Laptop_PC_charger_1 = EP.Appliance(EP,1,50,1,30,v2,30, wd_we_type = 1)
EP_Laptop_PC_charger_1.windows([540,720],t0,v1)

# EP_Laptop_PC_charger_2 = EP.Appliance(EP,1,50,1,60,v2,60, wd_we_type = 1)
# EP_Laptop_PC_charger_2.windows([840,1020],t0,v1)

EP_Laptop_PC_charger_3 = EP.Appliance(EP,1,50,1,30,v2,30, wd_we_type = 1)
EP_Laptop_PC_charger_3.windows(t22,t0,0)

EP_Herd = EP.Appliance(EP,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([540,600],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
EP_Herd.cycle_behaviour([540,600],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([660,780],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour([660,780],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([900,1020],t0,v1)
EP_Herd.specific_cycle_1(1800,10,0.15)
EP_Herd.cycle_behaviour([900,1020],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([1140,1260],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour([1140,1260],t0)


# EP All time ON devices


EP_router = EP.Appliance(EP,1,7,1,1440,0)
EP_router.windows([0,1440],t0)

EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3)
EP_Kuehlschrank.windows([0,1440],t0)
EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
EP_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# EP_Tiefkuehl = EP.Appliance(EP,1,200,1,1440,0,30,'yes',3)
# EP_Tiefkuehl.windows([0,1440],t0)
# EP_Tiefkuehl.specific_cycle_1(200,20,5,10)
# EP_Tiefkuehl.specific_cycle_2(200,15,5,15)
# EP_Tiefkuehl.specific_cycle_3(200,10,5,20)
# EP_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# EP Occasional_use devices


# EP_Mixer = EP.Appliance(EP,1,50,2,15,0,15, occasional_use = 1, wd_we_type = 0)
# EP_Mixer.windows([420,540],[1140,1260],v1)

# EP_Mixer_1 = EP.Appliance(EP,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 1)
# EP_Mixer_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

EP_Toaster = EP.Appliance(EP,1,1000,2,10,0,10, occasional_use = 0.5, wd_we_type = 0)
EP_Toaster.windows([420,540],[1140,1260],v1)

EP_Toaster_1 = EP.Appliance(EP,1,1000,4,10,0,10, occasional_use = 0.5, wd_we_type = 1)
EP_Toaster_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

EP_Haartrockner = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5, wd_we_type = 0)
EP_Haartrockner.windows([420,720],[960,1260],v1)

EP_Haartrockner_1 = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5, wd_we_type = 1)
EP_Haartrockner_1.windows([540,720],[960,1260],v1)

EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
EP_Luftfritteuse.windows([420,540],[1140,1260],v1)

EP_Luftfritteuse_1 = EP.Appliance(EP,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
EP_Luftfritteuse_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
EP_Spuelmaschine.windows([420,660],[1020,1320],v1)

EP_Spuelmaschine_1 = EP.Appliance(EP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
EP_Spuelmaschine_1.windows([540,660],[780,960],v1,[1020,1320])

EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
EP_Waschmaschine.windows([420,540],[1020,1260],v1)

EP_Waschmaschine_1 = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
EP_Waschmaschine_1.windows([540,720],[1020,1260],v1)

EP_Ofen = EP.Appliance(EP,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
EP_Ofen.windows([420,540],[1140,1260],v1)

EP_Ofen_1 = EP.Appliance(EP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
EP_Ofen_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])


#%%


# AE Weekdays

AE_bulb_living_1_1= AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb_living_1_1.windows(t1,t0,v1)

AE_bulb_living_1_2 = AE.Appliance(AE,1,10,1,150,v3,150, wd_we_type = 0)
AE_bulb_living_1_2.windows(t2,t0,0)

AE_bulb_kitchen_1= AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb_kitchen_1.windows(t1,t0,v1)

AE_bulb_kitchen_2= AE.Appliance(AE,1,10,1,70,v3,70, wd_we_type = 0)
AE_bulb_kitchen_2.windows(t2,t0,v1)

AE_bulb1_bedroom_1= AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
AE_bulb1_bedroom_1.windows(t1,t0,v1)

AE_bulb1_bedroom_2= AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 0)
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

AE_bulb_BT_hallway_1 = AE.Appliance(AE,1,10,1,30,0.25,15, wd_we_type = 0)
AE_bulb_BT_hallway_1.windows(t1,t0,v1)

AE_bulb_BT_hallway_2 = AE.Appliance(AE,1,10,1,30,0.25,15, wd_we_type = 0)
AE_bulb_BT_hallway_2.windows(t2,t0,0)

AE_outdoor_bulb_1 = AE.Appliance(AE,1,13,1,5,v3,5, wd_we_type = 0)   
AE_outdoor_bulb_1.windows([0,510],t0,0)

AE_outdoor_bulb_2 = AE.Appliance(AE,1,13,1,5,v3,5, wd_we_type = 0)   
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

AE_Laptop_PC_charger_1 = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
AE_Laptop_PC_charger_1.windows([390,450],t0,0)

# AE_Laptop_PC_charger_2 = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
# AE_Laptop_PC_charger_2.windows([840,1020],t0,0)

AE_Laptop_PC_charger_3 = AE.Appliance(AE,1,50,1,30,v1,30, wd_we_type = 0)
AE_Laptop_PC_charger_3.windows(t2,t0,v1)

AE_Herd = AE.Appliance(AE,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
AE_Herd.windows([420,540],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
AE_Herd.cycle_behaviour([420,540],t0)

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


AE_bulb_living_1_1= AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb_living_1_1.windows(t11,t0,v1)

AE_bulb_living_1_2 = AE.Appliance(AE,1,10,1,150,v3,150, wd_we_type = 1)
AE_bulb_living_1_2.windows(t22,t0,0)

# AE_bulb_kitchen_1 = AE.Appliance(AE,2,10,1,30,0,30, wd_we_type = 1)
# AE_bulb_kitchen_1.windows(t11,t0,v1)

# AE_bulb_kitchen_2 = AE.Appliance(AE,2,10,1,30,0,30, wd_we_type = 1)
# AE_bulb_kitchen_2.windows([960,1140],t0,v1)

AE_bulb_kitchen_3 = AE.Appliance(AE,1,10,1,100,v3,100, wd_we_type = 1)
AE_bulb_kitchen_3.windows(t22,t0,0)

AE_bulb1_bedroom_1 = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
AE_bulb1_bedroom_1.windows(t11,t0,v1)

AE_bulb1_bedroom_2 = AE.Appliance(AE,1,10,1,30,v3,30, wd_we_type = 1)
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

AE_bulb_BT_hallway_1 = AE.Appliance(AE,1,10,1,30,0.25,15, wd_we_type = 1)
AE_bulb_BT_hallway_1.windows(t11,t0,v1)

AE_bulb_BT_hallway_2 = AE.Appliance(AE,1,10,1,30,0.25,15, wd_we_type = 1)
AE_bulb_BT_hallway_2.windows(t22,t0,0)

AE_outdoor_bulb_1 = AE.Appliance(AE,1,13,1,5,v3,5, wd_we_type = 1)   
AE_outdoor_bulb_1.windows([0,510],t0,0)

AE_outdoor_bulb_2 = AE.Appliance(AE,1,13,1,15,v3,15, wd_we_type = 1)  
AE_outdoor_bulb_2.windows(t22,t0,0)

                              ###

AE_TV_1= AE.Appliance(AE,1,60,1,30,v2,30, wd_we_type = 1)
AE_TV_1.windows([540,720],t0,v1)

AE_TV_2= AE.Appliance(AE,1,60,1,30,v2,30, wd_we_type = 1)
AE_TV_2.windows([840,1020],t0,v1)

AE_TV_3= AE.Appliance(AE,1,60,1,60,v2,60, wd_we_type = 1)
AE_TV_3.windows(t22,t0,0)

AE_Phone_charger_1 = AE.Appliance(AE,2,5,1,45,v1,45, wd_we_type = 1)
AE_Phone_charger_1.windows([540,720],t0,v1)

AE_Phone_charger_2 = AE.Appliance(AE,2,5,1,15,v1,15, wd_we_type = 1)
AE_Phone_charger_2.windows(t22,t0,0)

AE_Laptop_PC_charger_1 = AE.Appliance(AE,1,50,1,30,v2,30, wd_we_type = 1)
AE_Laptop_PC_charger_1.windows([540,720],t0,v1)

# AE_Laptop_PC_charger_2 = AE.Appliance(AE,1,50,1,60,v1,60, wd_we_type = 1)
# AE_Laptop_PC_charger_2.windows([840,1020],t0,v1)

AE_Laptop_PC_charger_3 = AE.Appliance(AE,1,50,1,30,v2,30, wd_we_type = 1)
AE_Laptop_PC_charger_3.windows(t22,t0,0)

AE_Herd = AE.Appliance(AE,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([540,600],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,5,0.15)
AE_Herd.cycle_behaviour([540,600],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([660,780],t0,v1)
AE_Herd.specific_cycle_1(1800,10,750,35,0.15)
AE_Herd.cycle_behaviour([660,780],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
AE_Herd.windows([900,1020],t0,v1)
AE_Herd.specific_cycle_1(1800,10,0.15)
AE_Herd.cycle_behaviour([900,1020],t0)

AE_Herd = AE.Appliance(AE,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
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


# AE Occasional_use devices


# AE_Mixer = AE.Appliance(AE,1,50,2,15,0,15, occasional_use = 1, wd_we_type = 0)
# AE_Mixer.windows([420,540],[1140,1260],v1)

# AE_Mixer_1 = AE.Appliance(AE,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 1)
# AE_Mixer_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

AE_Toaster = AE.Appliance(AE,1,1000,2,10,0,10, occasional_use = 0.6, wd_we_type = 0)
AE_Toaster.windows([420,540],[1140,1260],v1)

AE_Toaster_1 = AE.Appliance(AE,1,1000,4,10,0,10, occasional_use = 0.6, wd_we_type = 1)
AE_Toaster_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

AE_Haartrockner = AE.Appliance(AE,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
AE_Haartrockner.windows([420,720],[960,1260],v1)

AE_Haartrockner_1 = AE.Appliance(AE,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
AE_Haartrockner_1.windows([540,720],[960,1260],v1)

AE_Luftfritteuse = AE.Appliance(AE,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
AE_Luftfritteuse.windows([420,540],[1140,1260],v1)

AE_Luftfritteuse_1 = AE.Appliance(AE,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
AE_Luftfritteuse_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
AE_Spuelmaschine.windows([420,660],[1020,1320],v1)

AE_Spuelmaschine_1 = AE.Appliance(AE,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
AE_Spuelmaschine_1.windows([540,660],[780,960],v1,[1020,1320])

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
AE_Waschmaschine.windows([420,540],[1020,1260],v1)

AE_Waschmaschine_1 = AE.Appliance(AE,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
AE_Waschmaschine_1.windows([540,720],[1020,1260],v1)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
AE_Ofen.windows([420,540],[1140,1260],v1)

AE_Ofen_1 = AE.Appliance(AE,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
AE_Ofen_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])


#%%

# POK Weekdays

POK_bulb_living_1_1= POK.Appliance(POK,2,10,1,30,v3,30, wd_we_type = 0)
POK_bulb_living_1_1.windows(t1,t0,v1)

POK_bulb_living_1_2 = POK.Appliance(POK,2,10,1,150,v3,150, wd_we_type = 0)
POK_bulb_living_1_2.windows(t2,t0,0)

POK_bulb_kitchen_1= POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 0)
POK_bulb_kitchen_1.windows(t1,t0,v1)

POK_bulb_kitchen_2= POK.Appliance(POK,1,10,1,70,v3,70, wd_we_type = 0)
POK_bulb_kitchen_2.windows(t2,t0,v1)

POK_bulb1_bedroom_1= POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 0)
POK_bulb1_bedroom_1.windows(t1,t0,v1)

POK_bulb1_bedroom_2= POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 0)
POK_bulb1_bedroom_2.windows([1320,1380],t0,v1)

# POK_bulb2_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb2_bedroom_1.windows(t1,t0,v1)

# POK_bulb2_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb2_bedroom_2.windows([960,1140],t0,v1)

POK_bulb2_bedroom_3 = POK.Appliance(POK,1,10,1,10,v3,10, wd_we_type = 0)
POK_bulb2_bedroom_3.windows([1140,1320],t0,v1)

# POK_bulb3_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb3_bedroom_1.windows(t1,t0,v1)

# POK_bulb3_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 0)
# POK_bulb3_bedroom_2.windows([1320,1380],t0,v1)

POK_bulb_BT_hallway_1 = POK.Appliance(POK,2,10,1,100,0.25,10, wd_we_type = 0)
POK_bulb_BT_hallway_1.windows(t1,t0,v1)

POK_bulb_BT_hallway_2 = POK.Appliance(POK,2,10,1,20,0.25,10, wd_we_type = 0)
POK_bulb_BT_hallway_2.windows(t2,t0,0)

POK_outdoor_bulb_1 = POK.Appliance(POK,1,13,1,5,v3,5, wd_we_type = 0)   
POK_outdoor_bulb_1.windows([0,510],t0,0)

POK_outdoor_bulb_2 = POK.Appliance(POK,1,13,1,5,v3,5, wd_we_type = 0)   
POK_outdoor_bulb_2.windows(t22,t0,0)

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

POK_Laptop_PC_charger_1 = POK.Appliance(POK,2,50,1,30,v1,30, wd_we_type = 0)
POK_Laptop_PC_charger_1.windows([390,450],t0,0)

# POK_Laptop_PC_charger_2 = POK.Appliance(POK,2,50,1,30,v1,30, wd_we_type = 0)
# POK_Laptop_PC_charger_2.windows([840,1020],t0,0)

POK_Laptop_PC_charger_3 = POK.Appliance(POK,2,50,1,30,v1,30, wd_we_type = 0)
POK_Laptop_PC_charger_3.windows(t2,t0,v1)

POK_Herd = POK.Appliance(POK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
POK_Herd.windows([420,540],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,5,0.15)
POK_Herd.cycle_behaviour([420,540],t0)

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


POK_bulb_living_1_1= POK.Appliance(POK,2,10,1,30,v3,30, wd_we_type = 1)
POK_bulb_living_1_1.windows(t11,t0,v1)

POK_bulb_living_1_2 = POK.Appliance(POK,2,10,1,150,v3,150, wd_we_type = 1)
POK_bulb_living_1_2.windows(t22,t0,0)

# POK_bulb_kitchen_1 = POK.Appliance(POK,2,10,1,30,0,30, wd_we_type = 1)
# POK_bulb_kitchen_1.windows(t11,t0,v1)

# POK_bulb_kitchen_2 = POK.Appliance(POK,2,10,1,30,0,30, wd_we_type = 1)
# POK_bulb_kitchen_2.windows([960,1140],t0,v1)

POK_bulb_kitchen_3 = POK.Appliance(POK,1,10,1,100,v3,100, wd_we_type = 1)
POK_bulb_kitchen_3.windows(t22,t0,0)

POK_bulb1_bedroom_1 = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 1)
POK_bulb1_bedroom_1.windows(t11,t0,v1)

POK_bulb1_bedroom_2 = POK.Appliance(POK,1,10,1,30,v3,30, wd_we_type = 1)
POK_bulb1_bedroom_2.windows([1320,1440],t0,v1)

# POK_bulb2_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb2_bedroom_1.windows(t11,t0,v1)

POK_bulb2_bedroom_2 = POK.Appliance(POK,1,10,1,10,v3,10, wd_we_type = 1)
POK_bulb2_bedroom_2.windows([1140,1320],t0,0)

# POK_bulb2_bedroom_3 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# POK_bulb3_bedroom_1 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb3_bedroom_1.windows(t11,t0,v1)

# POK_bulb3_bedroom_2 = POK.Appliance(POK,1,10,1,30,0,30, wd_we_type = 1)
# POK_bulb3_bedroom_2.windows([1320,1440],t0,v1)

POK_bulb_BT_hallway_1 = POK.Appliance(POK,2,10,1,10,0.25,10, wd_we_type = 1)
POK_bulb_BT_hallway_1.windows(t11,t0,v1)

POK_bulb_BT_hallway_2 = POK.Appliance(POK,2,10,1,20,0.25,10, wd_we_type = 1)
POK_bulb_BT_hallway_2.windows(t22,t0,0)

POK_outdoor_bulb_1 = POK.Appliance(POK,1,13,1,5,v3,5, wd_we_type = 1)   
POK_outdoor_bulb_1.windows([0,510],t0,0)

POK_outdoor_bulb_2 = POK.Appliance(POK,1,13,1,10,v3,10, wd_we_type = 1)  
POK_outdoor_bulb_2.windows(t22,t0,0)

                              ###

POK_TV_1= POK.Appliance(POK,1,60,1,30,v2,30, wd_we_type = 1)
POK_TV_1.windows([540,720],t0,v1)

POK_TV_2= POK.Appliance(POK,1,60,1,30,v2,30, wd_we_type = 1)
POK_TV_2.windows([840,1020],t0,v1)

POK_TV_3= POK.Appliance(POK,1,60,1,60,v2,60, wd_we_type = 1)
POK_TV_3.windows(t22,t0,0)

POK_Phone_charger_1 = POK.Appliance(POK,2,5,1,45,v1,45, wd_we_type = 1)
POK_Phone_charger_1.windows([540,720],t0,v1)

POK_Phone_charger_2 = POK.Appliance(POK,2,5,1,15,v1,15, wd_we_type = 1)
POK_Phone_charger_2.windows(t22,t0,0)

POK_Laptop_PC_charger_1 = POK.Appliance(POK,2,50,1,30,v2,30, wd_we_type = 1)
POK_Laptop_PC_charger_1.windows([540,720],t0,v1)

POK_Laptop_PC_charger_2 = POK.Appliance(POK,2,50,1,30,v2,30, wd_we_type = 1)
POK_Laptop_PC_charger_2.windows([840,1020],t0,v1)

POK_Laptop_PC_charger_3 = POK.Appliance(POK,2,50,1,30,v2,30, wd_we_type = 1)
POK_Laptop_PC_charger_3.windows(t22,t0,0)

POK_Herd = POK.Appliance(POK,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([540,600],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,5,0.15)
POK_Herd.cycle_behaviour([540,600],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([660,780],t0,v1)
POK_Herd.specific_cycle_1(1800,10,750,35,0.15)
POK_Herd.cycle_behaviour([660,780],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
POK_Herd.windows([900,1020],t0,v1)
POK_Herd.specific_cycle_1(1800,10,0.15)
POK_Herd.cycle_behaviour([900,1020],t0)

POK_Herd = POK.Appliance(POK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
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


# POK Occasional_use devices


POK_Mixer = POK.Appliance(POK,1,50,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
POK_Mixer.windows([420,540],[1140,1260],v1)

POK_Mixer_1 = POK.Appliance(POK,1,50,4,15,0,15, occasional_use = 0.5, wd_we_type = 1)
POK_Mixer_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

POK_Toaster = POK.Appliance(POK,1,1000,2,10,0,10, occasional_use = 0.6, wd_we_type = 0)
POK_Toaster.windows([420,540],[1140,1260],v1)

POK_Toaster_1 = POK.Appliance(POK,1,1000,4,10,0,10, occasional_use = 0.6, wd_we_type = 1)
POK_Toaster_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
POK_Haartrockner.windows([420,720],[960,1260],v1)

POK_Haartrockner_1 = POK.Appliance(POK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
POK_Haartrockner_1.windows([540,720],[960,1260],v1)

POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
POK_Luftfritteuse.windows([420,540],[1140,1260],v1)

POK_Luftfritteuse_1 = POK.Appliance(POK,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
POK_Luftfritteuse_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
POK_Spuelmaschine.windows([420,660],[1020,1320],v1)

POK_Spuelmaschine_1 = POK.Appliance(POK,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
POK_Spuelmaschine_1.windows([540,660],[780,960],v1,[1020,1320])

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
POK_Waschmaschine.windows([420,540],[1020,1260],v1)

POK_Waschmaschine_1 = POK.Appliance(POK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
POK_Waschmaschine_1.windows([540,720],[1020,1260],v1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
POK_Ofen.windows([420,540],[1140,1260],v1)

POK_Ofen_1 = POK.Appliance(POK,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
POK_Ofen_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])


#%%

# PMK Weekdays

PMK_bulb_living_1_1= PMK.Appliance(PMK,3,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb_living_1_1.windows(t1,t0,v1)

PMK_bulb_living_1_2 = PMK.Appliance(PMK,3,10,1,150,v3,150, wd_we_type = 0)
PMK_bulb_living_1_2.windows(t2,t0,0)

PMK_bulb_kitchen_1= PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb_kitchen_1.windows(t1,t0,v1)

PMK_bulb_kitchen_2= PMK.Appliance(PMK,1,10,1,70,v3,70, wd_we_type = 0)
PMK_bulb_kitchen_2.windows(t2,t0,v1)

PMK_bulb1_bedroom_1= PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb1_bedroom_1.windows(t1,t0,v1)

PMK_bulb1_bedroom_2= PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb1_bedroom_2.windows([1320,1380],t0,v1)

# PMK_bulb2_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
# PMK_bulb2_bedroom_1.windows(t1,t0,v1)

# PMK_bulb2_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
# PMK_bulb2_bedroom_2.windows([960,1140],t0,v1)

# PMK_bulb2_bedroom_3 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 0)
# PMK_bulb2_bedroom_3.windows([1320,1380],t0,v1)

PMK_bulb3_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb3_bedroom_1.windows(t1,t0,v1)

PMK_bulb3_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 0)
PMK_bulb3_bedroom_2.windows([1320,1380],t0,v1)

PMK_bulb_BT_hallway_1 = PMK.Appliance(PMK,2,10,1,10,0.25,10, wd_we_type = 0)
PMK_bulb_BT_hallway_1.windows(t1,t0,v1)

PMK_bulb_BT_hallway_2 = PMK.Appliance(PMK,2,10,1,20,0.25,10, wd_we_type = 0)
PMK_bulb_BT_hallway_2.windows(t2,t0,0)

PMK_outdoor_bulb_1 = PMK.Appliance(PMK,2,13,1,5,v3,5, wd_we_type = 0)   
PMK_outdoor_bulb_1.windows([0,510],t0,0)

PMK_outdoor_bulb_2 = PMK.Appliance(PMK,2,13,1,5,v3,5, wd_we_type = 0)   
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

PMK_Laptop_PC_charger_1 = PMK.Appliance(PMK,2,50,1,30,v1,30, wd_we_type = 0)
PMK_Laptop_PC_charger_1.windows([390,450],t0,0)

PMK_Laptop_PC_charger_2 = PMK.Appliance(PMK,2,50,1,30,v1,30, wd_we_type = 0)
PMK_Laptop_PC_charger_2.windows([840,1020],t0,0)

PMK_Laptop_PC_charger_3 = PMK.Appliance(PMK,2,50,1,30,v1,30, wd_we_type = 0)
PMK_Laptop_PC_charger_3.windows(t2,t0,v1)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
PMK_Herd.windows([420,540],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,5,0.15)
PMK_Herd.cycle_behaviour([420,540],t0)

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


PMK_bulb_living_1_1= PMK.Appliance(PMK,3,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb_living_1_1.windows(t11,t0,v1)

PMK_bulb_living_1_2 = PMK.Appliance(PMK,3,10,1,150,v3,150, wd_we_type = 1)
PMK_bulb_living_1_2.windows(t22,t0,0)

# PMK_bulb_kitchen_1 = PMK.Appliance(PMK,2,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb_kitchen_1.windows(t11,t0,v1)

# PMK_bulb_kitchen_2 = PMK.Appliance(PMK,2,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb_kitchen_2.windows([960,1140],t0,v1)

PMK_bulb_kitchen_3 = PMK.Appliance(PMK,1,10,1,100,v3,100, wd_we_type = 1)
PMK_bulb_kitchen_3.windows(t22,t0,0)

PMK_bulb1_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb1_bedroom_1.windows(t11,t0,v1)

PMK_bulb1_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb1_bedroom_2.windows([1320,1440],t0,v1)

PMK_bulb2_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb2_bedroom_1.windows(t11,t0,v1)

PMK_bulb2_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb2_bedroom_2.windows([1140,1320],t0,0)

PMK_bulb2_bedroom_3 = PMK.Appliance(PMK,1,10,1,30,v3,30, wd_we_type = 1)
PMK_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# PMK_bulb3_bedroom_1 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb3_bedroom_1.windows(t11,t0,v1)

# PMK_bulb3_bedroom_2 = PMK.Appliance(PMK,1,10,1,30,0,30, wd_we_type = 1)
# PMK_bulb3_bedroom_2.windows([1320,1440],t0,v1)

PMK_bulb_BT_hallway_1 = PMK.Appliance(PMK,2,10,1,10,0.25,10, wd_we_type = 1)
PMK_bulb_BT_hallway_1.windows(t11,t0,v1)

PMK_bulb_BT_hallway_2 = PMK.Appliance(PMK,2,10,1,20,0.25,10, wd_we_type = 1)
PMK_bulb_BT_hallway_2.windows(t22,t0,0)

PMK_outdoor_bulb_1 = PMK.Appliance(PMK,1,13,1,5,v3,5, wd_we_type = 1)   
PMK_outdoor_bulb_1.windows([0,510],t0,0)

PMK_outdoor_bulb_2 = PMK.Appliance(PMK,1,13,1,15,v3,15, wd_we_type = 1)  
PMK_outdoor_bulb_2.windows(t22,t0,0)

                              ###

PMK_TV_1= PMK.Appliance(PMK,1,60,1,30,v2,30, wd_we_type = 1)
PMK_TV_1.windows([540,720],t0,v1)

PMK_TV_2= PMK.Appliance(PMK,1,60,1,30,v2,30, wd_we_type = 1)
PMK_TV_2.windows([840,1020],t0,v1)

PMK_TV_3= PMK.Appliance(PMK,1,60,1,60,v2,60, wd_we_type = 1)
PMK_TV_3.windows(t22,t0,0)

PMK_Phone_charger_1 = PMK.Appliance(PMK,3,5,1,45,v1,45, wd_we_type = 1)
PMK_Phone_charger_1.windows([540,720],t0,v1)

PMK_Phone_charger_2 = PMK.Appliance(PMK,3,5,1,15,v1,15, wd_we_type = 1)
PMK_Phone_charger_2.windows(t22,t0,0)

PMK_Laptop_PC_charger_1 = PMK.Appliance(PMK,2,50,1,30,v2,30, wd_we_type = 1)
PMK_Laptop_PC_charger_1.windows([540,720],t0,v1)

PMK_Laptop_PC_charger_2 = PMK.Appliance(PMK,2,50,1,60,v2,60, wd_we_type = 1)
PMK_Laptop_PC_charger_2.windows([840,1020],t0,v1)

PMK_Laptop_PC_charger_3 = PMK.Appliance(PMK,2,50,1,30,v2,30, wd_we_type = 1)
PMK_Laptop_PC_charger_3.windows(t22,t0,0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([540,600],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,5,0.15)
PMK_Herd.cycle_behaviour([540,600],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([660,780],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,750,35,0.15)
PMK_Herd.cycle_behaviour([660,780],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
PMK_Herd.windows([900,1020],t0,v1)
PMK_Herd.specific_cycle_1(1800,10,0.15)
PMK_Herd.cycle_behaviour([900,1020],t0)

PMK_Herd = PMK.Appliance(PMK,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
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


# PMK Occasional_use devices


PMK_Mixer = PMK.Appliance(PMK,1,50,3,15,0,15, occasional_use = 0.7, wd_we_type = 0)
PMK_Mixer.windows([420,540],[900,1020],v1,[1140,1260])

PMK_Mixer_1 = PMK.Appliance(PMK,1,50,4,15,0,15, occasional_use = 0.7, wd_we_type = 1)
PMK_Mixer_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

PMK_Toaster = PMK.Appliance(PMK,1,1000,3,10,0,10, occasional_use = 0.8, wd_we_type = 0)
PMK_Toaster.windows([420,540],[900,1020],v1,[1140,1260])

PMK_Toaster_1 = PMK.Appliance(PMK,1,1000,4,10,0,10, occasional_use = 0.8, wd_we_type = 1)
PMK_Toaster_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 0)
PMK_Haartrockner.windows([420,720],[960,1260],v1)

PMK_Haartrockner_1 = PMK.Appliance(PMK,1,1000,2,15,0,15, occasional_use = 0.5, wd_we_type = 1)
PMK_Haartrockner_1.windows([540,720],[960,1260],v1)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,3,30,0,30, occasional_use = 0.5, wd_we_type = 0)
PMK_Luftfritteuse.windows([420,540],[900,1020],v1,[1140,1260])

PMK_Luftfritteuse_1 = PMK.Appliance(PMK,1,50,4,30,0,30, occasional_use = 0.5, wd_we_type = 1)
PMK_Luftfritteuse_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
PMK_Spuelmaschine.windows([420,660],[1020,1320],v1)

PMK_Spuelmaschine_1 = PMK.Appliance(PMK,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
PMK_Spuelmaschine_1.windows([540,660],[780,960],v1,[1020,1320])

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.5, wd_we_type = 0)
PMK_Waschmaschine.windows([420,540],[1020,1260],v1)

PMK_Waschmaschine_1 = PMK.Appliance(PMK,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.5, wd_we_type = 1)
PMK_Waschmaschine_1.windows([540,720],[1020,1260],v1)

PMK_Ofen = PMK.Appliance(PMK,1,2150,3,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 0)
PMK_Ofen.windows([420,540],[900,1020],v1,[1140,1260])

PMK_Ofen_1 = PMK.Appliance(PMK,1,2150,3,60,0,60, thermal_P_var = 0.2, occasional_use= 0.5, wd_we_type = 1)
PMK_Ofen_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])


#%%

# MP Weekdays

MP_bulb_living_1_1= MP.Appliance(MP,4,10,1,30,v3,30, wd_we_type = 0)
MP_bulb_living_1_1.windows(t1,t0,v1)

MP_bulb_living_1_2 = MP.Appliance(MP,4,10,1,150,v3,150, wd_we_type = 0)
MP_bulb_living_1_2.windows(t2,t0,0)

MP_bulb_kitchen_1= MP.Appliance(MP,2,10,1,30,v3,30, wd_we_type = 0)
MP_bulb_kitchen_1.windows(t1,t0,v1)

MP_bulb_kitchen_2= MP.Appliance(MP,2,10,1,70,v3,70, wd_we_type = 0)
MP_bulb_kitchen_2.windows(t2,t0,v1)

MP_bulb1_bedroom_1= MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb1_bedroom_1.windows(t1,t0,v1)

MP_bulb1_bedroom_2= MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb1_bedroom_2.windows([1320,1380],t0,v1)

MP_bulb2_bedroom_1 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom_1.windows(t1,t0,v1)

# MP_bulb2_bedroom_2 = MP.Appliance(MP,1,10,1,30,0,30, wd_we_type = 0)
# MP_bulb2_bedroom_2.windows([960,1140],t0,v1)

MP_bulb2_bedroom_3 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom_3.windows([1320,1380],t0,v1)

MP_bulb3_bedroom_1 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb3_bedroom_1.windows(t1,t0,v1)

MP_bulb3_bedroom_2 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb3_bedroom_2.windows([1320,1380],t0,v1)

MP_bulb_BT_hallway_1 = MP.Appliance(MP,3,10,1,10,0.25,10, wd_we_type = 0)
MP_bulb_BT_hallway_1.windows(t1,t0,v1)

MP_bulb_BT_hallway_2 = MP.Appliance(MP,3,10,1,20,0.25,10, wd_we_type = 0)
MP_bulb_BT_hallway_2.windows(t2,t0,0)

MP_outdoor_bulb_1 = MP.Appliance(MP,2,13,1,5,v3,5, wd_we_type = 0)   
MP_outdoor_bulb_1.windows([0,510],t0,0)

MP_outdoor_bulb_2 = MP.Appliance(MP,2,13,1,5,v3,5, wd_we_type = 0)   
MP_outdoor_bulb_2.windows(t22,t0,0)

                                ### 

MP_TV_1= MP.Appliance(MP,2,60,1,30,v1,30, wd_we_type = 0)
MP_TV_1.windows([540,720],t0,v1)

MP_TV_2= MP.Appliance(MP,2,60,1,60,v1,60, wd_we_type = 0)
MP_TV_2.windows([840,1020],t0,v1)

MP_TV_3= MP.Appliance(MP,2,60,1,60,v1,60, wd_we_type = 0)
MP_TV_3.windows(t2,t0,v1)

MP_Phone_charger_1 = MP.Appliance(MP,5,5,1,45,v1,45, wd_we_type = 0)
MP_Phone_charger_1.windows([390,450],t0,0)

MP_Phone_charger_2 = MP.Appliance(MP,5,5,1,15,v1,15, wd_we_type = 0)
MP_Phone_charger_2.windows(t2,t0,v1)

MP_Laptop_PC_charger_1 = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
MP_Laptop_PC_charger_1.windows([390,450],t0,0)

MP_Laptop_PC_charger_2 = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
MP_Laptop_PC_charger_2.windows([840,1020],t0,0)

MP_Laptop_PC_charger_3 = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
MP_Laptop_PC_charger_3.windows(t2,t0,v1)

MP_Herd = MP.Appliance(MP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows([420,540],t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,5,0.15)
MP_Herd.cycle_behaviour([420,540],t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows([660,780],t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour([660,780],t0)

MP_Herd = MP.Appliance(MP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows([900,1020],t0,v1)
MP_Herd.specific_cycle_1(1800,10,0.15)
MP_Herd.cycle_behaviour([900,1020],t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
MP_Herd.windows([1140,1260],t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour([1140,1260],t0)


# MP Weekends/Holidays


MP_bulb_living_1_1= MP.Appliance(MP,4,10,1,30,v3,30, wd_we_type = 1)
MP_bulb_living_1_1.windows(t11,t0,v1)

MP_bulb_living_1_2 = MP.Appliance(MP,4,10,1,150,v3,150, wd_we_type = 1)
MP_bulb_living_1_2.windows(t22,t0,0)

# MP_bulb_kitchen_1 = MP.Appliance(MP,2,10,1,30,0,30, wd_we_type = 1)
# MP_bulb_kitchen_1.windows(t11,t0,v1)

# MP_bulb_kitchen_2 = MP.Appliance(MP,2,10,1,30,0,30, wd_we_type = 1)
# MP_bulb_kitchen_2.windows([960,1140],t0,v1)

MP_bulb_kitchen_3 = MP.Appliance(MP,2,10,1,100,v3,100, wd_we_type = 1)
MP_bulb_kitchen_3.windows(t22,t0,0)

MP_bulb1_bedroom_1 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb1_bedroom_1.windows(t11,t0,v1)

MP_bulb1_bedroom_2 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb1_bedroom_2.windows([1320,1440],t0,v1)

MP_bulb2_bedroom_1 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom_1.windows(t11,t0,v1)

MP_bulb2_bedroom_2 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom_2.windows([1140,1320],t0,0)

MP_bulb2_bedroom_3 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom_3.windows([1320,1440],t0,v1)

MP_bulb3_bedroom_1 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb3_bedroom_1.windows(t11,t0,v1)

MP_bulb3_bedroom_2 = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb3_bedroom_2.windows([1320,1440],t0,v1)

MP_bulb_BT_hallway_1 = MP.Appliance(MP,3,10,1,10,0.25,10, wd_we_type = 1)
MP_bulb_BT_hallway_1.windows(t11,t0,v1)

MP_bulb_BT_hallway_2 = MP.Appliance(MP,3,10,1,20,0.25,10, wd_we_type = 1)
MP_bulb_BT_hallway_2.windows(t22,t0,0)

MP_outdoor_bulb_1 = MP.Appliance(MP,2,13,1,5,v3,5, wd_we_type = 1)   
MP_outdoor_bulb_1.windows([0,510],t0,0)

MP_outdoor_bulb_2 = MP.Appliance(MP,2,13,1,15,v3,15, wd_we_type = 1)  
MP_outdoor_bulb_2.windows(t22,t0,0)

                              ###

MP_TV_1= MP.Appliance(MP,2,60,1,30,v2,30, wd_we_type = 1)
MP_TV_1.windows([540,720],t0,v1)

MP_TV_2= MP.Appliance(MP,2,60,1,30,v2,30, wd_we_type = 1)
MP_TV_2.windows([840,1020],t0,v1)

MP_TV_3= MP.Appliance(MP,2,60,1,60,v2,45, wd_we_type = 1)
MP_TV_3.windows(t22,t0,0)

MP_Phone_charger_1 = MP.Appliance(MP,5,5,1,45,v1,45, wd_we_type = 1)
MP_Phone_charger_1.windows([540,720],t0,v1)

MP_Phone_charger_2 = MP.Appliance(MP,5,5,1,15,v1,15, wd_we_type = 1)
MP_Phone_charger_2.windows(t22,t0,0)

MP_Laptop_PC_charger_1 = MP.Appliance(MP,2,50,1,30,v2,30, wd_we_type = 1)
MP_Laptop_PC_charger_1.windows([540,720],t0,v1)

MP_Laptop_PC_charger_2 = MP.Appliance(MP,2,50,1,60,v2,60, wd_we_type = 1)
MP_Laptop_PC_charger_2.windows([840,1020],t0,v1)

MP_Laptop_PC_charger_3 = MP.Appliance(MP,2,50,1,30,v2,30, wd_we_type = 1)
MP_Laptop_PC_charger_3.windows(t22,t0,0)

MP_Herd = MP.Appliance(MP,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows([540,600],t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,5,0.15)
MP_Herd.cycle_behaviour([540,600],t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows([660,780],t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour([660,780],t0)

MP_Herd = MP.Appliance(MP,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows([900,1020],t0,v1)
MP_Herd.specific_cycle_1(1800,10,0.15)
MP_Herd.cycle_behaviour([900,1020],t0)

MP_Herd = MP.Appliance(MP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
MP_Herd.windows([1140,1260],t0,v1)
MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
MP_Herd.cycle_behaviour([1140,1260],t0)


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
MP_Mixer.windows([420,540],[660,780],v1,[900,1020],[1140,1260])

MP_Mixer_1 = MP.Appliance(MP,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 1)
MP_Mixer_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

MP_Toaster = MP.Appliance(MP,1,1000,4,10,0,10, occasional_use = 1, wd_we_type = 0)
MP_Toaster.windows([420,540],[660,780],v1,[900,1020],[1140,1260])

MP_Toaster_1 = MP.Appliance(MP,1,1000,4,10,0,10, occasional_use = 1, wd_we_type = 1)
MP_Toaster_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

MP_Haartrockner = MP.Appliance(MP,1,1000,2,15,0,15, occasional_use = 1, wd_we_type = 0)
MP_Haartrockner.windows([420,720],[960,1260],v1)

MP_Haartrockner_1 = MP.Appliance(MP,1,1000,2,15,0,15, occasional_use = 1, wd_we_type = 1)
MP_Haartrockner_1.windows([540,720],[960,1260],v1)

MP_Luftfritteuse = MP.Appliance(MP,1,50,4,30,0,30, occasional_use = 1, wd_we_type = 0)
MP_Luftfritteuse.windows([420,540],[660,780],v1,[900,1020],[1140,1260])

MP_Luftfritteuse_1 = MP.Appliance(MP,1,50,4,30,0,30, occasional_use = 1, wd_we_type = 1)
MP_Luftfritteuse_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])

MP_Spuelmaschine = MP.Appliance(MP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 0)
MP_Spuelmaschine.windows([420,660],[780,960],v1,[1020,1320])

MP_Spuelmaschine_1 = MP.Appliance(MP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 1)
MP_Spuelmaschine_1.windows([540,660],[780,960],v1,[1020,1320])

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 0)
MP_Waschmaschine.windows([420,540],[1020,1260],v1)

MP_Waschmaschine_1 = MP.Appliance(MP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 1)
MP_Waschmaschine_1.windows([540,720],[1020,1260],v1)

MP_Ofen = MP.Appliance(MP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 0)
MP_Ofen.windows([420,540],[660,780],v1,[900,1020],[1140,1260])

MP_Ofen_1 = MP.Appliance(MP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 1)
MP_Ofen_1.windows([540,600],[660,780],v1,[900,1020],[1140,1260])
