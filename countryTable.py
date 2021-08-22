# %%
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

def countryTable():
    """
    Returns table with country name, alpha2, alpha3, UN membership, G-20 membership
    """
    g_twenty_codes = ["AR",
                      "AU",
                      "BR",
                      "CA",
                      "CN",
                      "FR",
                      "DE",
                      "IN",
                      "ID",
                      "IT",
                      "JP",
                      "KR",
                      "MX",
                      "RU",
                      "SA",
                      "ZA",
                      "TR",
                      "GB",
                      "US"]
    # Two links
    link_un = "https://www.un.org/en/about-us/member-states"
    link_iban = "https://www.iban.com/country-codes"
    # Ensure whitespace elimination
    pattern_country_name = re.compile(r"^\s*([\w| ]+)\s*$")
    # Alt is for country names with parentheses
    pattern_country_name_alt = re.compile(r"^\s*([\w| ]+)\s\((the)?\s*([\w| ]*)\)\s*$")
    pattern_alpha_2 = re.compile(r"^\s*([A-Z]{2})\s*$")
    pattern_alpha_3 = re.compile(r"^\s*([A-Z]{3})\s*$")
    # Retrieve html page
    req_un = requests.get(link_un).text
    req_iban = requests.get(link_iban).text
    soup_un = BeautifulSoup(req_un, 'lxml')
    soup_iban = BeautifulSoup(req_iban, 'lxml')
    # Get the iban table with all the necesary rows
    table_iban = soup_iban.find("table", id="myTable").find("tbody")
    rows_iban = table_iban.find_all("tr")
    # First input worldwide
    list_country_name = []
    list_alpha_2 = []
    list_alpha_3 = []
    list_g_20_membership = []

    for row in rows_iban:
        cells = row.find_all("td")
        # Eliminate whitespace
        country_name = pattern_country_name.sub(r"\1", cells[0].text)
        if "(" in country_name:
            if "(the)" in country_name:
                country_name = pattern_country_name_alt.sub(r"\1", country_name)
            else:
                country_name = pattern_country_name_alt.sub(r"\3 \1", country_name)
        alpha_2 = pattern_alpha_2.sub(r"\1", cells[1].text)
        alpha_3 = pattern_alpha_3.sub(r"\1", cells[2].text)
        # Set membership params
        g_20_membership = alpha_2 in g_twenty_codes
        # Append to columns
        list_country_name.append(country_name)
        list_alpha_2.append(alpha_2)
        list_alpha_3.append(alpha_3)
        list_g_20_membership.append(g_20_membership)
        
    list_country_name.append("Worldwide")
    list_alpha_2.append("")
    list_alpha_3.append("")
    list_g_20_membership.append(True)
    
    # Create resulting df
    dictionary = {"Country": list_country_name,
                  "Alpha_2": list_alpha_2,
                  "Alpha_3": list_alpha_3,
                  "G20": list_g_20_membership}
    
    df = pd.DataFrame(dictionary)
    # df.to_csv("countryTableUgh.csv")
    # df = pd.read_csv("countryTableUgh.csv", header = 0)
    df["UN"] = False
    print(df)
    
    link_un = "https://www.un.org/en/about-us/member-states"
    # Retrieve html page
    req_un = requests.get(link_un).text
    soup_un = BeautifulSoup(req_un, 'lxml')
    # Extract list of UN members
    list_un_member_countries = soup_un.find_all("h2")[1:] # Avoid superfluous
    for un_country in list_un_member_countries:
        # un_country = pattern_country_name.sub("\1", un_country.text)
        un_country = un_country.text
        print(un_country)
        if un_country in list(df["Country"]):
            df.loc[df["Country"] == un_country, "UN"] = True
        else:
            code = input(f"Country: {un_country} - Alpha 3:")
            df.loc[df["Alpha_3"] == code, "UN"] = True
    
    df.loc[df["Country"] == "Worldwide", "UN"] = True
            
    print("Finished")
            
    return df

# %%
tbl = countryTable()
tbl.to_csv("countryTable.csv")


# %%
import pandas as pd
master_df = pd.read_csv("master_us_df.csv")
country_df = pd.read_csv("countryTable.csv")

country_df_filtered = country_df[country_df["UN"] == True]
un_countries = list(country_df_filtered["Country"])
print(len(un_countries))
master_df_countries = list(master_df.columns)


to_drop = []
for country in master_df_countries:
    print(country)
    if country not in un_countries and country != "date":
        print("yes")
        to_drop.append(country)
        
master_df.drop(columns = to_drop, inplace=True)
print(master_df)
master_df.to_csv("master_us_un_df.csv")

# %%
