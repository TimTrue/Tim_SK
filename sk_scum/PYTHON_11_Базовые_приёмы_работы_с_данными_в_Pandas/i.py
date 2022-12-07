import pandas as pd
import numpy as np

def get_short_street_type(street_types):
    exclude_long_list = ['AA', 'BB', 'CC']
    exclude_short_list = ['A', 'B', 'C']
    for i in range(len(street_types)):
        for j in range(len(exclude_long_list)):
            if street_types.iloc[i] == exclude_long_list[j]:
                street_types.iloc[i] = exclude_short_list[j]
    return street_types

street_types = pd.Series(
    data = ['AA', 'A', 'AA', 'BB', 'B', 'CC', 'C'],
    name = 'street_types'
)
print(get_short_street_type(street_types))