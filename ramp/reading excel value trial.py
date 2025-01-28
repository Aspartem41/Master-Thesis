# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:48:58 2024

@author: vrush
"""

import pandas as pd
# from ramp.core.core import Room, np
# Room_list = []

# N = 100   # Total number of Seminar Hall to be considered

# SH = Room("Seminar Hall",N,3)
# Room_list.append(SH)
import pandas as pd
df = pd.read_excel('input_files/Room inputfiles/Office 2P/Office 2P.xlsx', sheet_name = 'WS_Break' , index_col=0)

ntf = 2
nl = df.loc['Light','Number']
ap = df.loc['Light','AP (W)']
tt_wd = df.loc['Light','TT-WD (mins)']
mt_wd = df.loc['Light','MT-WD (mins)' ]
tt_we = df.loc['Light','TT-WE (mins)']
mt_we = df.loc['Light','MT-WE (mins)']

# Lights - Weekdays
# OFF_2P_Lights = OFF_2P.Appliance(OFF_2P,nl,ap,ntf,tt_wd,v0,mt_wd, wd_we_type = 0, occasional_use = 0.6)
# OFF_2P_Lights.windows(t1,t0,v0)

print(nl)
print(tt_wd)
print(tt_we)
print(mt_wd)
print(mt_we)
print(ap)