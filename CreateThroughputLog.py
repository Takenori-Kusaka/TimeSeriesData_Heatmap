import datetime
import pandas as pd
import numpy as np

throughput_list = []
datetime_list = []

time = datetime.datetime.strptime('2020-12-20 13:30:30', '%Y-%m-%d %H:%M:%S')

for i in range(1280):
    datetime_list.append(time)
    throughput_list.append(np.random.uniform(1, 1000))
    time = time + datetime.timedelta(milliseconds=1000)

df = pd.DataFrame({'throughput': throughput_list}, index=datetime_list)
df.to_csv('./throughput_log.csv', date_format='%Y/%m/%d %H:%M:%S.%f')

