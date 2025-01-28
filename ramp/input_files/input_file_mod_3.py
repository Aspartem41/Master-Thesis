# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:21:16 2022

@author: rbala
"""


#%% Definition of the inputs
'''
Input data definition (Paar mit Kind- Haushalt) 
'''


from ramp.core.core import User, np
User_list = []

'''
This input file represents the rough idea of appliances use in one person household.
'''

#Create new user classes
PMK = User("Paar mit Kind",1)
User_list.append(PMK)


#Create new appliances

# Zweipersonenhaushalt mit KIND



#'------------------------------------------------------------------------'
PMK_innen_licht = PMK.Appliance(PMK,4,7,2,225,0.2,10)
PMK_innen_licht.windows([330,480],[1140,1440],0.35)

PMK_aussen_licht = PMK.Appliance(PMK,1,13,2,180,0.2,10)
PMK_aussen_licht.windows([60,330],[1170,1440],0.35)

PMK_TV = PMK.Appliance(PMK,1,60,2,160,0.1,20)
PMK_TV.windows([720,900],[1170,1440],0.35)

PMK_router = PMK.Appliance(PMK,1,7,1,1440,0.1)
PMK_router.windows([0,1440],[0,0])

PMK_Kuehlschrank = PMK.Appliance(PMK,1,150,1,1440,0,30,'yes',3)
PMK_Kuehlschrank.windows([0,1440],[0,0])
PMK_Kuehlschrank.specific_cycle_1(150,20,5,10)
PMK_Kuehlschrank.specific_cycle_2(150,15,5,15)
PMK_Kuehlschrank.specific_cycle_3(150,10,5,20)
PMK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

PMK_Ladegeraet = PMK.Appliance(PMK,10,2,2,240,0.2,15)
PMK_Ladegeraet.windows([360,540],[1110,1440],0.35)

PMK_Tiefkuehl = PMK.Appliance(PMK,1,200,1,1440,0,30,'yes',3)
PMK_Tiefkuehl.windows([0,1440],[0,0])
PMK_Tiefkuehl.specific_cycle_1(200,20,5,10)
PMK_Tiefkuehl.specific_cycle_2(200,15,5,15)
PMK_Tiefkuehl.specific_cycle_3(200,10,5,20)
PMK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# PMK_Mixer = PMK.Appliance(PMK,1,50,2,0,30,0.1,1,occasional_use = 0.8)
# PMK_Mixer.windows([420,750],[1140,1200],0.35)

PMK_Luftfritteuse = PMK.Appliance(PMK,1,1500,2,0,45,0.1,15,occasional_use = 0.5)
PMK_Luftfritteuse.windows([420,750],[1140,1200],0.35)

PMK_PC = PMK.Appliance(PMK,1,50,2,180,0.1,15)
PMK_PC.windows([480,720],[1050,1440],0.35)

# PMK_Drucker = PMK.Appliance(PMK,1,20,2,30,0.1,5,occasional_use = 0.2)
# PMK_Drucker.windows([480,600],[1080,1260],0.35)

PMK_Herd = PMK.Appliance(PMK,1,1800,2,200,0.15,20,thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
PMK_Herd.windows([420,780],[1080,1200],0.15)
PMK_Herd.specific_cycle_1(1800,10,750,60,0.15)
PMK_Herd.cycle_behaviour([720,900],[0,0])

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,60,0.15,60,thermal_P_var = 0.2,occasional_use = 1)
PMK_Spuelmaschine.windows([420,540],[1140,1260],0.35)

PMK_Wasserkocher = PMK.Appliance(PMK,1,2500,2,24,0.15,3,occasional_use = 0.8)
PMK_Wasserkocher.windows([420,720], [960, 1260],0.30)

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0.15,60,thermal_P_var = 0.2,occasional_use = 1)
PMK_Waschmaschine.windows([420,720], [960, 1260],0.30)

PMK_Toaster = PMK.Appliance(PMK,1,1000,2,18,0.15,3,occasional_use = 0.7)
PMK_Toaster.windows([420,720], [960, 1260],0.30)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,20,0.15,5,occasional_use =0.5)
PMK_Haartrockner.windows([420,720], [960, 1260],0.30)

PMK_Ofen = PMK.Appliance(PMK,1,2150,2,120,0.15,60,occasional_use= 0.8,thermal_P_var = 0.2)
PMK_Ofen.windows([420,780],[1080,1200],0.15)