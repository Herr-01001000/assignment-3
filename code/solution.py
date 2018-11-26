import pandas as pd
import numpy as np

chs_data = pd.read_stata('../original_data/chs_data.dta')
list_1 = chs_data.childid.drop_duplicates(keep='first', inplace=False)
chs_data_1 = chs_data[chs_data['year'].isin(list(range(1986, 2011, 2)))]