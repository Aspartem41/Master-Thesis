# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:30:44 2023

@author: Romit
"""


from ramp.core.core import User, np
User_list = []


EP = User("Einpersonen",10,3)
User_list.append(EP)

# Windows for Lights and Charging/TV
t0 = [0,0]
t1 = [390,450]    # 6:30 - 7:30
t11 = [390,510]   # 6:30 - 8:30
t12 = [1260,1440] # 21:00 - 00:00
t22 = [1140,1440] # 19:00 - 00:00
tk = [1200,1290]  # 20:00 - 21:30
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
#%%'

# EP Weekdays

EP_bulb_living = EP.Appliance(EP,1,10,1,30,0.5,30, wd_we_type = 0)
EP_bulb_living.windows(t1,t0,v1)

EP_bulb_living = EP.Appliance(EP,1,10,1,90,0.5,90, wd_we_type = 0)
EP_bulb_living.windows(t12,t0,v1)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,15,v1,15, wd_we_type = 0)
EP_bulb_kitchen.windows(t1,t0,v1)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,45,v1,45, wd_we_type = 0)
EP_bulb_kitchen.windows(tk,t0,v1)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,1,30,v1,30, wd_we_type = 0)
EP_bulb1_bedroom.windows(t1,t0,v1)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,1,30,v1,30, wd_we_type = 0)
EP_bulb1_bedroom.windows(t12,t0,v1)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,1,5,0.25,5, wd_we_type = 0)
EP_bulb_BT_hallway.windows(t1,t0,v1)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,1,25,0.25,25, wd_we_type = 0)
EP_bulb_BT_hallway.windows(t12,t0,v1)

EP_outdoor_bulb = EP.Appliance(EP,1,13,1,5,v1,5, wd_we_type = 0)   
EP_outdoor_bulb.windows(t12,t0,0)

                              ###

# EP_TV = EP.Appliance(EP,1,60,1,90,v1,90, wd_we_type = 0)
# EP_TV.windows(t22,t0,v1)

# EP_Phone_charger = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 0)
# EP_Phone_charger.windows(t11,t0,0)

# EP_Phone_charger = EP.Appliance(EP,1,5,1,15,v1,15, wd_we_type = 0)
# EP_Phone_charger.windows(t22,t0,v1)

# EP_Laptop_PC_charger = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
# EP_Laptop_PC_charger.windows(t11,t0,0)

# EP_Laptop_PC_charger = EP.Appliance(EP,1,50,1,30,v1,30, wd_we_type = 0)
# EP_Laptop_PC_charger.windows(t22,t0,v1)

# EP_Herd = EP.Appliance(EP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# EP_Herd.windows(tc0,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
# EP_Herd.cycle_behaviour(tc0,t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# EP_Herd.windows(tc2,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# EP_Herd.cycle_behaviour(tc2,t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# EP_Herd.windows(tc3,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,0.15)
# EP_Herd.cycle_behaviour(tc3,t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
# EP_Herd.windows(tc4,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# EP_Herd.cycle_behaviour(tc4,t0)


# EP Weekends/Holidays


EP_bulb_living = EP.Appliance(EP,1,10,2,120,0.5,120, wd_we_type = 1)
EP_bulb_living.windows(t12,th,v1)

EP_bulb_kitchen = EP.Appliance(EP,1,10,1,60,v1,60, wd_we_type = 1)
EP_bulb_kitchen.windows(tk,t0,v1)

EP_bulb1_bedroom = EP.Appliance(EP,1,10,2,60,v1,60, wd_we_type = 1)
EP_bulb1_bedroom.windows(t12,th,v1)

EP_bulb_BT_hallway = EP.Appliance(EP,1,10,2,30,0.25,30, wd_we_type = 1)
EP_bulb_BT_hallway.windows(t12,th,v1)

EP_outdoor_bulb = EP.Appliance(EP,1,13,2,5,v1,5, wd_we_type = 1)  
EP_outdoor_bulb.windows(t12,th,v1)

                              ###
                              

# EP_TV = EP.Appliance(EP,1,60,1,60,v2,60, wd_we_type = 1)
# EP_TV.windows(tc3,t0,v1)

# EP_TV = EP.Appliance(EP,1,60,2,60,v2,60, wd_we_type = 1)
# EP_TV.windows(t22,th,0)

# EP_Phone_charger = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 1)
# EP_Phone_charger.windows(tm0,t0,v1)

# EP_Phone_charger = EP.Appliance(EP,1,5,2,15,v1,15, wd_we_type = 1)
# EP_Phone_charger.windows(t22,th,0)

# EP_Laptop_PC_charger = EP.Appliance(EP,1,50,1,30,v2,30, wd_we_type = 1)
# EP_Laptop_PC_charger.windows(tm0,t0,v1)

# EP_Laptop_PC_charger = EP.Appliance(EP,1,50,2,30,v2,30, wd_we_type = 1)
# EP_Laptop_PC_charger.windows(t22,th,0)

# EP_Herd = EP.Appliance(EP,1,1800,1,15,v2,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# EP_Herd.windows(tc1,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
# EP_Herd.cycle_behaviour(tc1,t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# EP_Herd.windows(tc2,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# EP_Herd.cycle_behaviour(tc2,t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,10,v2,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# EP_Herd.windows(tc3,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,0.15)
# EP_Herd.cycle_behaviour(tc3,t0)

# EP_Herd = EP.Appliance(EP,1,1800,1,45,v2,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
# EP_Herd.windows(tc4,t0,v1)
# EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
# EP_Herd.cycle_behaviour(tc4,t0)


# # EP All time ON devices


# EP_router = EP.Appliance(EP,1,7,1,1440,0)
# EP_router.windows([0,1440],t0)

# EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3)
# EP_Kuehlschrank.windows([0,1440],t0)
# EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
# EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
# EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
# EP_Kuehlschrank.cycle_behaviour([480,1200],t0,[300,479],t0,[0,299],[1201,1440])


# # EP Occasional_use devices


# EP_Toaster = EP.Appliance(EP,1,1000,2,10,0,10, occasional_use = 0.5, wd_we_type = 0)
# EP_Toaster.windows(tc0,tc4,v1)

# EP_Toaster = EP.Appliance(EP,1,1000,4,10,0,10, occasional_use = 0.5, wd_we_type = 1)
# EP_Toaster.windows(tc1,tc2,v1,tc3,tc4)

# EP_Haartrockner = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5, wd_we_type = 0)
# EP_Haartrockner.windows([420,720],[960,1260],v1)

# EP_Haartrockner = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5, wd_we_type = 1)
# EP_Haartrockner.windows(tm0,[960,1260],v1)

# EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0,30, occasional_use = 0.33, wd_we_type = 0)
# EP_Luftfritteuse.windows(tc0,tc4,v1)

# EP_Luftfritteuse = EP.Appliance(EP,1,50,4,30,0,30, occasional_use = 0.33, wd_we_type = 1)
# EP_Luftfritteuse.windows(tc1,tc2,v1,tc3,tc4)

# EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
# EP_Spuelmaschine.windows([420,660],[1020,1320],v1)

# EP_Spuelmaschine = EP.Appliance(EP,1,1500,3,120,0,120, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
# EP_Spuelmaschine.windows(tc1,[780,960],v1,[1020,1320])

# EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 0)
# EP_Waschmaschine.windows(tc0,[1020,1260],v1)

# EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33, wd_we_type = 1)
# EP_Waschmaschine.windows(tm0,[1020,1260],v1)

# EP_Ofen = EP.Appliance(EP,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 0)
# EP_Ofen.windows(tc0,tc4,v1)

# EP_Ofen = EP.Appliance(EP,1,2150,4,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33, wd_we_type = 1)
# EP_Ofen.windows(tc1,tc2,v1,tc3,tc4)
