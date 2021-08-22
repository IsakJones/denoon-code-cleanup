# %%

import os
import re
# %%
os.listdir()
# %%
print("Hello, World!")
# %%

try:
    x = 100 / 0
except Exception as e:
    print(e)
    print(type(e))
    print("zero" in str(e))
    print(ZeroDivisionError == type(e))
# %%
text = "ISO-alpha3 code"
pattern = re.compile(r"\s*([A-Z]{3})\s*")

print(re.match(pattern, text))
# %%
country_name = "Korea (the Democratic Republic of)"
pattern_country_name_alt = re.compile(r"^\s*([\w| ]+)\s*\([t|h|e]{3}?\s*([\w| ]+)\)\s*$")
if "(" in country_name:
    country_name = pattern_country_name_alt.sub(r"\2 \1", country_name)
print(country_name)
# %%
import pandas as pd

df = pd.DataFrame({"First": [30, 31, 32],
                   "Second": [10, 11, 12],
                   "Third": [100, 101, 102]})
df.set_index("First", inplace=True)
filt = df["Second"] == 11

print(df[filt])
print(df[filt].index)


# %%
import pandas as pd

df = pd.read_csv("countryTableComplete.csv")
filt = df["UN"] == True

new_df = df[filt]
# %%
import pandas as pd

un_df = pd.read_csv("master_us_df.csv", header=0)

print(type(un_df["date"][0]))
filt = un_df["date"] == "2020-11-01"

outliers = []
for country in un_df.columns:
    if un_df.loc[202, country] != 100:
        outliers.append(country)
        
print(outliers)
# %%
print(len(outliers))
# %%
import numpy as np
d = {}
for country in un_df.columns:
    d[country] = np.array(un_df[country][72:])

new_outliers = []
for country in un_df.columns:
    if np.max(d[country]) != d[country][130]:
        new_outliers.append(country)
        
print(new_outliers)
# %%
master_df = pd.read_csv("countryTable.csv")
print(master_df[master_df["UN"] == True].shape)
# %%
