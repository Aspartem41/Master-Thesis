# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''

'''Sim_3 ist für Sommer Profile'''

from ramp.core.core import User, np
User_list = []

'''
TMPs example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a 
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles. 
For examples related to "thermal loads", see the "input_file_2".
'''
#%%
#Create new user classes

MP = User("Mehrperson",3,3)
User_list.append(MP)

PMK = User("Paar mit Kind",25,3)
User_list.append(PMK)

POK = User("Paar ohne Kind",31,3)
User_list.append(POK)

AE = User("Alleinerziehende",10,3)
User_list.append(AE)

EP = User("Einpersonen",38,3)
User_list.append(EP)

#Create new appliances


# Mehrperson Haushalt:
    
MP_bulb_living = MP.Appliance(MP,3,7,2,120,0.2,30)
MP_bulb_living.windows([1170,1440],[0,30],0.1)

MP_bulb_kitchen = MP.Appliance(MP,2,7,2,60,0.2,30)
MP_bulb_kitchen.windows([1170,1440],[0,30],0.1)

MP_bulb_bedroom = MP.Appliance(MP,3,7,2,60,0.2,30)
MP_bulb_bedroom.windows([1170,1440],[0,30],0.1)

MP_bulb_floor = MP.Appliance(MP,2,7,2,60,0.2,30)
MP_bulb_floor.windows([1170,1440],[0,30],0.1)

MP_outdoor_bulb = MP.Appliance(MP,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
MP_outdoor_bulb.windows([0,330],[1170,1440],0.1)

MP_TV = MP.Appliance(MP,2,60,3,120,0.1,30, occasional_use= 1)
MP_TV.windows([600,720],[990,1080],0.1,[1170,1440])

MP_router = MP.Appliance(MP,1,7,1,1440,0.1)
MP_router.windows([0,1440],[0,0])

MP_Phone_charger = MP.Appliance(MP,5,1,2,300,0.2,20)
MP_Phone_charger.windows([0,1440],[0,0])           # im Nachts geladen

MP_Fridge = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3)
MP_Fridge.windows([0,1440],[0,0])
MP_Fridge.specific_cycle_1(200,20,5,10)
MP_Fridge.specific_cycle_2(200,15,5,15)
MP_Fridge.specific_cycle_3(200,10,5,20)
MP_Fridge.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

MP_Tiefkuehl = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3)
MP_Tiefkuehl.windows([0,1440],[0,0])
MP_Tiefkuehl.specific_cycle_1(200,20,5,10)
MP_Tiefkuehl.specific_cycle_2(200,15,5,15)
MP_Tiefkuehl.specific_cycle_3(200,10,5,20)
MP_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

MP_Mixer = MP.Appliance(MP,1,300,3,15,0.1,1,occasional_use = 0.8)
MP_Mixer.windows([420,600],[660,840],0.1,[1140,1230])

MP_Toaster = MP.Appliance(MP,1,1000,2,9,0.1,5, occasional_use = 1)
MP_Toaster.windows([420,600],[1140,1260],0.1)

MP_Haartrockner = MP.Appliance(MP,1,1000,2,10,0.1,5,occasional_use = 1)
MP_Haartrockner.windows([420,720],[960,1260],0.1)

MP_Luftfritteuse = MP.Appliance(MP,1,50,2,30,0.1,1,occasional_use = 0.6)
MP_Luftfritteuse.windows([660,840],[1140,1260], 0.1)

MP_Herd = MP.Appliance(MP,1,1800,3,150,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
MP_Herd.windows([420,600],[660,840],0.1,[1140,1260])
MP_Herd.specific_cycle_1(1800,10,750,60,0.15)
MP_Herd.cycle_behaviour([720,840],[0,0])

MP_Spuelmaschine = MP.Appliance(MP,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=1)
MP_Spuelmaschine.windows([870,990],[1080,1320],0.1)

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 1)
MP_Waschmaschine.windows([540,720],[960,1260],0.10)

MP_Ofen = MP.Appliance(MP,1,2150,2,60,0.1,60,occasional_use= 0.8, thermal_P_var = 0.2)
MP_Ofen.windows([660,900],[1080,1260],0.1)


#%%
# Paar mit Kind

PMK_bulb_living = PMK.Appliance(PMK,2,7,2,120,0.2,30)
PMK_bulb_living.windows([1170,1440],[0,30],0.1)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,7,2,60,0.2,30)
PMK_bulb_kitchen.windows([1170,1440],[0,30],0.1)

PMK_bulb_bedroom = PMK.Appliance(PMK,2,7,2,60,0.2,30)
PMK_bulb_bedroom.windows([1170,1440],[0,30],0.1)

PMK_bulb_floor = PMK.Appliance(PMK,2,7,2,60,0.2,30)
PMK_bulb_floor.windows([1170,1440],[0,30],0.1)

PMK_outdoor_bulb = PMK.Appliance(PMK,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
PMK_outdoor_bulb.windows([0,330],[1170,1440],0.1)

PMK_TV = PMK.Appliance(PMK,1,60,3,120,0.1,30)
PMK_TV.windows([600,720],[990,1080],0.1,[1170,1440])

PMK_router = PMK.Appliance(PMK,1,7,1,1440,0.1)
PMK_router.windows([0,1440],[0,0])

PMK_Phone_charger = PMK.Appliance(PMK,4,2,1,300,0.2,5)
PMK_Phone_charger.windows([0,1440],[0,0])

PMK_Fridge = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3)
PMK_Fridge.windows([0,1440],[0,0])
PMK_Fridge.specific_cycle_1(200,20,5,10)
PMK_Fridge.specific_cycle_2(200,15,5,15)
PMK_Fridge.specific_cycle_3(200,10,5,20)
PMK_Fridge.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

PMK_Tiefkuehl = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3)
PMK_Tiefkuehl.windows([0,1440],[0,0])
PMK_Tiefkuehl.specific_cycle_1(200,20,5,10)
PMK_Tiefkuehl.specific_cycle_2(200,15,5,15)
PMK_Tiefkuehl.specific_cycle_3(200,10,5,20)
PMK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

PMK_Mixer = PMK.Appliance(PMK,1,50,3,30,0.1,5, occasional_use = 0.7)
PMK_Mixer.windows([420,600],[660,840],0.1,[1140,1230])

PMK_Toaster = PMK.Appliance(PMK,1,1000,2,9,0.1,5, occasional_use = 0.6)
PMK_Toaster.windows([420,600],[1140,1260],0.1)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,20,0.1,5,occasional_use =0.5)
PMK_Haartrockner.windows([420,720],[960,1260],0.1)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,2,30,0.1,1,occasional_use = 0.5)
PMK_Luftfritteuse.windows([660,840],[1140,1260], 0.1)

PMK_Herd = PMK.Appliance(PMK,1,1800,3,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
PMK_Herd.windows([420,600],[660,840],0.1,[1140,1260])
PMK_Herd.specific_cycle_1(1800,10,750,60,0.15)
PMK_Herd.cycle_behaviour([720,900],[0,0])

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.5)
PMK_Spuelmaschine.windows([870,990],[1080,1320],0.1)

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.71)
PMK_Waschmaschine.windows([540,720],[960,1260],0.1)

PMK_Ofen = PMK.Appliance(PMK,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2)
PMK_Ofen.windows([660,840],[1080,1260],0.1)

#%%
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

#%%
# Alleinerziehende

AE_bulb_living = AE.Appliance(AE,2,7,2,120,0.2,30)
AE_bulb_living.windows([1170,1440],[0,30],0.1)

AE_bulb_kitchen = AE.Appliance(AE,1,7,2,60,0.2,30)
AE_bulb_kitchen.windows([1170,1440],[0,30],0.1)

AE_bulb_bedroom = AE.Appliance(AE,2,7,2,60,0.2,30)
AE_bulb_bedroom.windows([1170,1440],[0,30],0.1)

AE_bulb_floor = AE.Appliance(AE,1,7,2,60,0.2,30)
AE_bulb_floor.windows([1170,1440],[0,30],0.1)

AE_outdoor_bulb = AE.Appliance(AE,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
AE_outdoor_bulb.windows([0,330],[1170,1440],0.1)

AE_TV = AE.Appliance(AE,1,60,2,90,0.1,30)
AE_TV.windows([990,1080],[1170,1440],0.1)

AE_router = AE.Appliance(AE,1,7,1,1440,0.1)
AE_router.windows([0,1440],[0,0])

AE_Kuehlschrank = AE.Appliance(AE,1,150,1,1440,0,30,'yes',3)
AE_Kuehlschrank.windows([0,1440],[0,0])
AE_Kuehlschrank.specific_cycle_1(150,20,5,10)
AE_Kuehlschrank.specific_cycle_2(150,15,5,15)
AE_Kuehlschrank.specific_cycle_3(150,10,5,20)
AE_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

AE_Phone_charger = AE.Appliance(AE,2,2,1,300,0.2,5)
AE_Phone_charger.windows([0,1440],[0,0])

AE_Mixer = AE.Appliance(AE,1,50,2,20,0.1,5, occasional_use = 0.33)
AE_Mixer.windows([660,840],[1140,1260],0.1)

AE_Toaster = AE.Appliance(AE,1,1000,2,9,0.1,5, occasional_use = 0.8)
AE_Toaster.windows([420,600],[1140,1260],0.1)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,10,0.1,5,occasional_use = 0.5)
AE_Haartrockner.windows([420,720],[960,1260],0.1)

AE_Luftfritteuse = AE.Appliance(AE,1,50,2,30,0.1,1,occasional_use = 0.33)
AE_Luftfritteuse.windows([660,840],[1140,1260], 0.1)

AE_Herd = AE.Appliance(AE,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
AE_Herd.windows([420,600],[1140,1260],0.1)
AE_Herd.specific_cycle_1(1800,10,750,60,0.15)
AE_Herd.cycle_behaviour([720,900],[0,0])

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.5)
AE_Spuelmaschine.windows([870,990],[1080,1320],0.1)

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.5)
AE_Waschmaschine.windows([540,720],[960,1260],0.1)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0.1,60,occasional_use= 0.6, thermal_P_var = 0.2)
AE_Ofen.windows([660,840],[1080,1260],0.1)

#%%
# Einperson

EP_bulb_living = EP.Appliance(EP,1,7,2,120,0.2,30)
EP_bulb_living.windows([1170,1440],[0,30],0.1)

EP_bulb_kitchen = EP.Appliance(EP,1,7,2,60,0.2,30)
EP_bulb_kitchen.windows([1170,1440],[0,30],0.1)

EP_bulb_bedroom = EP.Appliance(EP,1,7,2,60,0.2,30)
EP_bulb_bedroom.windows([1170,1440],[0,30],0.1)

EP_bulb_floor = EP.Appliance(EP,1,7,2,60,0.2,30)
EP_bulb_floor.windows([1170,1440],[0,30],0.1)

EP_outdoor_bulb = EP.Appliance(EP,1,13,2,10,0.2,2)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
EP_outdoor_bulb.windows([0,330],[1170,1440],0.1)

EP_TV = EP.Appliance(EP,1,60,2,90,0.1,30)
EP_TV.windows([990,1080],[1170,1440],0.1)

EP_router = EP.Appliance(EP,1,7,1,1440,0.1)
EP_router.windows([0,1440],[0,0])

EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3)
EP_Kuehlschrank.windows([0,1440],[0,0])
EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
EP_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

EP_Phone_charger = EP.Appliance(EP,2,2,1,300,0.2,5)
EP_Phone_charger.windows([0,1440],[0,0])

EP_Mixer = EP.Appliance(EP,1,50,3,10,0.1,5, occasional_use = 0.33)
EP_Mixer.windows([660,840],[1140,1260],0.1)

EP_Toaster = EP.Appliance(EP,1,1000,2,15,0.1,5, occasional_use = 0.5)
EP_Toaster.windows([420,600],[1140,1260],0.1)

EP_Haartrockner = EP.Appliance(EP,1,1000,2,5,0.1,5, occasional_use =0.5)
EP_Haartrockner.windows([420,720],[960,1260],0.1)

EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0.1,1,occasional_use = 0.33)
EP_Luftfritteuse.windows([420,600],[1140,1260],0.1)

EP_Herd = EP.Appliance(EP,1,1800,3,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
EP_Herd.windows([420,600],[1140,1260],0.1)
EP_Herd.specific_cycle_1(1800,10,750,60,0.15)
EP_Herd.cycle_behaviour([720,900],[0,0])

EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.33)
EP_Spuelmaschine.windows([870,990],[1080,1320],0.1)

EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.3)
EP_Waschmaschine.windows([540,720],[960,1260],0.1)

EP_Ofen = EP.Appliance(EP,1,2150,3,60,0.1,60,occasional_use= 0.33, thermal_P_var = 0.2)
EP_Ofen.windows([660,840],[1080,1260],0.1)




#%% 
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
'Samstag und Sonntag (wd_we_type = 1)'

'TV Zeit- 50% mehr + andere zeitfenster'


# Mehrpersonen
MP_bulb_living = MP.Appliance(MP,3,7,2,120,0.2,10, wd_we_type = 1)
MP_bulb_living.windows([1170,1440],[0,30],0.1)

MP_bulb_kitchen = MP.Appliance(MP,2,7,2,60,0.2,10, wd_we_type = 1)
MP_bulb_kitchen.windows([1170,1440],[0,30],0.1)

MP_bulb_bedroom = MP.Appliance(MP,2,7,2,60,0.2,10, wd_we_type = 1)
MP_bulb_bedroom.windows([1170,1440],[0,30],0.10)

MP_bulb_floor = MP.Appliance(MP,2,7,2,60,0.2,10, wd_we_type = 1)
MP_bulb_floor.windows([1170,1440],[0,30],0.1)

MP_outdoor_bulb = MP.Appliance(MP,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
MP_outdoor_bulb.windows([0,330],[1170,1440],0.1)

MP_TV = MP.Appliance(MP,2,60,3,180,0.1,5, occasional_use= 1, wd_we_type = 1)
MP_TV.windows([720,900],[1170,1440],0.1,[0,60])

MP_router = MP.Appliance(MP,1,7,1,1440,0.1, wd_we_type = 1)
MP_router.windows([0,1440],[0,0])

MP_Phone_charger = MP.Appliance(MP,5,2,1,300,0.2,5, wd_we_type = 1)
MP_Phone_charger.windows([0,1440],[0,0],0.1)           # im Nachts geladen

MP_Fridge = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3, wd_we_type = 1)
MP_Fridge.windows([0,1440],[0,0])
MP_Fridge.specific_cycle_1(200,20,5,10)
MP_Fridge.specific_cycle_2(200,15,5,15)
MP_Fridge.specific_cycle_3(200,10,5,20)
MP_Fridge.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

MP_Tiefkuehl = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3, wd_we_type = 1)
MP_Tiefkuehl.windows([0,1440],[0,0])
MP_Tiefkuehl.specific_cycle_1(200,20,5,10)
MP_Tiefkuehl.specific_cycle_2(200,15,5,15)
MP_Tiefkuehl.specific_cycle_3(200,10,5,20)
MP_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

MP_Mixer = MP.Appliance(MP,1,50,2,30,0.1,1,occasional_use = 0.8, wd_we_type = 1)
MP_Mixer.windows([600,840],[1140,1230],0.1)

MP_Toaster = MP.Appliance(MP,1,1000,2,9,0.1,3, occasional_use = 1, wd_we_type = 1)
MP_Toaster.windows([540,660],[1140,1260],0.1)

MP_Haartrockner = MP.Appliance(MP,1,1000,2,10,0.1,5,occasional_use = 1, wd_we_type = 1)
MP_Haartrockner.windows([540,720],[960,1260],0.1)

MP_Luftfritteuse = MP.Appliance(MP,1,50,2,30,0.1,1,occasional_use = 0.6, wd_we_type = 1)
MP_Luftfritteuse.windows([660,900],[1080,1260],0.1)

MP_Herd = MP.Appliance(MP,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
MP_Herd.windows([660,900],[1080,1260],0.1)
MP_Herd.specific_cycle_1(1800,10,750,60,0.15)
MP_Herd.cycle_behaviour([720,900],[0,0])

MP_Spuelmaschine = MP.Appliance(MP,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=1, wd_we_type = 1)
MP_Spuelmaschine.windows([870,990],[1080,1320],0.1)

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 1, wd_we_type = 1)
MP_Waschmaschine.windows([540,720],[960,1260],0.1)

MP_Ofen = MP.Appliance(MP,1,2150,2,60,0.1,60,occasional_use= 0.8, thermal_P_var = 0.2, wd_we_type = 1)
MP_Ofen.windows([660,900],[1080,1260],0.1)


# Paar mit Kind

PMK_bulb_living = PMK.Appliance(PMK,2,7,2,120,0.2,10, wd_we_type = 1)
PMK_bulb_living.windows([1170,1440],[0,30],0.1)

PMK_bulb_kitchen = PMK.Appliance(PMK,1,7,2,60,0.2,10, wd_we_type = 1)
PMK_bulb_kitchen.windows([1170,1440],[0,30],0.1)

PMK_bulb_bedroom = PMK.Appliance(PMK,2,7,2,60,0.2,10, wd_we_type = 1)
PMK_bulb_bedroom.windows([1170,1440],[0,30],0.1)

PMK_bulb_floor = PMK.Appliance(PMK,2,7,2,60,0.2,10, wd_we_type = 1)
PMK_bulb_floor.windows([1170,1440],[0,30],0.1)

PMK_outdoor_bulb = PMK.Appliance(PMK,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
PMK_outdoor_bulb.windows([0,330],[1170,1440],0.1)

PMK_TV = PMK.Appliance(PMK,1,60,2,180,0.1,5, wd_we_type = 1)
PMK_TV.windows([720,900],[1170,1440],0.1,[0,60])

PMK_router = PMK.Appliance(PMK,1,7,1,1440,0.1, wd_we_type = 1)
PMK_router.windows([0,1440],[0,0])

PMK_Phone_charger = PMK.Appliance(PMK,4,2,1,300,0.2,5, wd_we_type = 1)
PMK_Phone_charger.windows([0,1440],[0,0],0.1)

PMK_Fridge = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3, wd_we_type = 1)
PMK_Fridge.windows([0,1440],[0,0])
PMK_Fridge.specific_cycle_1(200,20,5,10)
PMK_Fridge.specific_cycle_2(200,15,5,15)
PMK_Fridge.specific_cycle_3(200,10,5,20)
PMK_Fridge.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

PMK_Tiefkuehl = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3,  wd_we_type = 1)
PMK_Tiefkuehl.windows([0,1440],[0,0])
PMK_Tiefkuehl.specific_cycle_1(200,20,5,10)
PMK_Tiefkuehl.specific_cycle_2(200,15,5,15)
PMK_Tiefkuehl.specific_cycle_3(200,10,5,20)
PMK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

PMK_Mixer = PMK.Appliance(PMK,1,50,2,30,0.1,1, occasional_use = 0.7, wd_we_type = 1)
PMK_Mixer.windows([600,840],[1140,1230],0.1)

PMK_Toaster = PMK.Appliance(PMK,1,1000,2,9,0.1,3, occasional_use = 0.6, wd_we_type = 1)
PMK_Toaster.windows([540,660],[1140,1260],0.1)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,20,0.1,5,occasional_use =0.5, wd_we_type = 1)
PMK_Haartrockner.windows([540,720],[960,1260],0.10)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,50,2,30,0.1,1,occasional_use = 0.5, wd_we_type = 1)
PMK_Luftfritteuse.windows([660,900],[1080,1260],0.1)

PMK_Herd = PMK.Appliance(PMK,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
PMK_Herd.windows([660,900],[1080,1260],0.1)
PMK_Herd.specific_cycle_1(1800,10,750,60,0.15)
PMK_Herd.cycle_behaviour([720,900],[0,0])

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.5, wd_we_type = 1)
PMK_Spuelmaschine.windows([870,990],[1080,1320],0.1)

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.71,  wd_we_type = 1)
PMK_Waschmaschine.windows([540,720],[960,1260],0.1)

PMK_Ofen = PMK.Appliance(PMK,1,2150,3,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2, wd_we_type = 1)
PMK_Ofen.windows([660,900],[1080,1260],0.1)


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

# Alleinerziehende
AE_bulb_living = AE.Appliance(AE,2,7,2,120,0.2,10, wd_we_type = 1)
AE_bulb_living.windows([1170,1440],[0,30],0.1)

AE_bulb_kitchen = AE.Appliance(AE,1,7,2,60,0.2,10, wd_we_type = 1)
AE_bulb_kitchen.windows([1170,1440],[0,30],0.1)

AE_bulb_bedroom = AE.Appliance(AE,2,7,2,60,0.2,10, wd_we_type = 1)
AE_bulb_bedroom.windows([1170,1440],[0,30],0.1)

AE_bulb_floor = AE.Appliance(AE,1,7,2,60,0.2,10, wd_we_type = 1)
AE_bulb_floor.windows([1170,1440],[0,30],0.1)

AE_outdoor_bulb = AE.Appliance(AE,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
AE_outdoor_bulb.windows([0,330],[1170,1440],0.1)

AE_TV = AE.Appliance(AE,1,60,3,120,0.1,5, wd_we_type = 1)
AE_TV.windows([750,840],[1170,1440],0.1,[0,30])

AE_router = AE.Appliance(AE,1,7,1,1440,0.1, wd_we_type = 1)
AE_router.windows([0,1440],[0,0])

AE_Kuehlschrank = AE.Appliance(AE,1,150,1,1440,0,30,'yes',3, wd_we_type = 1)
AE_Kuehlschrank.windows([0,1440],[0,0])
AE_Kuehlschrank.specific_cycle_1(150,20,5,10)
AE_Kuehlschrank.specific_cycle_2(150,15,5,15)
AE_Kuehlschrank.specific_cycle_3(150,10,5,20)
AE_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

AE_Phone_charger = AE.Appliance(AE,2,2,1,300,0.2,5, wd_we_type = 1)
AE_Phone_charger.windows([0,1440],[0,0],0.1)

AE_Mixer = AE.Appliance(AE,1,50,2,20,0.1,1, occasional_use = 0.33, wd_we_type = 1)
AE_Mixer.windows([600,840],[1140,1230],0.1)

AE_Toaster = AE.Appliance(AE,1,1000,2,9,0.1,3, occasional_use = 0.8, wd_we_type = 1)
AE_Toaster.windows([540,660],[1140,1260],0.1)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,10,0.1,5,occasional_use = 0.5, wd_we_type = 1)
AE_Haartrockner.windows([540,720],[960,1260],0.1)

AE_Luftfritteuse = AE.Appliance(AE,1,50,2,30,0.1,1,occasional_use = 0.33, wd_we_type = 1)
AE_Luftfritteuse.windows([660,900],[1080,1260],0.1)

AE_Herd = AE.Appliance(AE,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
AE_Herd.windows([660,900],[1080,1260],0.1)
AE_Herd.specific_cycle_1(1800,10,750,60,0.15)
AE_Herd.cycle_behaviour([720,900],[0,0])

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.5, wd_we_type = 1)
AE_Spuelmaschine.windows([870,990],[1080,1320],0.1)

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.5, wd_we_type = 1)
AE_Waschmaschine.windows([540,720],[960,1260],0.1)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0.1,60,occasional_use= 0.6, thermal_P_var = 0.2, wd_we_type = 1)
AE_Ofen.windows([660,900],[1080,1260],0.1)

# Einperson

EP_bulb_living = EP.Appliance(EP,1,7,2,120,0.2,10, wd_we_type = 1)
EP_bulb_living.windows([1170,1440],[0,30],0.1)

EP_bulb_kitchen = EP.Appliance(EP,1,7,2,60,0.2,10, wd_we_type = 1)
EP_bulb_kitchen.windows([1170,1440],[0,30],0.1)

EP_bulb_bedroom = EP.Appliance(EP,1,7,2,60,0.2,10, wd_we_type = 1)
EP_bulb_bedroom.windows([1170,1440],[0,30],0.1)

EP_bulb_floor = EP.Appliance(EP,1,7,2,60,0.2,10, wd_we_type = 1)
EP_bulb_floor.windows([1170,1440],[0,30],0.1)

EP_outdoor_bulb = EP.Appliance(EP,1,13,2,10,0.2,1, wd_we_type = 1)   # Meistens mit Bewegungssensor, deswegen nur 10 minuten
EP_outdoor_bulb.windows([0,330],[1170,1440],0.1)

EP_TV = EP.Appliance(EP,1,60,3,120,0.1,5, wd_we_type = 1)
EP_TV.windows([750,840],[1170,1440],0.1,[0,30])

EP_router = EP.Appliance(EP,1,7,1,1440,0.1, wd_we_type = 1)
EP_router.windows([0,1440],[0,0])

EP_Kuehlschrank = EP.Appliance(EP,1,150,1,1440,0,30,'yes',3, wd_we_type = 1)
EP_Kuehlschrank.windows([0,1440],[0,0])
EP_Kuehlschrank.specific_cycle_1(150,20,5,10)
EP_Kuehlschrank.specific_cycle_2(150,15,5,15)
EP_Kuehlschrank.specific_cycle_3(150,10,5,20)
EP_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

EP_Phone_charger = EP.Appliance(EP,2,2,1,300,0.2,5, wd_we_type = 1)
EP_Phone_charger.windows([0,1440],[0,0],0.1) 

EP_Mixer = EP.Appliance(EP,1,50,2,10,0.1,1, occasional_use = 0.33, wd_we_type = 1)
EP_Mixer.windows([600,840],[1140,1230],0.1)

EP_Toaster = EP.Appliance(EP,1,1000,2,9,0.1,3, occasional_use = 0.5, wd_we_type = 1)
EP_Toaster.windows([540,660],[1140,1260],0.1)

EP_Haartrockner = EP.Appliance(EP,1,1000,2,5,0.1,5, occasional_use =0.5, wd_we_type = 1)
EP_Haartrockner.windows([540,720],[960,1260],0.1)

EP_Luftfritteuse = EP.Appliance(EP,1,50,2,30,0.1,1,occasional_use = 0.33, wd_we_type = 1)
EP_Luftfritteuse.windows([660,900],[1080,1260],0.1)

EP_Herd = EP.Appliance(EP,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1, wd_we_type = 1)
EP_Herd.windows([660,900],[1080,1260],0.35)
EP_Herd.specific_cycle_1(1800,10,750,60,0.15)
EP_Herd.cycle_behaviour([720,900],[0,0])

EP_Spuelmaschine = EP.Appliance(EP,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.33, wd_we_type = 1)
EP_Spuelmaschine.windows([870,990],[1080,1320],0.1)

EP_Waschmaschine = EP.Appliance(EP,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.3, wd_we_type = 1)
EP_Waschmaschine.windows([540,720],[960,1260],0.1)

EP_Ofen = EP.Appliance(EP,1,2150,2,60,0.1,60,occasional_use= 0.33, thermal_P_var = 0.2, wd_we_type = 1)
EP_Ofen.windows([660,900],[1080,1260],0.1)