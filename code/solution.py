"""Exercise 3"""

import pandas as pd
import numpy as np




# Task 3: Load the chs_data.
# Import Data.
chs = pd.read_stata('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/chs_data.dta')

# Extract a list of childids with no duplicates.
childids = chs.childid.unique().tolist()

# Discard observations in which year is not in range(1986, 2011, 2).
chs = chs[chs.year.isin(list(range(1986, 2011, 2)))]





# Task 4: Clean and transform the bpi dataset.
# Load the bpi dataset.
bpi = pd.read_stata('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/BEHAVIOR_PROBLEMS_INDEX.dta')

# Drop obserbations with the childids list.
bpi = bpi[bpi.C0000100.isin(childids)]

# Replace all negative numbers by pd.np.nan.
# bpi.replace(bpi[bpi<0], pd.np.nan)
bpi.replace(-7, np.nan, inplace=True)
bpi.replace(-3, np.nan, inplace=True)
bpi.replace(-2, np.nan, inplace=True)
bpi.replace(-1, np.nan, inplace=True)

# Create a dictionary.
# Import the bpi variable information file.
info = pd.read_csv('d:/Eriko-/prog-econ-sandbox/assignment-3-group_7/bld/bpi_variable_info.csv')

# Discard all variables that are not present in bpi_variable_info.csv.
bpi = bpi[info.nlsy_name.tolist()].T

# Add a column called year, which indicates the surevey year.
bpi['year'] = info.set_index('nlsy_name')['survey_year']

# Add the readable names as a column, then set them as the new index.
bpi['readable_name'] =  info.set_index('nlsy_name')['readable_name']
bpi = bpi.set_index('readable_name', drop=True)

# Create a dictionary where the keys are the survey years (years 1986 - 2010).
bpi_dict = {}
bpi_dict.fromkeys(info.survey_year[3:].tolist())

info_dict = info.set_index('nlsy_name')['readable_name'].T.to_dict()

temp1 = bpi.T[info[info.survey_year == info.survey_year.unique()[0]]['readable_name']]
for i in range(1, len(bpi.year.unique())):
    temp1['year'] = info.survey_year.unique()[i]
    temp2 = bpi.T[info[info.survey_year == info.survey_year.unique()[i]]['readable_name']]
    temp = pd.concat([temp1,temp2], axis=1) 
    temp = temp.rename(columns=info_dict)
    bpi_dict[info.survey_year.unique()[i]] = temp
    
    
    
    
# Task 5: Generate a new bpi dataset in long format.
bpi_long = bpi.T









    
    




