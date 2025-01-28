# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:23:36 2024

@author: vrush
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create Time-Series Data (Random Example)
np.random.seed(42)  # for reproducibility
dates = pd.date_range(start='2023-01-01', end='2023-01-07', freq='H')
power_consumption = np.random.randint(5, 15, size=len(dates))  # Random hourly consumption

df = pd.DataFrame({'Power': power_consumption}, index=dates)

# Step 2: Add Base Load
base_load = 2  # kW
df['Power'] += base_load
random_variation = np.random.normal(loc=base_load, scale=0.2, size=len(dates))
print(random_variation)

# Step 3: Plotting
fig, ax = plt.subplots(figsize=(10, 5))
df['Power'].plot(ax=ax, kind='line', color='blue', linestyle='-', marker='o')
ax.set_ylabel('Power [kW]')
ax.set_title('Load Profile with Base Load')
plt.grid(True)
plt.show()

# import random
# import numpy as np

# # Assuming App.r_t is some predefined value
# App_r_t = 0.1  # You need to replace this with the actual value

# # Calculate random_var_t
# random_var_t = random.uniform(1 - App_r_t, 1 + App_r_t)
# random_variation = np.random.normal(loc=random_var_t, scale=0.2, size=10)

# print(random_variation)