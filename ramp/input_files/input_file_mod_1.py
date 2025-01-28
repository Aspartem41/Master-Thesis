# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:46:40 2022

@author: rbala
"""

#%% Definition of the inputs
'''
Input data definition (Einperson Haushalt) 
'''


from ramp.core.core import User, np
User_list = []

'''
This input file represents the rough idea of appliances use in one person household.
'''

#Create new user classes
EP_s = User("Einperson",1,3)
User_list.append(EP_s)


#Create new appliances

# Einpersonenhaushalt

EP_s_innen_licht = EP_s.Appliance(EP_s, 4, 7, 2, 120, 0.2, 20)
EP_s_innen_licht.windows([330,480],[1140,1440],0.35)

EP_s_aussen_licht = EP_s.Appliance(EP_s,1,13,2,180,0.2,10)
EP_s_aussen_licht.windows([60,330],[1170,1440],0.35)

EP_s_TV = EP_s.Appliance(EP_s,1,60,3,120,0.1,5, occasional_use= 0.25)
EP_s_TV.windows([720,900],[1170,1440],0.35,[0,60])

EP_s_router = EP_s.Appliance(EP_s,1,7,1,1440,0.1)
EP_s_router.windows([0,1440],[0,0])

EP_s_Kuehlschrank = EP_s.Appliance(EP_s,1,150,1,1440,0,30,'yes',3)
EP_s_Kuehlschrank.windows([0,1440],[0,0])
EP_s_Kuehlschrank.specific_cycle_1(150,20,5,10)
EP_s_Kuehlschrank.specific_cycle_2(150,15,5,15)
EP_s_Kuehlschrank.specific_cycle_3(150,10,5,20)
EP_s_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

EP_s_Ladegeraet = EP_s.Appliance(EP_s,10,2,2,100,0.2,5)
EP_s_Ladegeraet.windows([360,540],[1110,1440],0.35)

# EP_s_Tiefkuehl = EP_s.Appliance(EP_s,1,200,1,1440,0,30,'yes',3)
# EP_s_Tiefkuehl.windows([0,1440],[0,0])
# EP_s_Tiefkuehl.specific_cycle_1(200,20,5,10)
# EP_s_Tiefkuehl.specific_cycle_2(200,15,5,15)
# EP_s_Tiefkuehl.specific_cycle_3(200,10,5,20)
# EP_s_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# EP_s_Mixer = EP_s.Appliance(EP_s,1,50,2,0,10,0.1,1,occasional_use = 0.5)
# EP_s_Mixer.windows([420,480],[660,750],0.35)#[1140,1200])

EP_s_Luftfriteuse = EP_s.Appliance(EP_s,1,1500,2,0,15,0.1,10,occasional_use = 0.5)
EP_s_Luftfriteuse.windows([420,480],[660,750],0.35)#,[1140,1200])

EP_s_PC = EP_s.Appliance(EP_s,1,50,2,120,0.1,10)
EP_s_PC.windows([480,720],[1050,1440],0.35)

# EP_s_Drucker = EP_s.Appliance(EP_s,1,20,2,30,0.1,5, occasional_use = 0.2)
# EP_s_Drucker.windows([480,600],[1080,1260],0.35)

EP_s_Herd = EP_s.Appliance(EP_s,1,1800,2,90,0.15,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
EP_s_Herd.windows([420,540],[660,900],0.15)#,[1110,1200])
EP_s_Herd.specific_cycle_1(1800,10,750,60,0.15)
EP_s_Herd.cycle_behaviour([720,900],[0,0])

EP_s_Spuelmaschine = EP_s.Appliance(EP_s,1,1500,2,60,0.15,60, thermal_P_var = 0.2, occasional_use=0.5)
EP_s_Spuelmaschine.windows([420,540],[1140,1260],0.35)

EP_s_Wasserkocher = EP_s.Appliance(EP_s,1,2500,3,10,0.15,3, occasional_use = 0.5)
EP_s_Wasserkocher.windows([420,720], [960, 1260],0.30)

EP_s_Waschmaschine = EP_s.Appliance(EP_s,1,1000,2,60,0.15,60, thermal_P_var = 0.2, occasional_use = 0.5)
EP_s_Waschmaschine.windows([420,720], [960, 1260],0.30)

EP_s_Toaster = EP_s.Appliance(EP_s,1,1000,2,9,0.15,3, occasional_use = 0.4)
EP_s_Toaster.windows([420,720], [960, 1260],0.30)

EP_s_Haartrockner = EP_s.Appliance(EP_s,1,1000,2,6,0.15,5, occasional_use =0.5)
EP_s_Haartrockner.windows([420,720], [960, 1260],0.30)

EP_s_Ofen = EP_s.Appliance(EP_s,1,2150,2,60,0.15,60,occasional_use= 0.5, thermal_P_var = 0.2)
EP_s_Ofen.windows([420,480],[660,750],0.35)