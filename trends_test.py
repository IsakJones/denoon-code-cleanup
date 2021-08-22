# %%

from pytrends.request import TrendReq
from matplotlib import pyplot as plt

import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

all_keywords = ["fidget spinner"]

pytrends.build_payload(all_keywords, # Keyword List can be up to 5 terms long
                       cat='0', # Category like art, business etc.
                       timeframe="today 5-y", # dates YYYY-MM-DD with space, other option is 'all'
                       geo="", # two-letter
                       gprop="") # what property to fill in

# %%
df = pytrends.interest_over_time()

print(df)

# %%
pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(all_keywords, # Keyword List can be up to 5 terms long
                       cat='0', # Category like art, business etc.
                       timeframe="today 2-y", # dates YYYY-MM-DD with space, other option is 'all'
                       geo="US", # two-letter
                       gprop="") # what property to fill in
df_us = pytrends.interest_over_time()
# %%
plt.plot(list(range(len(df))),
     df["fidget spinner"])
# %%

pytrends_two = TrendReq(hl='en-US', tz=360)

pytrends.build_payload(all_keywords, # Keyword List can be up to 5 terms long
                       cat='0', # Category like art, business etc.
                       timeframe="today 5-y", # dates YYYY-MM-DD with space, other option is 'all'
                       geo="", # two-letter
                       gprop="") # what property to fill in
pytrends_two.build_payload(all_keywords,
                           cat='0',
                           timeframe="2021-02-14 2021-01-14",
                           geo='US',
                           gprop="")
df_two = pytrends.get_historical_interest(["Nancy Pelosi"],
                                          year_start=2021,
                                          year_end=2021,
                                          month_start=1,
                                          month_end=2,
                                          day_start=25,
                                          day_end=3)

# %%

pytrends_three = TrendReq(hl='en-US', tz=360)
pytrends_three.build_payload(all_keywords, # Keyword List can be up to 5 terms long
                       cat='0', # Category like art, business etc.
                       timeframe="today 5-y", # dates YYYY-MM-DD with space, other option is 'all'
                       geo="", # two-letter
                       gprop="") # what property to fill in


df_three = pytrends_three.interest_by_region(resolution = 'COUNTRY') # This is more for general popularity, not over time
# %%
