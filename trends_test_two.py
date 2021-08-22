# %%

from pytrends.request import TrendReq
from matplotlib import pyplot as plt

import pandas as pd

pytrends = []
results = []
items = ["Bananas",
         "Apples", 
         "Oranges", 
         "Lemons",
         "Pears"]

for i in range(5):
    pytrends.append(TrendReq())
    pytrends[i].build_payload([items[i]],
                              cat='0',
                              timeframe="today 5-y",
                              geo="",
                              gprop="")
    results.append(pytrends[i].interest_over_time())

for table in results:
    print(table)
# %%
results[0]