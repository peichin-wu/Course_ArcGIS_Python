import pandas as pd
import numpy as np
"""
Annual average for each year in the dataset.
Minimum, maximum and average for the entire dataset.
Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
Calculate the anomaly for each value in the dataset relative to the mean for the entire timeseries.
"""
print('\n')


print('Minimum, maximum and average for the entire dataset.')
df = pd.read_csv('co2-ppm-daily.csv', parse_dates=['date'])
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year
print('Minimum',df["value"].min(),' Maximum',df["value"].max(),'Average',df["value"].sum()/df.shape[0])
print('\n')

print('Annual average for each year in the dataset.')
dfgb_y=df[["value","year","month"]].groupby(["year"]).agg(['mean', 'count'])
print(dfgb_y.value["mean"])
print('\n')


print('Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).')
dfgb_m=df[["value","year","month"]].groupby(["month"]).agg(['mean', 'count'])
spring=0
for i in [2,3,4]:
    spring += dfgb_m.value["mean"].loc[i]
summer=0
for i in [5,6,7]:
    summer += dfgb_m.value["mean"].loc[i]
fall=0
for i in [8,9,10]:
    fall += dfgb_m.value["mean"].loc[i]
winter=0
for i in [11,1,2]:
    winter += dfgb_m.value["mean"].loc[i]
print('Spring:',spring/3)
print('Summer',summer/3)
print('Fall:',fall/3)
print('Winter:',winter/3)
print('\n')

print('Calculate the anomaly for each value in the dataset relative to the mean for the entire timeseries.')
larger_than_2std=np.array(df[df.value > (df.mean().value+df.std(axis = 0, skipna = True).value*2)].value)
less_than_2std=np.array(df[df.value < (df.mean().value-df.std(axis = 0, skipna = True).value*2)].value)
anomoly=[]
for i in range(len(larger_than_2std)+len(less_than_2std)):
    anomoly.append(np.concatenate((larger_than_2std, less_than_2std), axis=None)[i])
print(anomoly)

# Numpy is designed for this kind of processing. So well done for using it, clearly you know what you are doing.
# However, your anomaly code is a little different to the simple definition of anomaly (value - overall_mean),
# you should have some negative values in the 1950's 1960's turning positive later on in the series.