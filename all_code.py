# %%
import pandas as pd
import numpy as np

# %% 
# 7 - a - ii
countryTable = pd.read_csv("countryTableComplete.csv")

np_mult = np.array(countryTable["Mult"].dropna())
print(np.count_nonzero(np_mult < 3))

# %%
# 7 - b - ii - 1 Bar plot

# %%
# 7 - D - i hourly_scraper.py