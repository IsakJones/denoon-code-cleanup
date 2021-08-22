"""
Here I will create the table that gives country name, regression sigma, regression residual, statistical significance
"""

# %%
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("master_us_df.csv", header=0)
df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True)
df.set_index("date")
# %%
x_values = list(df["date"])[-24:]
y_values = list(df["Worldwide"])[-24:]

# %%
def residual(x_values, y_values, ind=17):
    """
    Runs regression between x_values and y_values, but without the observation corresponding to the int, then calculates the difference between the predicted value for the observation and the observation.
    """
    x_values_try = x_values[:ind] + x_values[(ind+1):]
    y_values_try = y_values[:ind] + y_values[(ind+1):]

    x_values_rgr = np.array(x_values).reshape((-1, 1))
    x_values_rgr_try = np.array(x_values_try).reshape((-1, 1))
    y_values_rgr_try = np.array(y_values_try)

    model = LinearRegression().fit(x_values_rgr_try, 
                                   y_values_rgr_try)

    pred_values = model.predict(x_values_rgr)
    
    return y_values[ind] - pred_values[ind]

x_values_rgr = list(range(24))

print(residual(x_values=x_values_rgr,
               y_values=y_values))
# %%
fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x_values,
         y_values)

ax.plot(x_values,
         pred_values_try)

plt.show()

# %%
# %%
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("countryTable_gdpp_itu.csv", header=0)

# %%
# Here I'll do the gdpppc regression
df.drop(columns=["2004_IT_USAGE"], inplace=True)
df.dropna(inplace=True)

print(df)
# %%
x_values = list(df["GDPPCAP"])
x_values_rgr = np.array(x_values).reshape((-1, 1))

y_values = list(df[""])

# %%
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_regression(x_values, y_values):
    x_values_rgr = np.array(x_values).reshape((-1, 1))
    y_values_rgr = np.array(y_values)

    model = LinearRegression().fit(x_values_rgr, 
                                y_values_rgr)
    pred_values = model.predict(x_values_rgr)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.scatter(x_values,
            y_values)

    ax.plot(x_values,
            pred_values)

    plt.show()
    
# %%
df = pd.read_csv("countryTableComplete.csv", header=0)
df.set_index("Country", inplace=True)


# %%
# First regression is between gdppercapita and mult
df.dropna(inplace=True)

x_values = list(df["GDPPCAP"])
y_values = list(df["Residuals"])

plot_regression(x_values, y_values)

# %%
# Second regression is between 2004 internet usage and 2004 mean value

to_drop = [col for col in df.columns if col not in ["2004_IT_USAGE", "2004_Mean"]]
df.drop(columns=to_drop, inplace=True)
df.dropna(inplace=True)

x_values = list(df["2004_IT_USAGE"])
y_values = list(df["2004_Mean"])

plot_regression(x_values, y_values)
# %%
# Third regression is between 2004 internet usage and 2004 sigma
to_drop = [col for col in df.columns if col not in ["2004_IT_USAGE", "2004_Sigma"]]
df.drop(columns=to_drop, inplace=True)
df.dropna(inplace=True)

x_values = list(df["2004_IT_USAGE"])
y_values = list(df["2004_Sigma"])

plot_regression(x_values, y_values)
# %%
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

countryTable = pd.read_csv("countryTable_backup.csv")
to_drop = [col for col in countryTable.columns if col not in ["Country", "RES", "MULT", "GDPPCAP"]]
countryTable.drop(columns=to_drop, inplace=True)
countryTable.dropna(inplace=True)

filt = countryTable["GDPPCAP"] < 40_000
countryTable = countryTable[filt]

x_values = list(countryTable["GDPPCAP"])
y_values = list(countryTable["RES"])
labels = list(countryTable["Country"])

x_values_rgr = np.array(x_values).reshape((-1, 1))
y_values_rgr = np.array(y_values)

model = LinearRegression().fit(x_values_rgr, 
                               y_values_rgr)

pred_values = model.predict(x_values_rgr)

fig = plt.figure()
ax = fig.add_subplot()

ax.scatter(x_values,
        y_values)

ax.plot(x_values,
        pred_values)

for i, txt in enumerate(labels):
    ax.annotate(txt, (x_values[i], y_values[i]))

plt.show()

# %%
