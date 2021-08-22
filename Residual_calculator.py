# %%
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

def residual(x_values, y_values, ind=17):
    """
    Runs regression between x_values and y_values, but without the observation corresponding to the int, then calculates the difference between the predicted value for the observation and the observation.
    """
    # In these "try" arrays, Take out the indexth element
    x_values_try = x_values[:ind] + x_values[(ind+1):]
    y_values_try = y_values[:ind] + y_values[(ind+1):]
    # Format the arrays in numpy to be able to run the regression
    x_values_rgr = np.array(x_values).reshape((-1, 1))
    x_values_rgr_try = np.array(x_values_try).reshape((-1, 1))
    y_values_rgr_try = np.array(y_values_try)
    # Fit the "try" arrays
    model = LinearRegression().fit(x_values_rgr_try, 
                                   y_values_rgr_try)
    # Get the predicted values for the complete array of the independent variable
    pred_values = model.predict(x_values_rgr)
    # Return the residual
    return y_values[ind] - pred_values[ind]

def residual_list_generator(master_df, months=24, ind=17):
    """
    This function loops through the columns of a df, which has country columns,
    and retrieves the last *months* values, and provides residuals according to
    the indexth element.
    """
    residuals = []
    #Loop through columns (countries)
    for col in master_df.columns:
        if col == "date":
            continue
        #Extract values
        x_values = list(range(months))
        y_values = list(df[col])[-24:]
        #Append country residual
        residuals.append(residual(x_values=x_values,
                                  y_values=y_values,
                                  ind=ind))
    # Return list of residuals, in the same order as columns
    return residuals

def averages_and_errors(df, ind=12):
    
    averages_list = []
    errors_list = []
    #Loop through columns (countries)
    for col in df.columns:
        # Get all numbers up to the indexth element
        data = np.array(list(df[col])[:ind])
        # get mean and standard deviation of sample
        avg = np.mean(data)
        std = np.std(data, ddof=1) / np.sqrt(np.size(data))
        # Append results
        averages_list.append(avg)
        errors_list.append(std)
    
    return averages_list, errors_list
    
        
    
df = pd.read_csv("master_us_un_df.csv", header=0)
df.drop(columns=["Unnamed: 0"], inplace=True)
df.set_index("date", inplace=True)
df.fillna(0, inplace=True)

averages, errors = averages_and_errors(df=df)

# %%
countryTable = pd.read_csv("countryTableComplete(for_now).csv")
countryTable.set_index("Country", inplace=True)
print(countryTable)

addition = pd.DataFrame({"2004_Mean": averages,
                         "2004_Sigma": errors},
                         index=df.columns)

new_df = pd.concat([countryTable, addition], axis=1)
new_df.to_csv("countryTableComplete.csv")


# %%
residuals = residual_list_generator(df)

print(df.columns)

november_interest = list(df.loc["2020-11-01"])

print(len(november_interest))


# %%
countryTable = pd.read_csv("countryTable_gdpp_itu.csv")
countryTable.drop(columns=["Unnamed: 0"], inplace=True)
countryTable.set_index("Country", inplace=True)

addition = pd.DataFrame({"2020_NOV_INT": november_interest,
                         "Residuals": residuals},
                        index=df.columns)

print(addition)
# %%
new_df = pd.concat([countryTable, addition], axis=1)
print(new_df)

new_df["Mult"] = new_df["2020_NOV_INT"] / (new_df["2020_NOV_INT"] - new_df["Residuals"])

print(new_df)
# %%
for country in countryTable.index:
    if not country in addition.index:
        print(country)
print("Finished")
# %%
new_df.to_csv("countryTableComplete(for_now).csv")
# %%
