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

#Discard all observations which are not in the specific years.
chs = chs[chs.year.isin(list(range(1986, 2011, 2)))]


# Task 4: Clean and transform the bpi dataset.
# Load the bpi dataset.
bpi = pd.read_stata('../original_data/BEHAVIOR_PROBLEMS_INDEX.dta')

# Keep observations that are present in the chs_data.
bpi = bpi[bpi.C0000100.isin(childids)]

# Replace all negative numbers to NaN.
bpi.replace(-7, np.nan, inplace=True)
bpi.replace(-3, np.nan, inplace=True)
bpi.replace(-2, np.nan, inplace=True)
bpi.replace(-1, np.nan, inplace=True)

#print(bpi[bpi<0].count().min())  # Check if there is any negative number left.

# Create a dictionary for bpi dataset.
# Import bpi variables information.
info = pd.read_csv('../original_data/bpi_variable_info.csv')  

# Discard all variables that are not present in bpi_variable_info.csv.
bpi = bpi[info.nlsy_name.tolist()]

# Build a dictionary to map readable names to nlsy names.
info_dict = info.set_index('nlsy_name')['readable_name'].T.to_dict()

# Create the dictionary for bpi dataset where the keys are the survey years.
bpi_dict = {}
bpi_dict.fromkeys(info.survey_year[3:].tolist())

# Put data of the corresponding survey year into the value of the key.
temp1 = bpi[info[info.survey_year == info.survey_year.unique()[0]]['nlsy_name']]
for i in range(1,len(info.survey_year.unique())):     
    temp1['year'] = info.survey_year.unique()[i]
    temp2 = bpi[info[info.survey_year == info.survey_year.unique()[i]]['nlsy_name']]
    temp = pd.concat([temp1,temp2], axis=1) 
    temp = temp.rename(columns=info_dict)
    bpi_dict[info.survey_year.unique()[i]] = temp
    

