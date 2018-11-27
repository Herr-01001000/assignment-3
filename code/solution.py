import pandas as pd
import numpy as np

# Task 3: Load the chs_data. Extract a list of childids that contains all values that variable takes in the chs_data, but no duplicates. Also, discard all observations in which year is not in list(range(1986, 2011, 2))
chs_data = pd.read_stata('../original_data/chs_data.dta')

list_1 = chs_data.childid.drop_duplicates(keep='first', inplace=False)

chs_data_1 = chs_data[chs_data['year'].isin(list(range(1986, 2011, 2)))]

# Task 4: Clean and transform the bpi dataset.

# Load the bpi dataset.
bpi = pd.read_stata('../original_data/BEHAVIOR_PROBLEMS_INDEX.dta')

# Use the list of childids to only keep observations that are present in the chs_data.
bpi_1 = bpi[bpi.C0000100.isin(list_1)]

# Replace all negative numbers by pd.np.nan.
bpi_1.replace(bpi_1[bpi_1<0], np.nan, inplace = True)

# Create a dictionary where the keys are the survey years and the values are DataFrames with the bpi data of that year.
bpi_2 = pd.read_csv('../original_data/bpi_variable_info.csv')
bpi = bpi[bpi_2.nlsy_name.tolist()]
info_dict = bpi_2.set_index('nlsy_name')['readable_name'].T.to_dict()

bpi_dict = {}
bpi_dict.fromkeys(bpi_2.survey_year[3:].tolist())
temp1 = bpi[bpi_2[bpi_2.survey_year == bpi_2.survey_year.unique()[0]]['nlsy_name']]
for i in range(1,len(bpi_2.survey_year.unique())):     
    temp1['year'] = bpi_2.survey_year.unique()[i]
    temp2 = bpi[bpi_2[bpi_2.survey_year == bpi_2.survey_year.unique()[i]]['nlsy_name']]
    temp = pd.concat([temp1,temp2], axis=1) 
    temp = temp.rename(columns=info_dict)
    bpi_dict[bpi_2.survey_year.unique()[i]] = temp