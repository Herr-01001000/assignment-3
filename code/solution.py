"""Exercise 3 Solution - Data Management and Plotting."""


# Task 3: Load the chs_data.
# Import Packages.
import numpy as np
import pandas as pd
#import warnings
#warnings.filterwarnings("ignore")

# Import Data.
chs = pd.read_stata('../original_data/chs_data.dta')

# Extract a list of childids that contains all values that takes in the chs_data.
childids = chs.childid.unique().tolist()

# Discard all observations which are not in the specific years.
chs = chs[chs.year.isin(list(range(1986, 2011, 2)))]




    
    




