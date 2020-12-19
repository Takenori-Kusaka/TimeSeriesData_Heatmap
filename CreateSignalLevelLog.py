import datetime
import pandas as pd
import numpy as np

signal_level_list = []
datetime_list = []

time = datetime.datetime.strptime('2020-12-20 13:30:30', '%Y-%m-%d %H:%M:%S')

for i in range(64000):
    datetime_list.append(time)
    signal_level_list.append(np.random.uniform(-120, 10))
    time = time + datetime.timedelta(milliseconds=np.random.uniform(50, 100))

df = pd.DataFrame({'signal_level': signal_level_list}, index=datetime_list)
df.to_csv('./signal_level_log.csv', date_format='%Y/%m/%d %H:%M:%S.%f')

