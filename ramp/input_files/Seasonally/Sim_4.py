# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:50:44 2023

@author: rbala
"""

from ramp.core.core import User, np
User_list = []

# EP = User("Einpersonen",1,3)
# User_list.append(EP)
POK = User("Paar ohne Kind",1,3)
User_list.append(POK)

# Einperson

# EP_bulb_living = EP.Appliance(EP,1,7,2,120,0.2,30)
# EP_bulb_living.windows([1170,1440],[0,30],0.1)

# EP_bulb_kitchen = EP.Appliance(EP,1,7,2,60,0.2,30)
# EP_bulb_kitchen.windows([1170,1440],[0,30],0.1)

# EP_bulb_bedroom = EP.Appliance(EP,1,7,2,60,0.2,30)
# EP_bulb_bedroom.windows([1170,1440],[0,30],0.1)

# EP_bulb_floor = EP.Appliance(EP,1,7,2,60,0.2,30)
# EP_bulb_floor.windows([1170,1440],[0,30],0.1)

# EP_outdoor_bulb = EP.Appliance(EP,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
# EP_outdoor_bulb.windows([0,330],[1170,1440],0.1)

# EP_TV = EP.Appliance(EP,1,60,2,90,0.1,30)
# EP_TV.windows([990,1080],[1170,1440],0.1)

# EP_router = EP.Appliance(EP,1,7,1,1440,0.1)
# EP_router.windows([0,1440],[0,0])

# EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3)
# EP_Kuehlschrank.windows([0,1440],[0,0])
# EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
# EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
# EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
# EP_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# EP_Phone_charger = EP.Appliance(EP,2,2,1,300,0.2,5)
# EP_Phone_charger.windows([0,1440],[0,0])

# EP_Mixer = EP.Appliance(EP,1,50,3,10,0.1,5, occasional_use = 0.33)
# EP_Mixer.windows([660,840],[1140,1260],0.1)

# EP_Toaster = EP.Appliance(EP,1,1000,2,15,0.1,5, occasional_use = 0.5)
# EP_Toaster.windows([420,600],[1140,1260],0.1)

# EP_Haartrockner = EP.Appliance(EP,1,1000,2,5,0.1,5, occasional_use =0.5)
# EP_Haartrockner.windows([420,720],[960,1260],0.1)

# EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0.1,1,occasional_use = 0.33)
# EP_Luftfritteuse.windows([420,600],[1140,1260],0.1)

# EP_Herd = EP.Appliance(EP,1,1800,3,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
# EP_Herd.windows([420,600],[1140,1260],0.1)
# EP_Herd.specific_cycle_1(1800,10,750,60,0.15)
# EP_Herd.cycle_behaviour([720,900],[0,0])

# EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.33)
# EP_Spuelmaschine.windows([870,990],[1080,1320],0.1)

# EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.3)
# EP_Waschmaschine.windows([540,720],[960,1260],0.1)

# EP_Ofen = EP.Appliance(EP,1,2150,3,60,0.1,60,occasional_use= 0.33, thermal_P_var = 0.2)
# EP_Ofen.windows([660,840],[1080,1260],0.1)

# # Einperson

# EP_bulb_living = EP.Appliance(EP,1,7,2,120,0.2,10, wd_we_type = 1)
# EP_bulb_living.windows([1170,1440],[0,30],0.1)

# EP_bulb_kitchen = EP.Appliance(EP,1,7,2,60,0.2,10, wd_we_type = 1)
# EP_bulb_kitchen.windows([1170,1440],[0,30],0.1)

# EP_bulb_bedroom = EP.Appliance(EP,1,7,2,60,0.2,10, wd_we_type = 1)
# EP_bulb_bedroom.windows([1170,1440],[0,30],0.1)

# EP_bulb_floor = EP.Appliance(EP,1,7,2,60,0.2,10, wd_we_type = 1)
# EP_bulb_floor.windows([1170,1440],[0,30],0.1)

# EP_outdoor_bulb = EP.Appliance(EP,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
# EP_outdoor_bulb.windows([0,330],[1170,1440],0.1)

# EP_TV = EP.Appliance(EP,1,60,3,120,0.1,5, wd_we_type = 1)
# EP_TV.windows([750,840],[1170,1440],0.1,[0,30])

# EP_router = EP.Appliance(EP,1,7,1,1440,0.1, wd_we_type = 1)
# EP_router.windows([0,1440],[0,0])

# EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3, wd_we_type = 1)
# EP_Kuehlschrank.windows([0,1440],[0,0])
# EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
# EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
# EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
# EP_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# EP_Phone_charger = EP.Appliance(EP,2,2,1,300,0.2,5, wd_we_type = 1)
# EP_Phone_charger.windows([0,1440],[0,0],0.1) 

# EP_Mixer = EP.Appliance(EP,1,50,2,10,0.1,1, occasional_use = 0.33, wd_we_type = 1)
# EP_Mixer.windows([600,840],[1140,1230],0.1)

# EP_Toaster = EP.Appliance(EP,1,1000,2,9,0.1,3, occasional_use = 0.5, wd_we_type = 1)
# EP_Toaster.windows([540,660],[1140,1260],0.1)

# EP_Haartrockner = EP.Appliance(EP,1,1000,2,5,0.1,5, occasional_use =0.5, wd_we_type = 1)
# EP_Haartrockner.windows([540,720],[960,1260],0.1)

# EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0.1,1,occasional_use = 0.33, wd_we_type = 1)
# EP_Luftfritteuse.windows([660,900],[1080,1260],0.1)

# EP_Herd = EP.Appliance(EP,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
# EP_Herd.windows([660,900],[1080,1260],0.35)
# EP_Herd.specific_cycle_1(1800,10,750,60,0.15)
# EP_Herd.cycle_behaviour([720,900],[0,0])

# EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.33, wd_we_type = 1)
# EP_Spuelmaschine.windows([870,990],[1080,1320],0.1)

# EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.3, wd_we_type = 1)
# EP_Waschmaschine.windows([540,720],[960,1260],0.1)

# EP_Ofen = EP.Appliance(EP,1,2150,2,60,0.1,60,occasional_use= 0.33, thermal_P_var = 0.2, wd_we_type = 1)
# EP_Ofen.windows([660,900],[1080,1260],0.1)


#%%'
# Paar ohne Kind

POK_bulb_living = POK.Appliance(POK,2,7,2,120,0.2,30)
POK_bulb_living.windows([1170,1440],[0,30],0.1)

POK_bulb_kitchen = POK.Appliance(POK,1,7,2,60,0.2,30)
POK_bulb_kitchen.windows([1170,1440],[0,30],0.1)

POK_bulb_bedroom = POK.Appliance(POK,1,7,2,60,0.2,30)
POK_bulb_bedroom.windows([1170,1440],[0,30],0.1)

POK_bulb_floor = POK.Appliance(POK,2,7,2,60,0.2,30)
POK_bulb_floor.windows([1170,1440],[0,30],0.1)

POK_outdoor_bulb = POK.Appliance(POK,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
POK_outdoor_bulb.windows([0,330],[1170,1440],0.1)

POK_TV = POK.Appliance(POK,1,60,2,90,0.1,30)
POK_TV.windows([990,1080],[1170,1440],0.1)

POK_router = POK.Appliance(POK,1,7,1,1440,0.1)
POK_router.windows([0,1440],[0,0])

POK_Phone_charger = POK.Appliance(POK,4,2,1,300,0.2,5)
POK_Phone_charger.windows([0,1440],[0,0])

POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3)
POK_Kuehlschrank.windows([0,1440],[0,0])
POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
POK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3)
POK_Tiefkuehl.windows([0,1440],[0,0])
POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
POK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

POK_Mixer = POK.Appliance(POK,1,50,2,30,0.1,1, occasional_use = 0.33)
POK_Mixer.windows([420,600],[1140,1260],0.1)

POK_Toaster = POK.Appliance(POK,1,1000,2,9,0.1,5, occasional_use = 0.5)
POK_Toaster.windows([420,600],[1140,1260],0.1)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0.1,5,occasional_use =0.5)
POK_Haartrockner.windows([420,720],[960,1260],0.10)

POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0.1,15,occasional_use = 0.33)
POK_Luftfritteuse.windows([660,840],[1140,1260], 0.1)

POK_Herd = POK.Appliance(POK,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
POK_Herd.windows([420,600],[1140,1260],0.1)
POK_Herd.specific_cycle_1(1800,10,750,60,0.15)
POK_Herd.cycle_behaviour([720,900],[0,0])

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.33)
POK_Spuelmaschine.windows([870,990],[1080,1320],0.1)

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.43)
POK_Waschmaschine.windows([540,720],[960,1260],0.1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2)
POK_Ofen.windows([660,840],[1080,1260],0.1)

# Paar ohne Kind
POK_bulb_living = POK.Appliance(POK,2,7,2,120,0.2,10, wd_we_type = 1)
POK_bulb_living.windows([1170,1440],[0,30],0.1)

POK_bulb_kitchen = POK.Appliance(POK,1,7,2,60,0.2,10, wd_we_type = 1)
POK_bulb_kitchen.windows([1170,1440],[0,30],0.1)

POK_bulb_bedroom = POK.Appliance(POK,1,7,2,60,0.2,10, wd_we_type = 1)
POK_bulb_bedroom.windows([1170,1440],[0,30],0.1)

POK_bulb_floor = POK.Appliance(POK,2,7,2,60,0.2,10, wd_we_type = 1)
POK_bulb_floor.windows([1170,1440],[0,30],0.1)

POK_outdoor_bulb = POK.Appliance(POK,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
POK_outdoor_bulb.windows([0,330],[1170,1440],0.1)

POK_TV = POK.Appliance(POK,1,60,3,120,0.1,5, wd_we_type = 1)
POK_TV.windows([720,900],[1170,1440],0.1,[0,60])

POK_router = POK.Appliance(POK,1,7,1,1440,0.1, wd_we_type = 1)
POK_router.windows([0,1440],[0,0])

POK_Phone_charger = POK.Appliance(POK,4,2,1,300,0.2,5, wd_we_type = 1)
POK_Phone_charger.windows([0,1440],[0,0],0.1)

POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3, wd_we_type = 1)
POK_Kuehlschrank.windows([0,1440],[0,0])
POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
POK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3, wd_we_type = 1)
POK_Tiefkuehl.windows([0,1440],[0,0])
POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
POK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

POK_Mixer = POK.Appliance(POK,1,50,2,30,0.1,1, occasional_use = 0.33, wd_we_type = 1)
POK_Mixer.windows([600,840],[1140,1230],0.1)

POK_Toaster = POK.Appliance(POK,1,1000,2,9,0.1,3, occasional_use = 0.5, wd_we_type = 1)
POK_Toaster.windows([540,660],[1140,1260],0.1)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0.1,5,occasional_use =0.5, wd_we_type = 1)
POK_Haartrockner.windows([540,720],[960,1260],0.1)

POK_Luftfritteuse = POK.Appliance(POK,1,50,2,30,0.1,1,occasional_use = 0.33, wd_we_type = 1)
POK_Luftfritteuse.windows([660,900],[1080,1260],0.1)

POK_Herd = POK.Appliance(POK,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
POK_Herd.windows([660,900],[1080,1260],0.1)
POK_Herd.specific_cycle_1(1800,10,750,60,0.15)
POK_Herd.cycle_behaviour([720,900],[0,0])

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.33, wd_we_type = 1)
POK_Spuelmaschine.windows([870,990],[1080,1320],0.1)

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.43, wd_we_type = 1)
POK_Waschmaschine.windows([540,720],[960,1260],0.1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2, wd_we_type = 1)
POK_Ofen.windows([660,900],[1080,1260],0.1)