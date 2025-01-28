# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:07:41 2022

@author: rbala
"""

#%% Definition of the inputs
'''
Input data definition (Paar ohne Kind- Haushalt) 
'''


from ramp.core.core import User, np
User_list = []

'''
This input file represents the rough idea of appliances use in one person household.
'''

#Create new user classes
POK = User("Paar ohne Kind",1)
User_list.append(POK)


#Create new appliances

# Zweipersonenhaushalt

POK_innen_licht = POK.Appliance(POK, 4, 7, 2, 180, 0.2, 20)
POK_innen_licht.windows([330,480],[1140,1440],0.35)

POK_aussen_licht = POK.Appliance(POK,1,13,2,180,0.2,10)
POK_aussen_licht.windows([60,330],[1170,1440],0.35)

POK_TV = POK.Appliance(POK,1,60,2,180,0.1,5, occasional_use= 0.25)
POK_TV.windows([720,900],[1170,1440],0.35)

POK_router = POK.Appliance(POK,1,7,1,1440,0.1)
POK_router.windows([0,1440],[0,0])

POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3)
POK_Kuehlschrank.windows([0,1440],[0,0])
POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
POK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

POK_Ladegeraet = POK.Appliance(POK,10,2,2,150,0.2,15)
POK_Ladegeraet.windows([360,540],[1110,1440],0.35)

POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3)
POK_Tiefkuehl.windows([0,1440],[0,0])
POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
POK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# POK_Mixer = POK.Appliance(POK,1,50,2,0,10,0.1,1,occasional_use = 0.5)
# POK_Mixer.windows([420,480],[660,750],0.35)#[1140,1200])

POK_Luftfriteuse = POK.Appliance(POK,1,1500,2,0,30,0.1,15,occasional_use = 0.7)
POK_Luftfriteuse.windows([420,480],[660,750],0.35)#,[1140,1200])

POK_PC = POK.Appliance(POK,1,50,2,180,0.1,10)
POK_PC.windows([480,720],[1050,1440],0.35)

# POK_Drucker = POK.Appliance(POK,1,20,2,30,0.1,5, occasional_use = 0.2)
# POK_Drucker.windows([480,600],[1080,1260],0.35)

POK_Herd = POK.Appliance(POK,1,1800,2,135,0.15,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
POK_Herd.windows([420,540],[660,900],0.15)#,[1110,1200])
POK_Herd.specific_cycle_1(1800,10,750,60,0.15)
POK_Herd.cycle_behaviour([720,900],[0,0])

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,60,0.15,60, thermal_P_var = 0.2, occasional_use=0.7)
POK_Spuelmaschine.windows([420,540],[1140,1260],0.35)

POK_Wasserkocher = POK.Appliance(POK,1,2500,2,10,0.15,3, occasional_use = 0.7)
POK_Wasserkocher.windows([420,720], [960, 1260],0.30)

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.15,60, thermal_P_var = 0.2, occasional_use = 0.7)
POK_Waschmaschine.windows([420,720], [960, 1260],0.30)

POK_Toaster = POK.Appliance(POK,1,1000,2,9,0.15,3, occasional_use = 0.7)
POK_Toaster.windows([420,720], [960, 1260],0.30)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,10,0.15,5, occasional_use =0.5)
POK_Haartrockner.windows([420,720], [960, 1260],0.30)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.15,60,occasional_use= 0.7, thermal_P_var = 0.2)
POK_Ofen.windows([420,480],[660,750],0.35)