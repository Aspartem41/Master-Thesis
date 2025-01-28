# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:08:20 2023

@author: Romit
"""


from ramp.core.core import User, np
User_list = []

SH = User("Seminar Hall",10,3)
User_list.append(SH)

LH = User("Lecture Hall",1,3)
User_list.append(LH)

LAB = User("Laboratory",1,3)
User_list.append(LAB)

OFF_1p = User("Faculty Office - 1 Person",1,3)
User_list.append(OFF_1p)

OFF_2p = User("Faculty Office - 2 Person",1,3)
User_list.append(OFF_2p)

OFF_5p = User("Faculty Office - 5 Person",1,3)
User_list.append(OFF_5p)

STR = User("Stairwells",1,3)
User_list.append(STR)

HC_gf = User("Hallways & Corridors - Ground Floor",1,3)
User_list.append(HC_gf)

HC_ff = User("Hallways & Corridors - First Floor",1,3)
User_list.append(HC_ff)

EL = User("Elevator",1,3)
User_list.append(EL)

WC = User("Toilet",1,3)
User_list.append(WC)

# Timeframes
t0 = [0,0]
t1 = [480,1080]  # Working hours ( 8:00 AM - 6:00 PM)
t2 = [1080,1440] # both t2 and t21 for hallways lights
t21 = [0,480] 
t3 = [1080,1200] # for Lamp (5:00 PM - 8:00 PM)


# Variability factors
v1 = 0.1
v2 = 0.2   # For projector,laptop and For duty cycles
#%%

# Seminar Hall

# SH_projector = SH.Appliance(SH,1,350,1,180,v2,90, wd_we_type = 0, occasional_use = 0.15)
# SH_projector.windows(t1,t0,v1)

# SH_projector = SH.Appliance(SH,1,350,1,120,v1,60, wd_we_type = 1, occasional_use = 0.2)
# SH_projector.windows(t1,t0,v1)

# SH_Lap = SH.Appliance(SH,1,300,1,60,v2,60, wd_we_type = 0, occasional_use = 0.15)
# SH_Lap.windows(t1,t0,v1)

# SH_Lap = SH.Appliance(SH,1,300,1,120,v1,60, wd_we_type = 1, occasional_use = 0.2)
# SH_Lap.windows(t1,t0,v1)
 
SH_Lights= SH.Appliance(SH,20,36,1,60,v2,60, wd_we_type = 0, occasional_use = 0.15)
SH_Lights.windows(t1,t0,v1)

# SH_Lights= SH.Appliance(SH,2,36,1,120,v1,60, wd_we_type = 1, occasional_use = 0.2)
# SH_Lights.windows(t1,t0,v1)



# # Lecture Hall

# LH_projector = LH.Appliance(LH,1,350,1,270,v1,90, wd_we_type = 0)
# LH_projector.windows(t1,t0,v1)

# LH_Comp = LH.Appliance(LH,1,550,1,270,v1,90, wd_we_type = 0)
# LH_Comp.windows(t1,t0,v1)

# LH_Lap = LH.Appliance(LH,1,300,1,270,v1,90, wd_we_type = 0)
# LH_Lap.windows(t1,t0,v1)

# LH_Lights= LH.Appliance(LH,18,36,1,150,v1,90, wd_we_type = 0, occasional_use = 0.8)
# LH_Lights.windows(t1,t0,v1)




# # # Laboratory 




# # # 1 Person Office

# OFF_1p_Comp = OFF_1p.Appliance(OFF_1p,1,550,1,480,v1,480, fixed_cycle = 1, wd_we_type = 0)
# OFF_1p_Comp.windows(t1,t0,v1)
# OFF_1p_Comp.specific_cycle_1(550,360,45,120,v2)
# OFF_1p_Comp.cycle_behaviour(t1,t0)

# OFF_1p_Lap = OFF_1p.Appliance(OFF_1p,1,300,1,180,v1,120, occasional_use = 0.4, wd_we_type = 0)
# OFF_1p_Lap.windows(t1,t0,v1)

# OFF_1p_Moni = OFF_1p.Appliance(OFF_1p,1,120,1,480,v1,480, wd_we_type = 0)
# OFF_1p_Moni.windows(t1,t0,v1)
# OFF_1p_Moni.specific_cycle_1(120,360,10,120,v2)
# OFF_1p_Moni.cycle_behaviour(t1,t0)

# OFF_1p_Lamp = OFF_1p.Appliance(OFF_1p,1,10,1,120,v1,120, occasional_use = 0.2, wd_we_type = 0)
# OFF_1p_Lamp.windows(t3,t0,0)

# OFF_1p_Lights = OFF_1p.Appliance(OFF_1p,2,36,1,180,v1,180, wd_we_type = 0)
# OFF_1p_Lights.windows(t1,t0,v1)

# OFF_1p_Mobile = OFF_1p.Appliance(OFF_1p,1,20,1,120,v1,60, occasional_use = 0.8, wd_we_type = 0)
# OFF_1p_Mobile.windows(t1,t0,v1)

# OFF_1p_Printer = OFF_1p.Appliance(OFF_1p,1,300,1,600,v1,600, fixed_cycle = 1, occasional_use = 0.5, wd_we_type = 0)
# OFF_1p_Printer.windows(t1,t0,v1)
# OFF_1p_Printer.specific_cycle_1(300,15,10,585,v2)
# OFF_1p_Printer.cycle_behaviour(t1,t0)



# # 2 Person Office

# OFF_2p_Comp = OFF_2p.Appliance(OFF_2p,2,550,1,480,v1,480, fixed_cycle = 1, wd_we_type = 0)
# OFF_2p_Comp.windows(t1,t0,v1)
# OFF_2p_Comp.specific_cycle_1(550,360,45,120,v2)
# OFF_2p_Comp.cycle_behaviour(t1,t0)

# OFF_2p_Lap = OFF_2p.Appliance(OFF_2p,2,300,1,180,v1,120, occasional_use = 0.4, wd_we_type = 0)
# OFF_2p_Lap.windows(t1,t0,v1)

# OFF_2p_Moni = OFF_2p.Appliance(OFF_2p,4,120,1,480,v1,480, wd_we_type = 0)
# OFF_2p_Moni.windows(t1,t0,v1)
# OFF_2p_Moni.specific_cycle_1(120,360,10,120,v2)
# OFF_2p_Moni.cycle_behaviour(t1,t0)

# OFF_2p_Lights = OFF_2p.Appliance(OFF_2p,6,36,1,180,v1,180, wd_we_type = 0)
# OFF_2p_Lights.windows(t1,t0,v1)

# OFF_2p_Lamp = OFF_2p.Appliance(OFF_2p,1,10,1,120,v1,120, occasional_use = 0.2, wd_we_type = 0)
# OFF_2p_Lamp.windows(t3,t0,0)

# OFF_2p_Mobile = OFF_2p.Appliance(OFF_2p,2,20,1,120,v1,60, occasional_use = 0.8,  wd_we_type = 0)
# OFF_2p_Mobile.windows(t1,t0,v1)



# # 5 Person Office

# OFF_5p_Comp = OFF_5p.Appliance(OFF_5p,5,50,1,540,v1,540, fixed_cycle = 1, wd_we_type = 0)
# OFF_5p_Comp.windows(t1,t0,v1)
# OFF_5p_Comp.specific_cycle_1(550,420,45,120,v2)
# OFF_5p_Comp.cycle_behaviour(t1,t0)

# OFF_5p_Lap = OFF_5p.Appliance(OFF_5p,5,300,1,180,v1,120, occasional_use = 0.4, wd_we_type = 0)
# OFF_5p_Lap.windows(t1,t0,v1)

# OFF_5p_Moni = OFF_5p.Appliance(OFF_5p,10,50,1,540,v1,540, fixed_cycle = 1, wd_we_type = 0)
# OFF_5p_Moni.windows(t1,t0,v1)
# OFF_5p_Comp.specific_cycle_1(120,420,10,120,v2)
# OFF_5p_Comp.cycle_behaviour(t1,t0)

# OFF_5p_Lights = OFF_5p.Appliance(OFF_5p,6,36,1,540,v1,540, wd_we_type = 0)
# OFF_5p_Lights.windows(t1,t0,v1)

# OFF_5p_Lights = OFF_5p.Appliance(OFF_5p,6,36,1,540,v1,540, occasional_use = 0.4, wd_we_type = 0)
# OFF_5p_Lights.windows(t1,t0,v1)

# OFF_5p_Mobile = OFF_5p.Appliance(OFF_5p,5,20,1,120,v1,60, occasional_use = 0.8, wd_we_type = 0)
# OFF_5p_Mobile.windows(t1,t0,v1)

# OFF_5p_Lamp = OFF_2p.Appliance(OFF_5p,5,10,1,120,v1,120, occasional_use = 0.2, wd_we_type = 0)
# OFF_5p_Lamp.windows(t3,t0,0)

# # Hallways & Corridors - Ground Floor

# HC_gf_Lights= HC_gf.Appliance(HC_gf,11,36,2,120,v1,5, wd_we_type = 0)
# HC_gf_Lights.windows(t2,t21,v1)



# # Hallways & Corridors - First Floor

# HC_ff_Lights= HC_ff.Appliance(HC_ff,11,36,2,120,v1,5, wd_we_type = 0)
# HC_ff_Lights.windows(t2,t21,v1)


# # Stairwells

# STR_Lights = STR.Appliance(STR,2,36,2,120,v1,5, wd_we_type = 0)
# STR_Lights.windows(t2,t21,v1)

# # # Elevator



# # Toilets

# WC_H_D_Lights= WC.Appliance(WC,6,36,1,45,v1,5, occasional_use = 0.5, wd_we_type = 0)
# WC_H_D_Lights.windows(t2,t0,v1)

# WC_N_Lights= WC.Appliance(WC,1,36,1,45,v1,5, occasional_use = 0.5, wd_we_type = 0)
# WC_N_Lights.windows(t2,t0,v1)