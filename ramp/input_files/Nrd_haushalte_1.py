# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:27:53 2022

@author: rbala
"""

#%% Definition of the inputs
'''
Input data definition 
'''


from ramp.core.core import User, np
User_list = []


#Nutzer Definierung

EP_s = User("Einperson",1)
User_list.append(EP_s)

POK = User("Paar ohne Kind",1)
User_list.append(POK)

PMK = User("Paar mit Kind",1)
User_list.append(PMK)

AE = User("Alleinerziehende",1)
User_list.append(AE)

MP = User("Mehrpersonen",1)
User_list.append(MP)

#Create new appliances

# Einpersonenhaushalt

EP_s_innen_licht = EP_s.Appliance(EP_s, 4, 7, 2, 120, 0.2, 20)
EP_s_innen_licht.windows([330,480],[1140,1440],0.35)

EP_s_aussen_licht = EP_s.Appliance(EP_s,1,13,2,180,0.2,10)
EP_s_aussen_licht.windows([60,330],[1170,1440],0.35)

EP_s_TV = EP_s.Appliance(EP_s,1,60,2,120,0.1,20, occasional_use= 0.25)
EP_s_TV.windows([720,900],[1170,1440],0.35)

EP_s_router = EP_s.Appliance(EP_s,1,7,1,1440,0.1)
EP_s_router.windows([0,1440],[0,0])

EP_s_Kuehlschrank = EP_s.Appliance(EP_s,1,150,1,1440,0,30,'yes',3)
EP_s_Kuehlschrank.windows([0,1440],[0,0])
EP_s_Kuehlschrank.specific_cycle_1(150,20,5,10)
EP_s_Kuehlschrank.specific_cycle_2(150,15,5,15)
EP_s_Kuehlschrank.specific_cycle_3(150,10,5,20)
EP_s_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

EP_s_Ladegeraet = EP_s.Appliance(EP_s,10,2,2,90,0.2,15)
EP_s_Ladegeraet.windows([360,540],[1110,1440],0.35)

EP_s_Luftfriteuse = EP_s.Appliance(EP_s,1,1500,2,0,15,0.1,15,occasional_use = 0.5)
EP_s_Luftfriteuse.windows([420,480],[660,750],0.35)#,[1140,1200])

EP_s_PC = EP_s.Appliance(EP_s,1,50,2,120,0.1,10)
EP_s_PC.windows([480,720],[1050,1440],0.35)

EP_s_Herd = EP_s.Appliance(EP_s,1,1800,2,100,0.1,20, thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
EP_s_Herd.windows([420,540],[660,900],0.15)#,[1110,1200])
EP_s_Herd.specific_cycle_1(1800,10,750,60,0.15)
EP_s_Herd.cycle_behaviour([720,900],[0,0])

EP_s_Spuelmaschine = EP_s.Appliance(EP_s,1,1500,2,60,0.1,60, thermal_P_var = 0.2, occasional_use=0.5)
EP_s_Spuelmaschine.windows([420,540],[1140,1260],0.35)

EP_s_Wasserkocher = EP_s.Appliance(EP_s,1,2500,2,9,0.1,3, occasional_use = 0.5)
EP_s_Wasserkocher.windows([420,720],[960,1260],0.30)

EP_s_Waschmaschine = EP_s.Appliance(EP_s,1,1000,2,60,0.1,60, thermal_P_var = 0.2, occasional_use = 0.5)
EP_s_Waschmaschine.windows([420,720],[960,1260],0.30)

EP_s_Toaster = EP_s.Appliance(EP_s,1,1000,2,9,0.1,3, occasional_use = 0.4)
EP_s_Toaster.windows([420,720],[960,1260],0.30)

EP_s_Haartrockner = EP_s.Appliance(EP_s,1,1000,2,5,0.1,5, occasional_use =0.5)
EP_s_Haartrockner.windows([420,720],[960,1260],0.30)

EP_s_Ofen = EP_s.Appliance(EP_s,1,2150,2,60,0.1,60,occasional_use= 0.5, thermal_P_var = 0.2)
EP_s_Ofen.windows([420,480],[660,750],0.35)

# Zweipersonenhaushalt

POK_innen_licht = POK.Appliance(POK,4,7,2,180,0.2,10)
POK_innen_licht.windows([330,480],[1140,1440],0.35)

POK_aussen_licht = POK.Appliance(POK,1,13,2,180,0.2,10)
POK_aussen_licht.windows([60,330],[1170,1440],0.35)

POK_TV = POK.Appliance(POK,1,60,2,120,0.1,20)
POK_TV.windows([720,900],[1170,1440],0.35)

POK_router = POK.Appliance(POK,1,7,1,1440,0.1)
POK_router.windows([0,1440],[0,0])

POK_Kuehlschrank = POK.Appliance(POK,1,150,1,1440,0,30,'yes',3)
POK_Kuehlschrank.windows([0,1440],[0,0])
POK_Kuehlschrank.specific_cycle_1(150,20,5,10)
POK_Kuehlschrank.specific_cycle_2(150,15,5,15)
POK_Kuehlschrank.specific_cycle_3(150,10,5,20)
POK_Kuehlschrank.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

POK_Ladegeraet = POK.Appliance(POK,10,2,2,200,0.2,15)
POK_Ladegeraet.windows([360,540],[1110,1440],0.35)

POK_Tiefkuehl = POK.Appliance(POK,1,200,1,1440,0,30,'yes',3)
POK_Tiefkuehl.windows([0,1440],[0,0])
POK_Tiefkuehl.specific_cycle_1(200,20,5,10)
POK_Tiefkuehl.specific_cycle_2(200,15,5,15)
POK_Tiefkuehl.specific_cycle_3(200,10,5,20)
POK_Tiefkuehl.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

# POK_Mixer = POK.Appliance(POK,1,50,2,0,20,0.1,1,occasional_use = 0.5)
# POK_Mixer.windows([420,750],[1140,1200],0.35)

POK_Luftfritteuse = POK.Appliance(POK,1,1500,2,0,30,0.1,15,occasional_use = 0.5)
POK_Luftfritteuse.windows([420,750],[1140,1200],0.35)

POK_PC = POK.Appliance(POK,1,50,2,180,0.1,15)
POK_PC.windows([480,720],[1050,1440],0.35)

# POK_Drucker = POK.Appliance(POK,1,20,2,30,0.1,5,occasional_use = 0.2)
# POK_Drucker.windows([480,600],[1080,1260],0.35)

POK_Herd = POK.Appliance(POK,1,1800,2,120,0.1,20,thermal_P_var = 0.2,pref_index =1,fixed_cycle=1)
POK_Herd.windows([420,780],[1080,1200],0.15)
POK_Herd.specific_cycle_1(1800,10,750,60,0.15)
POK_Herd.cycle_behaviour([720,900],[0,0])

POK_Spuelmaschine = POK.Appliance(POK,1,1500,2,60,0.1,60,thermal_P_var = 0.2,occasional_use=0.75)
POK_Spuelmaschine.windows([420,540],[1140,1260],0.35)

POK_Wasserkocher = POK.Appliance(POK,1,2500,2,18,0.1,3,occasional_use = 0.5)
POK_Wasserkocher.windows([420,720],[960,1260],0.30)

POK_Waschmaschine = POK.Appliance(POK,1,1000,2,60,0.1,60,thermal_P_var = 0.2,occasional_use = 0.75)
POK_Waschmaschine.windows([420,720],[960,1260],0.30)

POK_Toaster = POK.Appliance(POK,1,1000,2,18,0.1,3,occasional_use = 0.6)
POK_Toaster.windows([420,720],[960,1260],0.30)

POK_Haartrockner = POK.Appliance(POK,1,1000,2,15,0.1,5,occasional_use =0.5)
POK_Haartrockner.windows([420,720],[960,1260],0.30)

POK_Ofen = POK.Appliance(POK,1,2150,2,60,0.1,60,occasional_use= 0.75,thermal_P_var = 0.2)
POK_Ofen.windows([420,780],[1080,1200],0.15)

# Zweipersonenhaushalt mit KIND

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

PMK_Herd = PMK.Appliance(PMK,1,1800,2,200,0.1,20,thermal_P_var = 0.2,pref_index =1, fixed_cycle=1)
PMK_Herd.windows([420,780],[1080,1200],0.15)
PMK_Herd.specific_cycle_1(1800,10,750,60,0.15)
PMK_Herd.cycle_behaviour([720,900],[0,0])

PMK_Spuelmaschine = PMK.Appliance(PMK,1,1500,2,60,0.1,60,thermal_P_var = 0.2,occasional_use = 1)
PMK_Spuelmaschine.windows([420,540],[1140,1260],0.35)

PMK_Wasserkocher = PMK.Appliance(PMK,1,2500,2,24,0.1,3,occasional_use = 0.8)
PMK_Wasserkocher.windows([420,720],[960,1260],0.30)

PMK_Waschmaschine = PMK.Appliance(PMK,1,1000,2,60,0.1,60,thermal_P_var = 0.2,occasional_use = 1)
PMK_Waschmaschine.windows([420,720],[960,1260],0.30)

PMK_Toaster = PMK.Appliance(PMK,1,1000,2,18,0.1,3,occasional_use = 0.7)
PMK_Toaster.windows([420,720],[960,1260],0.30)

PMK_Haartrockner = PMK.Appliance(PMK,1,1000,2,20,0.1,5,occasional_use =0.5)
PMK_Haartrockner.windows([420,720],[960,1260],0.30)

PMK_Ofen = PMK.Appliance(PMK,1,2150,2,120,0.1,60,occasional_use= 0.8,thermal_P_var = 0.2)
PMK_Ofen.windows([420,780],[1080,1200],0.15)

# Alleinerziehendehaushalt

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

AE_Herd = AE.Appliance(AE,1,1800,2,140,0.1,20,thermal_P_var = 0.2,pref_index = 1, fixed_cycle = 1)
AE_Herd.windows([420,780],[1080,1200],0.15)
AE_Herd.specific_cycle_1(1800,10,750,60,0.15)
AE_Herd.cycle_behaviour([720,900],[0,0])

AE_Spuelmaschine = AE.Appliance(AE,1,1500,2,60,0.1,60,thermal_P_var = 0.2,occasional_use = 0.75)
AE_Spuelmaschine.windows([420,540],[1140,1260],0.35)

AE_Wasserkocher = AE.Appliance(AE,1,2500,3,15,0.1,3,occasional_use = 0.75)
AE_Wasserkocher.windows([420,720],[960,1260],0.30)

AE_Waschmaschine = AE.Appliance(AE,1,1000,2,60,0.1,60,thermal_P_var = 0.2,occasional_use = 0.75)
AE_Waschmaschine.windows([420,720],[960,1260],0.30)

AE_Toaster = AE.Appliance(AE,1,1000,2,15,0.1,3,occasional_use = 0.6)
AE_Toaster.windows([420,720],[960,1260],0.30)

AE_Haartrockner = AE.Appliance(AE,1,1000,2,10,0.1,5,occasional_use = 0.5)
AE_Haartrockner.windows([420,720],[960,1260],0.30)

AE_Ofen = AE.Appliance(AE,1,2150,2,60,0.1,60,occasional_use= 0.75,thermal_P_var = 0.2)
AE_Ofen.windows([420,780],[1080,1200],0.15)

# Mehrpersonen (Zweipersonenhaushalt mit KIND)

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

MP_Herd = MP.Appliance(MP,1,1800,2,240,0.1,20,thermal_P_var = 0.2,pref_index = 1,fixed_cycle = 1)
MP_Herd.windows([420,780],[1080,1200],0.15)
MP_Herd.specific_cycle_1(1800,10,750,60,0.15)
MP_Herd.cycle_behaviour([720,900],[0,0])

MP_Spuelmaschine = MP.Appliance(MP,1,1500,2,60,0.1,60,thermal_P_var = 0.2,occasional_use = 1)
MP_Spuelmaschine.windows([420,540],[1140,1260],0.35)

MP_Wasserkocher = MP.Appliance(MP,1,2500,3,30,0.1,3,occasional_use = 1)
MP_Wasserkocher.windows([420,720],[960, 1260],0.30)

MP_Waschmaschine = MP.Appliance(MP,1,1000,2,60,0.1,60,thermal_P_var = 0.2,occasional_use =1)
MP_Waschmaschine.windows([420,720],[960,1260],0.30)

MP_Toaster = MP.Appliance(MP,1,1000,2,18,0.1,3,occasional_use = 1)
MP_Toaster.windows([420,720],[960,1260],0.30)

MP_Haartrockner = MP.Appliance(MP,1,1000,2,10,0.1,5,occasional_use = 1)
MP_Haartrockner.windows([420,720],[960,1260],0.30)

MP_Ofen = MP.Appliance(MP,1,2150,2,60,0.1,60,occasional_use= 1,thermal_P_var = 0.2)
MP_Ofen.windows([420,780],[1080,1200],0.15)