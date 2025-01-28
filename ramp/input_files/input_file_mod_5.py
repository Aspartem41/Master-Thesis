# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:33:27 2022

@author: rbala
"""

#%% Definition of the inputs
'''
Input data definition (Mehrpersonen Haushalt) 
'''


from ramp.core.core import User, np
User_list = []

'''
This input file represents the rough idea of appliances use in one person household.
'''

#Create new user classes
MP = User("Mehrpersonen",1)
User_list.append(MP)


#Create new appliances

# Zweipersonenhaushalt mit KIND

MP_innen_licht = MP.Appliance(MP,5,7,2,300,0.2,10)
MP_innen_licht.windows([330,480],[1140,1440],0.35)

MP_aussen_licht = MP.Appliance(MP,1,13,2,180,0.2,10)
MP_aussen_licht.windows([60,330],[1170,1440],0.35)

MP_TV = MP.Appliance(MP,1,60,2,300,0.1,20,occasional_use = 0.25)
MP_TV.windows([720,900],[1170,1440],0.35)

MP_router = MP.Appliance(MP,1,7,1,1440,0.1)
MP_router.windows([0,1440],[0,0])

MP_Kuehlschrank = MP.Appliance(MP,1,150,1,1440,0,30,'yes',3)
MP_Kuehlschrank.windows([0,1440],[0,0])
MP_Kuehlschrank.specific_cycle_1(150,20,5,10)
MP_Kuehlschrank.specific_cycle_2(150,15,5,15)
MP_Kuehlschrank.specific_cycle_3(150,10,5,20)
MP_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

MP_Ladegeraet = MP.Appliance(MP,10,2,2,300,0.2,15)
MP_Ladegeraet.windows([360,540],[1110,1440],0.35)

MP_Tiefkuehl = MP.Appliance(MP,1,200,1,1440,0,30,'yes',3)
MP_Tiefkuehl.windows([0,1440],[0,0])
MP_Tiefkuehl.specific_cycle_1(200,20,5,10)
MP_Tiefkuehl.specific_cycle_2(200,15,5,15)
MP_Tiefkuehl.specific_cycle_3(200,10,5,20)
MP_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# MP_Mixer = MP.Appliance(MP,1,50,2,0,30,0.1,1,occasional_use = 0.8)
# MP_Mixer.windows([420,750],[1140,1200],0.35)

MP_Luftfriteuse = MP.Appliance(MP,1,1500,2,0,60,0.1,15,occasional_use = 0.8)
MP_Luftfriteuse.windows([420,750],[1140,1200],0.35)

MP_PC = MP.Appliance(MP,1,50,2,300,0.1,15)
MP_PC.windows([480,720],[1050,1440],0.35)

# MP_Drucker = MP.Appliance(MP,1,20,2,30,0.1,5,occasional_use = 0.2)
# MP_Drucker.windows([480,600],[1080,1260],0.35)

MP_Herd = MP.Appliance(MP,1,1800,2,240,0.15,20,thermal_P_var = 0.2,pref_index = 1,fixed_cycle = 1)
MP_Herd.windows([420,780],[1080,1200],0.15)
MP_Herd.specific_cycle_1(1800,10,750,60,0.15)
MP_Herd.cycle_behaviour([720,900],[0,0])

MP_Spuelmaschine = MP.Appliance(MP,1,1500,2,60,0.15,60,thermal_P_var = 0.2,occasional_use = 1)
MP_Spuelmaschine.windows([420,540],[1140,1260],0.35)

MP_Wasserkocher = MP.Appliance(MP,1,2500,3,30,0.15,3,occasional_use = 1)
MP_Wasserkocher.windows([420,720], [960, 1260],0.30)

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0.15,60,thermal_P_var = 0.2,occasional_use =1)
MP_Waschmaschine.windows([420,720], [960, 1260],0.30)

MP_Toaster = MP.Appliance(MP,1,1000,2,18,0.15,3,occasional_use = 1)
MP_Toaster.windows([420,720], [960, 1260],0.30)

MP_Haartrockner = MP.Appliance(MP,1,1000,2,10,0.15,5,occasional_use = 1)
MP_Haartrockner.windows([420,720], [960, 1260],0.30)

MP_Ofen = MP.Appliance(MP,1,2150,2,60,0.15,60,occasional_use= 1,thermal_P_var = 0.2)
MP_Ofen.windows([420,780],[1080,1200],0.15)