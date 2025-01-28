# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:39:01 2023

@author: rbala

This infut file is for Spring
"""

from ramp.core.core import User, np
User_list = []


POK = User("Paar ohne Kind",1,3)
User_list.append(POK)


#%%'
# Paar ohne Kind

POK_bulb_living = POK.Appliance(POK,2,7,2,210,0.25,30)
POK_bulb_living.windows([360,510],[1170,1380],0.1)

POK_bulb_kitchen = POK.Appliance(POK,1,7,2,100,0.25,30)
POK_bulb_kitchen.windows([360,510],[1170,1260],0.1)

POK_bulb_bedroom = POK.Appliance(POK,1,7,2,60,0.25,30)
POK_bulb_bedroom.windows([360,420],[1170,1380],0.1)

POK_bulb_floor = POK.Appliance(POK,2,7,2,60,0.25,30)
POK_bulb_floor.windows([360,450],[1170,1320],0.1)

POK_outdoor_bulb = POK.Appliance(POK,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
POK_outdoor_bulb.windows([0,330],[1170,1440],0.1)

POK_TV = POK.Appliance(POK,1,60,3,90,0.1,30)
POK_TV.windows([660,780],[990,1080],0.1,[1170,1440])

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

POK_Toaster = POK.Appliance(POK,1,1000,2,10,0.1,5, occasional_use = 0.5)
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

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.48)
POK_Waschmaschine.windows([540,720],[960,1260],0.1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2)
POK_Ofen.windows([660,840],[1080,1260],0.1)

#%%'
# Paar ohne Kind
POK_bulb_living = POK.Appliance(POK,2,7,2,210,0.25,10, wd_we_type = 1)
POK_bulb_living.windows([450,570],[1050,1440],0.1)

POK_bulb_kitchen = POK.Appliance(POK,1,7,2,100,0.25,10, wd_we_type = 1)
POK_bulb_kitchen.windows([450,540],[1140,1320],0.1)

POK_bulb_bedroom = POK.Appliance(POK,1,7,2,60,0.25,10, wd_we_type = 1)
POK_bulb_bedroom.windows([450,540],[1140,1440],0.1)

POK_bulb_floor = POK.Appliance(POK,2,7,2,60,0.25,10, wd_we_type = 1)
POK_bulb_floor.windows([450,540],[1140,1260],0.1)

POK_outdoor_bulb = POK.Appliance(POK,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
POK_outdoor_bulb.windows([0,330],[1050,1440],0.1)

POK_TV = POK.Appliance(POK,1,60,3,120,0.1,5, wd_we_type = 1)
POK_TV.windows([660,780],[990,1080],0.1,[1170,1440])

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

POK_Toaster = POK.Appliance(POK,1,1000,2,10,0.1,3, occasional_use = 0.5, wd_we_type = 1)
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

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.48, wd_we_type = 1)
POK_Waschmaschine.windows([540,720],[960,1260],0.1)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2, wd_we_type = 1)
POK_Ofen.windows([660,900],[1080,1260],0.1)
