# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:32:03 2023

@author: vrush
"""




from ramp.core.core import User, np
User_list = []


EP = User("Einpersonen",3,3)
User_list.append(EP)


t0 = [0,0]
t1 = [390,510]   # 6:30 - 8:30
t11 = [450,510]  # 7:30 - 8:30
t2 = [1140,1380] # 19:00 - 23:00
t22 = [1140,1440]# 19:00 - 00:00
v1 = 0.1
v2 = 0.2
#%%'

#  EP Weekdays


EP_bulb_living_1_1= EP.Appliance(EP,1,10,1,60,0,60, wd_we_type = 0)
EP_bulb_living_1_1.windows(t1,t0,v1)

EP_bulb_living_1_2 = EP.Appliance(EP,1,10,1,210,0,210, wd_we_type = 0)
EP_bulb_living_1_2.windows([1020,1380],t0,0)

EP_bulb_kitchen_1= EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
EP_bulb_kitchen_1.windows(t1,t0,v1)

EP_bulb_kitchen_2= EP.Appliance(EP,1,10,1,120,0,120, wd_we_type = 0)
EP_bulb_kitchen_2.windows(t2,t0,v1)

EP_bulb1_bedroom_1= EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
EP_bulb1_bedroom_1.windows(t1,t0,v1)

EP_bulb1_bedroom_2= EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
EP_bulb1_bedroom_2.windows([1320,1380],t0,v1)

# EP_bulb2_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb2_bedroom_1.windows(t1,t0,v1)

# EP_bulb2_bedroom_2 = EP.Appliance(EP,1,10,1,15,0,15, wd_we_type = 0)
# EP_bulb2_bedroom_2.windows([1020,1140],t0,v1)

# EP_bulb2_bedroom_3 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb2_bedroom_3.windows([1320,1380],t0,v1)

# EP_bulb3_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb3_bedroom_1.windows(t1,t0,v1)

# EP_bulb3_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 0)
# EP_bulb3_bedroom_2.windows([1320,1380],t0,v1)

EP_bulb_BT_hallway_1 = EP.Appliance(EP,1,10,1,30,0,15, wd_we_type = 0)
EP_bulb_BT_hallway_1.windows(t1,t0,v1)

EP_bulb_BT_hallway_2 = EP.Appliance(EP,1,10,1,30,0,15, wd_we_type = 0)
EP_bulb_BT_hallway_2.windows([1020,1380],t0,0)

EP_outdoor_bulb_1 = EP.Appliance(EP,1,13,1,5,0,5, wd_we_type = 0)   
EP_outdoor_bulb_1.windows([0,510],t0,0)

EP_outdoor_bulb_2 = EP.Appliance(EP,1,13,1,10,0,10, wd_we_type = 0)   
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

EP_Laptop_PC_charger_1 = EP.Appliance(EP,1,50,1,30,0.05,30, wd_we_type = 0)
EP_Laptop_PC_charger_1.windows([390,450],t0,0)

# EP_Laptop_PC_charger_2 = EP.Appliance(EP,1,50,1,30,0.05,30, wd_we_type = 0)
# EP_Laptop_PC_charger_2.windows([840,1020],t0,0)

EP_Laptop_PC_charger_3 = EP.Appliance(EP,1,50,1,30,0.05,30, wd_we_type = 0)
EP_Laptop_PC_charger_3.windows(t2,t0,v1)

EP_Herd = EP.Appliance(EP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 0)
EP_Herd.windows([420,540],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
EP_Herd.cycle_behaviour([480,600],t0)

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


EP_bulb_living_1_1= EP.Appliance(EP,1,10,1,60,0,60, wd_we_type = 1)
EP_bulb_living_1_1.windows(t11,t0,v1)

EP_bulb_living_1_2 = EP.Appliance(EP,1,10,1,210,0,210, wd_we_type = 1)
EP_bulb_living_1_2.windows([1020,1440],t0,0)

EP_bulb_kitchen_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
EP_bulb_kitchen_1.windows(t11,t0,v1)

# EP_bulb_kitchen_2 = EP.Appliance(EP,2,10,1,30,0,30, wd_we_type = 1)
# EP_bulb_kitchen_2.windows([960,1140],t0,v1)

EP_bulb_kitchen_3 = EP.Appliance(EP,1,10,1,120,0,120, wd_we_type = 1)
EP_bulb_kitchen_3.windows(t22,t0,v1)

EP_bulb1_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
EP_bulb1_bedroom_1.windows(t11,t0,v1)

EP_bulb1_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
EP_bulb1_bedroom_2.windows([1320,1440],t0,v1)

# EP_bulb2_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb2_bedroom_1.windows(t11,t0,v1)

# EP_bulb2_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb2_bedroom_2.windows([1020,1320],t0,0)

# EP_bulb2_bedroom_3 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb2_bedroom_3.windows([1320,1440],t0,v1)

# EP_bulb3_bedroom_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb3_bedroom_1.windows(t11,t0,v1)

# EP_bulb3_bedroom_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
# EP_bulb3_bedroom_2.windows([1320,1440],t0,v1)

EP_bulb_BT_hallway_1 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
EP_bulb_BT_hallway_1.windows(t11,t0,v1)

EP_bulb_BT_hallway_2 = EP.Appliance(EP,1,10,1,30,0,30, wd_we_type = 1)
EP_bulb_BT_hallway_2.windows([1020,1440],t0,0)

EP_outdoor_bulb_1 = EP.Appliance(EP,1,13,1,10,0,10, wd_we_type = 1)   
EP_outdoor_bulb_1.windows([0,510],t0,0)

EP_outdoor_bulb_2 = EP.Appliance(EP,1,13,1,10,0,10, wd_we_type = 1)  
EP_outdoor_bulb_2.windows([1020,1440],t0,0)

                              ###

# EP_TV_1= EP.Appliance(EP,1,60,1,30,v1,30, wd_we_type = 1)
# EP_TV_1.windows([540,720],t0,v1)

EP_TV_2= EP.Appliance(EP,1,60,1,60,v1,60, wd_we_type = 1)
EP_TV_2.windows([840,1020],t0,v1)

EP_TV_3= EP.Appliance(EP,1,60,1,60,v1,60, wd_we_type = 1)
EP_TV_3.windows(t22,t0,0)

EP_Phone_charger_1 = EP.Appliance(EP,1,5,1,45,v1,45, wd_we_type = 1)
EP_Phone_charger_1.windows([540,720],t0,v1)

EP_Phone_charger_2 = EP.Appliance(EP,1,5,1,15,v1,15, wd_we_type = 1)
EP_Phone_charger_2.windows(t22,t0,0)

EP_Laptop_PC_charger_1 = EP.Appliance(EP,1,50,1,30,0.05,30, wd_we_type = 1)
EP_Laptop_PC_charger_1.windows([540,720],t0,v1)

# EP_Laptop_PC_charger_2 = EP.Appliance(EP,1,50,1,60,0.05,60, wd_we_type = 1)
# EP_Laptop_PC_charger_2.windows([840,1020],t0,v1)

EP_Laptop_PC_charger_3 = EP.Appliance(EP,1,50,1,30,0.05,30, wd_we_type = 1)
EP_Laptop_PC_charger_3.windows(t22,t0,0)

EP_Herd = EP.Appliance(EP,1,1800,1,15,v1,15, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([480,600],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,5,0.15)
EP_Herd.cycle_behaviour([480,600],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([660,780],t0,v1)
EP_Herd.specific_cycle_1(1800,10,750,35,0.15)
EP_Herd.cycle_behaviour([660,780],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,10,v1,10, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
EP_Herd.windows([900,1020],t0,v1)
EP_Herd.specific_cycle_1(1800,10,0.15)
EP_Herd.cycle_behaviour([900,1020],t0)

EP_Herd = EP.Appliance(EP,1,1800,1,45,v1,45, thermal_P_var = 0.2, fixed_cycle=1, pref_index = 0, wd_we_type = 1)
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


# EP Occasional used devices


# EP_Mixer = EP.Appliance(EP,1,50,2,15,0,10, occasional_use = 1)
# EP_Mixer.windows([420,540],[1140,1260],v1)

EP_Toaster = EP.Appliance(EP,1,1000,2,10,0,10, occasional_use = 0.5)
EP_Toaster.windows([420,540],[1140,1260],v1)

EP_Haartrockner = EP.Appliance(EP,1,1000,2,15,0,15,occasional_use = 0.5)
EP_Haartrockner.windows([420,720],[960,1260],v1)

EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0,15,occasional_use = 0.33)
EP_Luftfritteuse.windows([420,540],[1140,1260], v1)

EP_Spuelmaschine = EP.Appliance(EP,1,1500,1,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33)
EP_Spuelmaschine.windows([1200,1320],t0,v1)

EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0,60, thermal_P_var = 0.2, occasional_use = 0.33)
EP_Waschmaschine.windows([540,720],[1020,1260],v1)

EP_Ofen = EP.Appliance(EP,1,2150,2,60,0,60, thermal_P_var = 0.2, occasional_use= 0.33)
EP_Ofen.windows([420,540],[1140,1260],v1)