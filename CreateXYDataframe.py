import datetime
import pandas as pd
import random

x_list = []
y_list = []
datetime_list = []

time = datetime.datetime.strptime('2020-12-20 13:30:30', '%Y-%m-%d %H:%M:%S')
index = 0.0
for x in range(800):
    for y in range(600):
        datetime_list.append(time)
        x_list.append(x)
        y_list.append(y)
        time = time + datetime.timedelta(milliseconds=random.uniform(100, 200))

df = pd.DataFrame({'x': x_list, 'y': y_list}, index=datetime_list)
df.to_csv('./map_log.csv', date_format='%Y/%m/%d %H:%M:%S.%f')

