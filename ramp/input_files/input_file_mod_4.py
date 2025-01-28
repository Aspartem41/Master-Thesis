# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:16:40 2022

@author: rbala
"""

#%% Definition of the inputs
'''
Input data definition (Alleinerziehende Haushalt) 
'''


from ramp.core.core import User, np
User_list = []

'''
This input file represents the rough idea of appliances use in one person household.
'''

#Create new user classes
AE = User("Alleinerziehende",1)
User_list.append(AE)


#Create new appliances

# Einpersonenhaushalt

AE_innen_licht = AE.Appliance(AE,4,7,2,180,0.2,10)
AE_innen_licht.windows([330,480],[1140,1440],0.35)

AE_aussen_licht = AE.Appliance(AE,1,13,2,180,0.2,10)
AE_aussen_licht.windows([60,330],[1170,1440],0.35)

AE_TV = AE.Appliance(AE,1,60,2,180,0.1,10,occasional_use = 1)
AE_TV.windows([720,900],[1170,1440],0.35)

AE_router = AE.Appliance(AE,1,7,1,1440,0.1)
AE_router.windows([0,1440],[0,0])

AE_Kuehlschrank = AE.Appliance(AE,1,150,1,1440,0,30,'yes',3)
AE_Kuehlschrank.windows([0,1440],[0,0])
AE_Kuehlschrank.specific_cycle_1(150,20,5,10)
AE_Kuehlschrank.specific_cycle_2(150,15,5,15)
AE_Kuehlschrank.specific_cycle_3(150,10,5,20)
AE_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

AE_Ladegeraet = AE.Appliance(AE,10,2,2,150,0.2,15)
AE_Ladegeraet.windows([360,540],[1110,1440],0.35)

# AE_Tiefkuehl = AE.Appliance(AE,1,200,1,1440,0,30,'yes',3)
# AE_Tiefkuehl.windows([0,1440],[0,0])
# AE_Tiefkuehl.specific_cycle_1(200,20,5,10)
# AE_Tiefkuehl.specific_cycle_2(200,15,5,15)
# AE_Tiefkuehl.specific_cycle_3(200,10,5,20)
# AE_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# AE_Mixer = AE.Appliance(AE,1,50,2,0,20,0.1,1,occasional_use = 0.8)
# AE_Mixer.windows([420,750],[1140,1200],0.35)

AE_Luftfriteuse = AE.Appliance(AE,1,1500,2,0,30,0.1,15,occasional_use = 0.75)
AE_Luftfriteuse.windows([420,750],[1140,1200],0.35)

AE_PC = AE.Appliance(AE,1,50,2,180,0.1,15)
AE_PC.windows([480,720],[1050,1440],0.35)

# AE_Drucker = AE.Appliance(AE,1,20,2,30,0.1,5,occasional_use = 0.2)
# AE_Drucker.windows([480,600],[1080,1260],0.35)

AE_Herd = AE.Appliance(AE,1,1800,2,140,0.15,20,thermal_P_var = 0.2,pref_index = 1, fixed_cycle = 1)
AE_Herd.windows([420,780],[1080,1200],0.15)
AE_Herd.specific_cycle_1(1800,10,750,60,0.15)
AE_Herd.cycle_behaviour([720,900],[0,0])

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,60,0.15,60,thermal_P_var = 0.2,occasional_use = 0.75)
AE_Spuelmaschine.windows([420,540],[1140,1260],0.35)

AE_Wasserkocher = AE.Appliance(AE,1,2500,3,15,0.15,3,occasional_use = 0.75)
AE_Wasserkocher.windows([420,720], [960, 1260],0.30)

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0.15,60,thermal_P_var = 0.2,occasional_use = 0.75)
AE_Waschmaschine.windows([420,720], [960, 1260],0.30)

AE_Toaster = AE.Appliance(AE,1,1000,2,15,0.15,3,occasional_use = 0.6)
AE_Toaster.windows([420,720], [960, 1260],0.30)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,10,0.15,5,occasional_use = 0.5)
AE_Haartrockner.windows([420,720], [960, 1260],0.30)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0.15,60,occasional_use= 0.75,thermal_P_var = 0.2)
AE_Ofen.windows([420,780],[1080,1200],0.15)