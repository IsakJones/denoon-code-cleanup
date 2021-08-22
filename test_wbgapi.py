# %%
import wbgapi as wbank

help(wbank)
# %%
df = wbank.economy.DataFrame()
# %%
import pandas as pd

countryTable = pd.read_csv("countryTableComplete.csv")
countryTable = countryTable[countryTable["UN"] == True]
# countryTable.dropna(inplace=True)

isos = list(countryTable["Alpha_3"])
print(len(isos))

# %%
pops = []
ordered_isos = []

for row in wbank.data.fetch("SP.POP.TOTL", economy=isos, time=2004):
    pops.append(row["value"])
    ordered_isos.append(row["economy"])
    
for country, pop in zip(ordered_isos, pops):
    countryTable.loc[countryTable["Alpha_3"] == country, "2004_POP"] = pop
    
print(countryTable)
countryTable.to_csv("countryTable.csv")
    
# %%
for row in wbank.data.fetch("NY.GDP.PCAP.CD", economy=isos, time=2019):
    print(row)
# %%
# %%
for row in wbank.data.fetch("NY.GDP.PCAP.CD", economy=isos, time=2019):
    print(type(row))
    break
# %%
gdps = []
ordered_isos = []

for row in wbank.data.fetch("NY.GDP.PCAP.CD", economy=isos, time=2019):
    gdps.append(row["value"])
    ordered_isos.append(row["economy"])

    
for country, gdppcap in zip(ordered_isos, gdps):
    countryTable.loc[countryTable["Alpha_3"] == country, "GDPPCAP"] = gdppcap

    
# %%
countryTable.drop(columns=["Unnamed: 0", "GDPPCAP"], inplace=True)
# %%
for row in wbank.data.fetch("IT.NET.USER.ZS", economy=isos, time=2004):
    print(row)
# %%
def add_wbank_data(countryTable, fetch_value, economies, time, new_col_name):
    """
    Adds a column of wbank data by country.
    """
    new_vals = []
    ordered_isos = []

    for row in wbank.data.fetch(fetch_value, economy=economies, time=time):
        new_vals.append(row["value"])
        ordered_isos.append(row["economy"])

        
    for iso, new_val in zip(ordered_isos, new_vals):
        countryTable.loc[countryTable["Alpha_3"] == iso, new_col_name] = new_val
        
    return None

add_wbank_data(countryTable, fetch_value="IT.NET.USER.ZS", economies=isos, time=2004, new_col_name="2004_IT_USAGE")
# %%
countryTable.drop(columns=["2004_IT_USAGE"], inplace=True)
# %%
usages = []
ordered_isos = []

for row in wbank.data.fetch("SP.POP.TOTL", economy=isos, time=2019):
    usages.append(row["value"])
    ordered_isos.append(row["economy"])

    
for iso, usage in zip(ordered_isos, usages):
    countryTable.loc[countryTable["Alpha_3"] == iso, "2004_IT_USAGE"] = gdppcap