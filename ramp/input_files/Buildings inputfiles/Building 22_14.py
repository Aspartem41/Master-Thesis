# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 06:50:33 2024

@author: Romit
"""

"For Winter sem - Exam"

from ramp.core.core import Room, np
Room_list = []

# Timeframes
t0 = [0,0]
t1 = [480,1320]  # 
# t2 = [960,1320] #

# t21 = [0,480]
# t3 = [1080,1200] # for Lamp (5:00 PM - 8:00 PM)


# Variability factors
v0 = 0.1   # For timeframes

# ----------------------------------------------------------------------------------------------------------------------------------

# Sports Hall

SPH = Room("Sports hall",100,3)
Room_list.append(SPH)

v1 = 0.25  # For total time of SPH

# lights - Weekdays
SPH_lights = SPH.Appliance(SPH,90,36,2,480,v1,90, fixed = 'yes', occasional_use = 0.6, wd_we_type = 0)
SPH_lights.windows(t1,t0,v0)

# lights - Weekends
SPH_lights = SPH.Appliance(SPH,90,36,2,120,v1,90, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
SPH_lights.windows(t1,t0,v0)

# Plug load - Weekdays

# plug load - Weekends

# ----------------------------------------------------------------------------------------------------------------------------------

# Hallway

HC = Room("Hallway/Corridor",100,3)
Room_list.append(HC)

v1 = 0.25   # For total time of HW

# lights - Weekdays
HC_lights = HC.Appliance(HC,4,36,2,480,v1,90, fixed = 'yes', occasional_use = 0.6, wd_we_type = 0)
HC_lights.windows(t1,t0,v0)

# lights - Weekends
HC_lights = HC.Appliance(HC,4,36,2,120,v1,90, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
HC_lights.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

DR_m = Room("Dressing room - male",100,3)
Room_list.append(DR_m)

v1 = 0.25   # For total time of DR_m

# lights - Weekdays
DR_m_lights = DR_m.Appliance(DR_m,7,36,2,480,v1,90, fixed = 'yes', occasional_use = 0.6, wd_we_type = 0)
DR_m_lights.windows(t1,t0,v0)

# lights - Weekends
DR_m_lights = DR_m.Appliance(DR_m,7,36,2,120,v1,90, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
DR_m_lights.windows(t1,t0,v0)

# Plug load - Weekdays
DR_m_Mobile = DR_m.Appliance(DR_m,4,20,2,60,v0,30, occasional_use = 0.5, wd_we_type = 0)
DR_m_Mobile.windows(t1,t0,v0)

# plug load - Weekends
DR_m_Mobile = DR_m.Appliance(DR_m,2,20,2,60,v0,30, occasional_use = 0.4, wd_we_type = 1)
DR_m_Mobile.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

DR_f = Room("Dressing room - female",100,3)
Room_list.append(DR_f)

v1 = 0.25   # For total time of DR_m

# lights - Weekdays
DR_f_lights = DR_f.Appliance(DR_f,7,36,2,480,v1,90, fixed = 'yes', occasional_use = 0.6, wd_we_type = 0)
DR_f_lights.windows(t1,t0,v0)

# lights - Weekends
DR_f_lights = DR_f.Appliance(DR_f,7,36,2,120,v1,90, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
DR_f_lights.windows(t1,t0,v0)

# Plug load - Weekdays
DR_f_Mobile = DR_f.Appliance(DR_f,4,20,2,60,v0,30, occasional_use = 0.5, wd_we_type = 0)
DR_f_Mobile.windows(t1,t0,v0)

# plug load - Weekends
DR_f_Mobile = DR_f.Appliance(DR_f,2,20,2,60,v0,30, occasional_use = 0.4, wd_we_type = 1)
DR_f_Mobile.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

SR = Room("Refree room",100,3)
Room_list.append(SR)

v1 = 0.25   # For total time of SR

# lights - Weekdays
SR_lights = SR.Appliance(SR,2,36,2,480,v1,90, fixed = 'yes', occasional_use = 0.6, wd_we_type = 0)
SR_lights.windows(t1,t0,v0)

# lights - Weekends
SR_lights = SR.Appliance(SR,2,36,2,120,v1,90, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
SR_lights.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

WC_m = Room("Toilet & Shower - male",100,3)
Room_list.append(WC_m)

v1 = 0.25   # For total time of WC_m

# lights - Weekdays
WC_m_lights = WC_m.Appliance(WC_m,3,36,2,180,v1,5, occasional_use = 0.6, wd_we_type = 0)
WC_m_lights.windows(t1,t0,v0)

# lights - Weekends
WC_m_lights = WC_m.Appliance(WC_m,3,36,2,45,v1,5, occasional_use = 0.4, wd_we_type = 1)
WC_m_lights.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

WC_f = Room("Toilet & Shower - female",100,3)
Room_list.append(WC_f)

v1 = 0.25   # For total time of WC_f

# lights - Weekdays
WC_f_lights = WC_f.Appliance(WC_f,3,36,2,180,v1,5, occasional_use = 0.6, wd_we_type = 0)
WC_f_lights.windows(t1,t0,v0)

# lights - Weekends
WC_f_lights = WC_f.Appliance(WC_f,3,36,2,45,v1,5, occasional_use = 0.4, wd_we_type = 1)
WC_f_lights.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

STR_1 = Room("Sports teacher room 1",100,3)
Room_list.append(STR_1)

v1 = 0.25   # For total time of STR_1

# lights - Weekdays
STR_1_lights = STR_1.Appliance(STR_1,3,36,2,120,v1,30, occasional_use = 0.6, wd_we_type = 0)
STR_1_lights.windows(t1,t0,v0)

# lights - Weekends
STR_1_lights = STR_1.Appliance(STR_1,3,36,2,30,v1,30, occasional_use = 0.4, wd_we_type = 1)
STR_1_lights.windows(t1,t0,v0)

# Plug load - Weekdays
STR_1_Mobile =STR_1.Appliance(STR_1,1,20,2,60,v0,30, occasional_use = 0.5, wd_we_type = 0)
STR_1_Mobile.windows(t1,t0,v0)

# plug load - Weekends
STR_1_Mobile = STR_1.Appliance(STR_1,1,20,2,60,v0,30, occasional_use = 0.4, wd_we_type = 1)
STR_1_Mobile.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

STR_2 = Room("Sports teacher room 2",100,3)
Room_list.append(STR_2)

v1 = 0.25   # For total time of STR_2

# lights - Weekdays
STR_2_lights = STR_2.Appliance(STR_2,3,36,2,120,v1,30, occasional_use = 0.6, wd_we_type = 0)
STR_2_lights.windows(t1,t0,v0)

# lights - Weekends
STR_2_lights = STR_2.Appliance(STR_2,3,36,2,30,v1,30, occasional_use = 0.4, wd_we_type = 1)
STR_2_lights.windows(t1,t0,v0)

# Plug load - Weekdays
STR_2_Mobile = STR_2.Appliance(STR_2,1,20,2,60,v0,30, occasional_use = 0.5, wd_we_type = 0)
STR_2_Mobile.windows(t1,t0,v0)

# plug load - Weekends
STR_2_Mobile = STR_2.Appliance(STR_2,1,20,2,60,v0,30, occasional_use = 0.4, wd_we_type = 1)
STR_2_Mobile.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

HT_1 = Room("House technik 1",100,3)
Room_list.append(HT_1)

v1 = 0.25   # For total time of HT_1

# lights - Weekdays
HT_1_lights = HT_1.Appliance(HT_1,3,36,2,60,v1,5, occasional_use = 0.1, wd_we_type = 0)
HT_1_lights.windows(t1,t0,v0)

# lights - Weekends

# ----------------------------------------------------------------------------------------------------------------------------------

HT_2 = Room("House technik 2",100,3)
Room_list.append(HT_2)

v1 = 0.25   # For total time of HT_2

# lights - Weekdays
HT_2_lights = HT_2.Appliance(HT_2,3,36,2,60,v1,5, occasional_use = 0.1, wd_we_type = 0)
HT_2_lights.windows(t1,t0,v0)

# lights - Weekends

# ----------------------------------------------------------------------------------------------------------------------------------

TE_1 = Room("Technik 1",100,3)
Room_list.append(TE_1)

v1 = 0.25   # For total time of TE_1

# lights - Weekdays
TE_1_lights = TE_1.Appliance(TE_1,1,36,2,60,v1,5, occasional_use = 0.1, wd_we_type = 0)
TE_1_lights.windows(t1,t0,v0)

# lights - Weekends

# ----------------------------------------------------------------------------------------------------------------------------------

PUM = Room("PUMI",100,3)
Room_list.append(PUM)

v1 = 0.25   # For total time of PUM

# lights - Weekdays
PUM_lights = PUM.Appliance(PUM,1,36,2,60,v1,5, occasional_use = 0.1, wd_we_type = 0)
PUM_lights.windows(t1,t0,v0)

# lights - Weekends

# ----------------------------------------------------------------------------------------------------------------------------------

ES_1 = Room("Equipment storage 1",100,3)
Room_list.append(ES_1)

v1 = 0.25   # For total time of ES_1

# lights - Weekdays
ES_1_lights = ES_1.Appliance(ES_1,7,36,2,30,v1,5, fixed = 'yes', occasional_use = 0.4, wd_we_type = 0)
ES_1_lights.windows(t1,t0,v0)

# lights - Weekends
ES_1_lights = ES_1.Appliance(ES_1,7,36,2,15,v1,5, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
ES_1_lights.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

ES_2 = Room("Equipment storage 2",100,3)
Room_list.append(ES_2)

v1 = 0.25   # For total time of ES_2

# lights - Weekdays
ES_2_lights = ES_2.Appliance(ES_2,3,36,2,30,v1,5, fixed = 'yes', occasional_use = 0.4, wd_we_type = 0)
ES_2_lights.windows(t1,t0,v0)

# lights - Weekends
ES_2_lights = ES_2.Appliance(ES_2,3,36,2,15,v1,5, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
ES_2_lights.windows(t1,t0,v0)

# ----------------------------------------------------------------------------------------------------------------------------------

ES_3 = Room("Equipment storage 3",100,3)
Room_list.append(ES_3)

v1 = 0.25   # For total time of ES_3

# lights - Weekdays
ES_3_lights = ES_3.Appliance(ES_3,4,36,2,30,v1,5, fixed = 'yes', occasional_use = 0.4, wd_we_type = 0)
ES_3_lights.windows(t1,t0,v0)

# lights - Weekends
ES_3_lights = ES_3.Appliance(ES_3,4,36,2,15,v1,5, fixed = 'yes', occasional_use = 0.4, wd_we_type = 1)
ES_3_lights.windows(t1,t0,v0)