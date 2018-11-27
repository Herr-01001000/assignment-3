"""Exercise 3"""

import pandas as pd



# Task 3
# Import Data.
chs = pd.read_stata('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/chs_data.dta')

# Extract a list of childids with no duplicates.
childids = chs.childid.unique().tolist()

# Discard observations in which year is not in range(1986, 2011, 2)
year = list(range(1986, 2011, 2))

# Define the is_in function as the filer condition
def is_in(year):

    
ids_year = list(filter(is_in, childids))

