# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:35:32 2023

@author: Romit
"""


from ramp.core.core import User, np
User_list = []


MP = User("Mehrpersonen",10,3)
User_list.append(MP)

# Windows for Lights and Charging/TV
t0 = [0,0]
t1 = [390,510]    # 6:30 - 8:30
t11 = [450,510]   # 7:30 - 8:30
t_out = [0,510]   # 00:00 - 8:30
t2 = [1320,1440]  # 22:00 - 00:00
t22 = [1140,1440] # 19:00 - 00:00
th = [0,60]       # 00:00 - 1:00 (One hour of late night next day for weekend)

# Windows for Coocking devices and Machines
tc0 = [420,540]    # 7:00 - 9:00
tc1 = [540,660]    # 9:00 - 11:00
tc2 = [660,840]    # 11:00 - 14:00
tc3 = [840,1020]   # 14:00 - 17:00
tc4 = [1140,1260]  # 19:00 - 21:00
tm0 = [540,720]    # 9:00 - 12:00

# Variability factors 
v1 = 0.1
v2 = 0.4        
v3 = 0.16
#%%'

# MP Weekdays

MP_bulb_living = MP.Appliance(MP,4,10,1,30,v3,30, wd_we_type = 0)
MP_bulb_living.windows(t1,t0,v1)

MP_bulb_living = MP.Appliance(MP,4,10,1,150,v3,150, wd_we_type = 0)
MP_bulb_living.windows(t22,t0,0)

MP_bulb_kitchen = MP.Appliance(MP,2,10,1,30,v3,30, wd_we_type = 0)
MP_bulb_kitchen.windows(t1,t0,v1)

MP_bulb_kitchen = MP.Appliance(MP,2,10,1,70,v3,70, wd_we_type = 0)
MP_bulb_kitchen.windows(t22,t0,v1)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb1_bedroom.windows(t1,t0,v1)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb1_bedroom.windows(t2,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom.windows(t1,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb2_bedroom.windows(t2,t0,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb3_bedroom.windows(t1,t0,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 0)
MP_bulb3_bedroom.windows(t2,t0,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,1,10,0.25,10, wd_we_type = 0)
MP_bulb_BT_hallway.windows(t1,t0,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,1,20,0.25,10, wd_we_type = 0)
MP_bulb_BT_hallway.windows(t22,t0,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,1,5,v3,5, wd_we_type = 0)   
MP_outdoor_bulb.windows(t_out,t0,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,1,5,v3,5, wd_we_type = 0)   
MP_outdoor_bulb.windows(t22,t0,0)

                                ### 

# MP_TV = MP.Appliance(MP,2,60,1,30,v1,30, wd_we_type = 0)
# MP_TV.windows(tm0,t0,v1)

# MP_TV = MP.Appliance(MP,2,60,1,60,v1,60, wd_we_type = 0)
# MP_TV.windows(tc3,t0,v1)

# MP_TV = MP.Appliance(MP,2,60,1,60,v1,60, wd_we_type = 0)
# MP_TV.windows(t22,t0,v1)

# MP_Phone_charger = MP.Appliance(MP,5,5,1,45,v1,45, wd_we_type = 0)
# MP_Phone_charger.windows(t1,t0,0)

# MP_Phone_charger = MP.Appliance(MP,5,5,1,15,v1,15, wd_we_type = 0)
# MP_Phone_charger.windows(t22,t0,v1)

# MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
# MP_Laptop_PC_charger.windows(t1,t0,0)

# MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
# MP_Laptop_PC_charger.windows(tc3,t0,0)

# MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v1,30, wd_we_type = 0)
# MP_Laptop_PC_charger.windows(t22,t0,v1)

# MP_Herd = MP.Appliance(MP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# MP_Herd.windows(tc0,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,750,5,0.15)
# MP_Herd.cycle_behaviour(tc0,t0)

# MP_Herd = MP.Appliance(MP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# MP_Herd.windows(tc2,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# MP_Herd.cycle_behaviour(tc2,t0)

# MP_Herd = MP.Appliance(MP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# MP_Herd.windows(tc3,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,0.15)
# MP_Herd.cycle_behaviour(tc3,t0)

# MP_Herd = MP.Appliance(MP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# MP_Herd.windows(tc4,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# MP_Herd.cycle_behaviour(tc4,t0)


# MP Weekends/Holidays


MP_bulb_living = MP.Appliance(MP,4,10,1,30,v3,30, wd_we_type = 1)
MP_bulb_living.windows(t11,t0,v1)

MP_bulb_living = MP.Appliance(MP,4,10,2,150,v3,150, wd_we_type = 1)
MP_bulb_living.windows(t22,th,0)

MP_bulb_kitchen = MP.Appliance(MP,2,10,2,100,v3,100, wd_we_type = 1)
MP_bulb_kitchen.windows(t22,th,0)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb1_bedroom.windows(t11,t0,v1)

MP_bulb1_bedroom = MP.Appliance(MP,1,10,2,30,v3,30, wd_we_type = 1)
MP_bulb1_bedroom.windows(t2,th,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom.windows(t11,t0,v1)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom.windows([1140,1320],t0,0)

MP_bulb2_bedroom = MP.Appliance(MP,1,10,2,30,v3,30, wd_we_type = 1)
MP_bulb2_bedroom.windows(t2,th,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,1,30,v3,30, wd_we_type = 1)
MP_bulb3_bedroom.windows(t11,t0,v1)

MP_bulb3_bedroom = MP.Appliance(MP,1,10,2,30,v3,30, wd_we_type = 1)
MP_bulb3_bedroom.windows(t2,th,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,1,10,0.25,10, wd_we_type = 1)
MP_bulb_BT_hallway.windows(t11,t0,v1)

MP_bulb_BT_hallway = MP.Appliance(MP,3,10,2,20,0.25,10, wd_we_type = 1)
MP_bulb_BT_hallway.windows(t22,th,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,1,5,v3,5, wd_we_type = 1)   
MP_outdoor_bulb.windows(t_out,t0,0)

MP_outdoor_bulb = MP.Appliance(MP,2,13,2,15,v3,15, wd_we_type = 1)  
MP_outdoor_bulb.windows(t22,th,0)

                              ###

# MP_TV = MP.Appliance(MP,2,60,1,30,v2,30, wd_we_type = 1)
# MP_TV.windows(tm0,t0,v1)

# MP_TV = MP.Appliance(MP,2,60,1,30,v2,30, wd_we_type = 1)
# MP_TV.windows(tc3,t0,v1)

# MP_TV = MP.Appliance(MP,2,60,2,60,v2,45, wd_we_type = 1)
# MP_TV.windows(t22,th,0)

# MP_Phone_charger = MP.Appliance(MP,5,5,1,45,v1,45, wd_we_type = 1)
# MP_Phone_charger.windows(tm0,t0,v1)

# MP_Phone_charger = MP.Appliance(MP,5,5,2,15,v1,15, wd_we_type = 1)
# MP_Phone_charger.windows(t22,th,0)

# MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,30,v2,30, wd_we_type = 1)
# MP_Laptop_PC_charger.windows(tm0,t0,v1)

# MP_Laptop_PC_charger = MP.Appliance(MP,2,50,1,60,v2,60, wd_we_type = 1)
# MP_Laptop_PC_charger.windows(tc3,t0,v1)

# MP_Laptop_PC_charger = MP.Appliance(MP,2,50,2,30,v2,30, wd_we_type = 1)
# MP_Laptop_PC_charger.windows(t22,th,0)

# MP_Herd = MP.Appliance(MP,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# MP_Herd.windows(tc1,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,750,5,0.15)
# MP_Herd.cycle_behaviour(tc1,t0)

# MP_Herd = MP.Appliance(MP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# MP_Herd.windows(tc2,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# MP_Herd.cycle_behaviour(tc2,t0)

# MP_Herd = MP.Appliance(MP,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# MP_Herd.windows(tc3,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,0.15)
# MP_Herd.cycle_behaviour(tc3,t0)

# MP_Herd = MP.Appliance(MP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# MP_Herd.windows(tc4,t0,v1)
# MP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# MP_Herd.cycle_behaviour(tc4,t0)


# # MP All time ON devices


# MP_router = MP.Appliance(MP,1,7,1,1440,0)
# MP_router.windows([0,1440],t0)

# MP_Kuehlschrank = MP.Appliance(MP,1,150,1,1440,0,30,'yes',3)
# MP_Kuehlschrank.windows([0,1440],t0)
# MP_Kuehlschrank.specific_cycle_1(150,20,5,10)
# MP_Kuehlschrank.specific_cycle_2(150,15,5,15)
# MP_Kuehlschrank.specific_cycle_3(150,10,5,20)
# MP_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])

# MP_Tiefkuehl = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3)
# MP_Tiefkuehl.windows([0,1440],t0)
# MP_Tiefkuehl.specific_cycle_1(200,20,5,10)
# MP_Tiefkuehl.specific_cycle_2(200,15,5,15)
# MP_Tiefkuehl.specific_cycle_3(200,10,5,20)
# MP_Tiefkuehl.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# # MP Occasional_use devices


# MP_Mixer = MP.Appliance(MP,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 0)
# MP_Mixer.windows(tc0,tc2,v1,tc3,tc4)

# MP_Mixer = MP.Appliance(MP,1,50,4,15,0,15, occasional_use = 1, wd_we_type = 1)
# MP_Mixer.windows(tc1,tc2,v1,tc3,tc4)

# MP_Toaster = MP.Appliance(MP,1,1000,4,10,0,10, occasional_use = 1, wd_we_type = 0)
# MP_Toaster.windows(tc0,tc2,v1,tc3,tc4)

# MP_Toaster = MP.Appliance(MP,1,1000,4,10,0,10, occasional_use = 1, wd_we_type = 1)
# MP_Toaster.windows(tc1,tc2,v1,tc3,tc4)

# MP_Haartrockner = MP.Appliance(MP,1,1000,2,15,0,15, occasional_use = 1, wd_we_type = 0)
# MP_Haartrockner.windows([420,720],[960,1260],v1)

# MP_Haartrockner = MP.Appliance(MP,1,1000,2,15,0,15, occasional_use = 1, wd_we_type = 1)
# MP_Haartrockner.windows(tm0,[960,1260],v1)

# MP_Luftfritteuse = MP.Appliance(MP,1,50,4,30,0,30, occasional_use = 1, wd_we_type = 0)
# MP_Luftfritteuse.windows(tc0,tc2,v1,tc3,tc4)

# MP_Luftfritteuse = MP.Appliance(MP,1,50,4,30,0,30, occasional_use = 1, wd_we_type = 1)
# MP_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

# MP_Spuelmaschine = MP.Appliance(MP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 0)
# MP_Spuelmaschine.windows([420,660],[780,960],v1,[1020,1320])

# MP_Spuelmaschine = MP.Appliance(MP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 1)
# MP_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

# MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 0)
# MP_Waschmaschine.windows(tc0,[1020,1260],v1)

# MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 1)
# MP_Waschmaschine.windows(tm0,[1020,1260],v1)

# MP_Ofen = MP.Appliance(MP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 0)
# MP_Ofen.windows(tc0,tc2,v1,tc3,tc4)

# MP_Ofen = MP.Appliance(MP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 1, wd_we_type = 1)
# MP_Ofen.windows(tc1,tc2,v1,tc3,tc4)