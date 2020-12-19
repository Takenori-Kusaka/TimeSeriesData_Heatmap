import datetime
import pandas as pd
import random

x_list = []
y_list = []
rotate_list = []
datetime_list = []

def rotate(index):
    mod = index % 360
    return mod - 180

time = datetime.datetime.strptime('2020-12-20 13:30:30', '%Y-%m-%d %H:%M:%S')
index = 0
for x in range(1, 81):
    for y in range(1, 61):
        datetime_list.append(time)
        x_list.append(x*10+random.uniform(-5, 5))
        y_list.append(y*10+random.uniform(-5, 5))
        rotate_list.append(rotate(index))
        time = time + datetime.timedelta(milliseconds=random.uniform(100, 200))
        index = index + 1

df = pd.DataFrame({'x': x_list, 'y': y_list, 'rotate': rotate_list}, index=datetime_list)
df.to_csv('./map_log.csv', date_format='%Y/%m/%d %H:%M:%S.%f')

