# %%
import re
import pandas as pd
from matplotlib import pyplot as plt
from pytrends.request import TrendReq

# %%
us_topic_id = ["/m/09c7w0"] # To capture US topic not just search term
hourly_us_pytrends = TrendReq(hl='en-US', tz=360)

df = hourly_us_pytrends.get_historical_interest(us_topic_id,
                                                year_start=2020,
                                                year_end=2020,
                                                month_start=11,
                                                month_end=11,
                                                day_start=2,
                                                day_end=15,
                                                hour_start=0,
                                                hour_end=0,
                                                geo="")

df.drop(columns="isPartial", inplace=True)
df.columns = ["2020"]

print(df)

df.to_csv("hourly_worldwide_us.csv")

# %%
df = pd.read_csv("hourly_worldwide_us.csv")

plt.plot(pd.to_datetime(df["date"], infer_datetime_format=True),
         list(df["2020"]))
# %%
us_topic_id = ["/m/09c7w0"] # To capture US topic not just search term
hourly_us_pytrends = TrendReq(hl='en-US', tz=360)

df_new = hourly_us_pytrends.get_historical_interest(us_topic_id,
                                                    year_start=2016,
                                                    year_end=2016,
                                                    month_start=11,
                                                    month_end=11,
                                                    day_start=3,
                                                    day_end=10,
                                                    hour_start=0,
                                                    hour_end=0,
                                                    geo="")

df_new.drop(columns="isPartial", inplace=True)
df_new.columns = ["2016"]

plt.plot(df_new.index,
         list(df_new["2016"]))

# %%
