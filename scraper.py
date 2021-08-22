"""
DOCSTRING

This is the project I'm doing for Denoon's class.
"""
# %%
import re
import pandas as pd
from matplotlib import pyplot as plt
from pytrends.request import TrendReq

def monthly_us_scraper(UN=False):
    us_topic_id = ["/m/09c7w0"] # To capture US topic not just search term
    country_table = pd.read_csv("countryTable.csv")

    if UN:
        country_table = country_table[country_table["UN"] == True]
        
    temp_df_list = []
    master_us_pytrends = TrendReq(hl='en-US', tz=360)

    for country_name, code in zip(country_table["Country"], country_table["Alpha_2"]):
        # Print to track country
        print(country_name)
        # Get data, handle exception if country is not found
        try:
            master_us_pytrends.build_payload(us_topic_id,
                                             timeframe = "all",
                                             geo=code)
        except Exception as e:
            if "Google returned a response with code 400" in str(e):
                print("Caught 400")
                continue
            else:
                raise(e)
        temp_df = master_us_pytrends.interest_over_time()
        # Drop irrelevant column, check if the dataset is empty
        try:
            temp_df.drop(columns="isPartial", inplace=True)
        except KeyError:
            if len(temp_df) == 0:
                continue
        # Rename the values column as the country column
        temp_df.columns = [country_name]
        # Add the results to the list of dfs
        temp_df_list.append(temp_df)

    # Concatenate all the dfs
    master_us_df = pd.concat(temp_df_list, axis=1)
    try:
        master_us_pytrends.build_payload(us_topic_id,
                                            timeframe = "all",
                                            geo="")
    except Exception as e:
            if "Google returned a response with code 400" in str(e):
                print("Caught 400")
            else:
                raise(e)
    finally:
        temp_df = master_us_pytrends.interest_over_time()
        temp_df.drop(columns="isPartial", inplace=True)
        master_us_df["Worldwide"] = temp_df
        print("Finished")
        return master_us_df

def un_countries_table():
    master_df = pd.read_csv("master_us_df.csv")
    country_df = pd.read_csv("countryTable.csv")

    country_df_filtered = country_df[country_df["UN"] == True]
    un_countries = list(country_df_filtered["Country"])
    master_df_countries = list(master_df.columns)

    to_drop = []
    for country in master_df_countries:
        print(country)
        if country not in un_countries and country != "date":
            print("yes")
            to_drop.append(country)
            
    master_df.drop(columns = to_drop, inplace=True)
    return master_df

# un_countries_table().to_csv("master_us_un_df.csv")


# df = monthly_us_scraper()
un_df = monthly_us_scraper(UN=True)
un_df.to_csv("master_us_un_df_2.csv")



# # %%
# outliers = []
# Nov_2020_results = master_us_df.loc["2020-11-01"]
# print(Nov_2020_results)

# for col_name in master_us_df.columns:
#     if Nov_2020_results[col_name] != 100:
#         outliers.append(col_name)
        
# print(outliers)


# %%
us_topic_id = ["/m/09c7w0"] # To capture US topic not just search term
country_table = pd.read_csv("countryTable.csv")
hourly_us_pytrends = TrendReq(hl='en-US', tz=360)
temp_df_list = []

# %%
# Loop through each country and two-letter abbreviation
for country_name, code in zip(country_table["Country"], country_table["Alpha_2"]):
    # Print to track country
    print(country_name, code)
    if type(code) == float:
        code = ""
    # Get data, handle exception if country is not found
    try:
        temp_df = hourly_us_pytrends.get_historical_interest(us_topic_id,
                                                             year_start=2020,
                                                             year_end=2020,
                                                             month_start=10,
                                                             month_end=11,
                                                             day_start=28,
                                                             day_end=10,
                                                             hour_start=0,
                                                             hour_end=0,
                                                             geo=code)
    except Exception as e:
        if "Google returned a response with code 400" in str(e):
            continue
        else:
            raise(e)
    # Drop irrelevant column, check if the dataset is empty
    try:
        temp_df.drop(columns="isPartial", inplace=True)
        temp_df = temp_df.loc[~temp_df.index.duplicated()]
    except KeyError:
        # In case an empty df has been given
        if len(temp_df) == 0:
            continue
    # Rename the values column as the country column
    temp_df.columns = [country_name]
    # Add the results to the list of dfs
    temp_df_list.append(temp_df)


# %%
# Concatenate all the dfs
hourly_us_df = pd.concat(temp_df_list, axis=1, ignore_index=True)
hourly_us_df.columns = [df.columns[0] for df in temp_df_list] 
hourly_us_df.to_csv("hourly_us_df.csv")
print("Finished")

# conn = sqlite3.connect("denoon_project.db")
# cursor = conn.cursor()

# # %% 
# conn_test = sqlite3.connect(":memory:")
# cursor_test = conn_test.cursor()

# # %%
# cursor 


# # %%
# conn.commit()
# conn.close()
# # %%
# us_topic_id = ["/m/09c7w0"] # To capture US topic not just search term
# country_table = pd.read_csv("countryTableComplete.csv")
# hourly_us_pytrends = TrendReq(hl='en-US', tz=360)
# try:
#     temp_df = hourly_us_pytrends.get_historical_interest(us_topic_id,
#                                                             year_start=2020,
#                                                             year_end=2020,
#                                                             month_start=10,
#                                                             month_end=11,
#                                                             day_start=28,
#                                                             day_end=10,
#                                                             hour_start=0,
#                                                             hour_end=0,
#                                                             geo="")
# except Exception as e:
#     if "Google returned a response with code 400" in str(e):
#         raise(e)
#     else:
#         raise(e)
# # Drop irrelevant column, check if the dataset is empty
# try:
#     temp_df.drop(columns="isPartial", inplace=True)
#     temp_df = temp_df.loc[~temp_df.index.duplicated()]
# except KeyError:
#     if len(temp_df) == 0:
#         pass
# # Rename the values column as the country column
# temp_df.columns = ["Worldwide"]
# # Add the results to the list of dfs
# print(temp_df)
# # %%
# hourly_us_df = pd.read_csv("hourly_us_df.csv")
# hourly_us_df.set_index("date")

# us_topic_id = ["/m/09c7w0"] # To capture US topic not just search term
# country_table = pd.read_csv("countryTableComplete.csv")
# hourly_us_pytrends = TrendReq(hl='en-US', tz=360)
# try:
#     temp_df = hourly_us_pytrends.get_historical_interest(us_topic_id,
#                                                             year_start=2020,
#                                                             year_end=2020,
#                                                             month_start=10,
#                                                             month_end=11,
#                                                             day_start=28,
#                                                             day_end=10,
#                                                             hour_start=0,
#                                                             hour_end=0,
#                                                             geo="")
# except Exception as e:
#     if "Google returned a response with code 400" in str(e):
#         raise(e)
#     else:
#         raise(e)
# # Drop irrelevant column, check if the dataset is empty
# try:
#     temp_df.drop(columns="isPartial", inplace=True)
#     temp_df = temp_df.loc[~temp_df.index.duplicated()]
# except KeyError:
#     if len(temp_df) == 0:
#         pass
# # Rename the values column as the country column
# temp_df.columns = ["Worldwide"]

# new_df = pd.concat([hourly_us_df, temp_df], axis=1)
# print(new_df)
# %%
import pandas as pd

df = pd.read_csv("master_us_un_df_2.csv")
df.drop(columns="Worldwide", inplace=True)
df.to_csv("master_us_un_df.csv")
# %%
