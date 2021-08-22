# %%
from pytrends.request import TrendReq
from pytrends import dailydata
import pandas as pd
import time 

pytrends = TrendReq(hl="en-US", tz=360)
items = ["Bananas",
         "Apples", 
         "Oranges", 
         "Lemons",
         "Pears"]
us_topic_id = ["/m/09c7w0"]

# %%

# df = dailydata.get_daily_data(word=us_topic_id[0],
#                               start_year=2004,
#                               start_mon=1,
#                               stop_year=2021,
#                               stop_mon=4,
#                               geo='US')
# print(df)



# %%

pytrends.build_payload(kw_list=us_topic_id,
                       timeframe='all',
                       geo="US",
                       gprop="")
df_banana = pytrends.interest_over_time()
print(df_banana.columns)

df_banana.to_csv("banana.csv")

# %%
new_df = pd.read_csv("banana.csv", header = 0)
print(new_df)
print(new_df.columns)

# %%

