"""Exercise 3"""

import pandas as pd



# Task 3
# Import Data.
chs = pd.read_stata('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/chs_data.dta')

# Extract a list of childids with no duplicates.
childids = chs.childid.unique()

