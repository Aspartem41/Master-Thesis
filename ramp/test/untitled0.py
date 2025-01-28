# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:06:03 2024

@author: vrush
"""
import pandas as pd
import numpy as np

# Your modified my_list
my_list = [
    {'custom_name_1': [np.array([1, 2, 3, 4])], 'custom_name_2': [np.array([5, 6, 7, 8])]},
    {'custom_name_3': [np.array([9, 10, 11, 12])], 'custom_name_4': [np.array([13, 14, 15, 16])]}
]

# Create a DataFrame
df = pd.DataFrame()

# Iterate through each element in my_list
for i, data_dict in enumerate(my_list, start=1):
    for key, value in data_dict.items():
        # Add main column
        main_col = f'Day_{i}'
        
        # If the array has named columns
        if value[0].dtype.names:
            sub_col_names = list(value[0].dtype.names)
            for sub_col_name in sub_col_names:
                # Add sub-column with indexing
                df[f'{main_col}_{key}_{sub_col_name}'] = value[0][sub_col_name]
        else:
            # If the array does not have named columns, add values directly
            for j, val in enumerate(value[0]):
                df.at[j, f'{main_col}_{key}'] = val

# Display the DataFrame
print(df)

