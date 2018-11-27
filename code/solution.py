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
    

#Task 5: Generate a new bpi dataset in long format.
bpi_long = bpi_dict['1986']
for i in bpi_dict.keys():
    bpi_long = bpi_long.merge(bpi_dict[i], how='outer')
    
# Save the long format dataset as a comma separated file.
bpi_long.to_csv('../bld/bpi_long.csv')


# Task 6: Merge the long dataset with the chs dataset.
# Change the data type of year in bpi_long to match the data type in chs.
bpi_long['year']=bpi_long['year'].astype(np.int16)

bpi_merged = pd.merge(chs, bpi_long, how='left', on=['childid', 'year'], suffixes=('_chs', '_long'))
bpi_merged.to_csv('../bld/bpi_merged.csv')


# Task 7: Calculate scores for each subscale of the bpi.
# Change the data type of birth_order in order to use replace function later.
bpi_final = bpi_merged
bpi_final['birth_order']=bpi_final['birth_order'].astype(object)

# Replace the answers with numbers.
bpi_final.replace(r'SOMETIMES TRUE', 1, inplace=True)
bpi_final.replace(r'Sometimes True', 1, inplace=True)
bpi_final.replace(r'Sometimes true', 1, inplace=True)
bpi_final.replace(r'OFTEN TRUE', 1, inplace=True)
bpi_final.replace(r'Often True', 1, inplace=True)
bpi_final.replace(r'Often true', 1, inplace=True)
bpi_final.replace(r'NOT TRUE', 0, inplace=True)
bpi_final.replace(r'Not True', 0, inplace=True)
bpi_final.replace(r'Not true', 0, inplace=True)
bpi_final.replace(r'NEVER ATTENDED SCHOOL', np.nan, inplace=True)
bpi_final.replace(r'Never Attended School', np.nan, inplace=True)
bpi_final.replace(r'Child has never attended school', np.nan, inplace=True)

# Separate the data into groups by different ages.
bpi_final = pd.DataFrame(bpi_final, dtype = np.float)
bpi_final = bpi_final.groupby('age').mean()

# Calculate the each subscale score for each group.
import selectnames as sn

antisocial = bpi_final[sn.selectnamesA(list(bpi_final))].mean(1).to_frame('antisocial')
anxiety = bpi_final[sn.selectnamesB(list(bpi_final))].mean(1).to_frame('anxiety')
headstrong = bpi_final[sn.selectnamesC(list(bpi_final))].mean(1).to_frame('headstrong')
hyperactive = bpi_final[sn.selectnamesD(list(bpi_final))].mean(1).to_frame('hyperactive')
peer = bpi_final[sn.selectnamesE(list(bpi_final))].mean(1).to_frame('peer')

# Merge the scores into bpi_final and save it as a csv file.
bpi_final = pd.concat([bpi_final, antisocial, anxiety, headstrong, hyperactive, peer], axis=1)
bpi_final.to_csv('../bld/bpi_final.csv')


# Task 8: Make regression plots for each subscale.
# Replace missing data in chs by NaN.
bpi_final.replace(-100, np.nan, inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

sns.regplot('antisocial', 'bpiA', bpi_final, x_estimator=np.mean, ci=70)
plt.savefig('../bld/regplot_antisocial.png')







