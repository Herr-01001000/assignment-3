"""Exercise 3"""

import pandas as pd
import numpy as np



# Task 3: Load the chs_data.
# Import Data.
chs = pd.read_stata('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/chs_data.dta')

# Extract a list of childids with no duplicates.
childids = chs.childid.unique().tolist()

# Discard observations in which year is not in range(1986, 2011, 2).
selected_years = list(range(1986, 2011, 2))
chs = chs[chs.year.isin(selected_years)]



# Task 4: Clean and transform the bpi dataset.
# Load the bpi dataset.
bpi = pd.read_stata('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/BEHAVIOR_PROBLEMS_INDEX.dta')

# Drop obserbations with the childids list.
bpi = bpi[bpi.C0000100.isin(childids)]

# Replace all negative numbers by pd.np.nan
bpi.replace(bpi[bpi<0], pd.np.nan)





