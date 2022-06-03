import re
import pandas as pd
import numpy as np
import get_data

raw_data = get_data.get_data('raw_data.csv')

##Task 1
raw_data['picking_finished_time'] = pd.to_datetime(raw_data['picking_finished_time'])
raw_data['picking_accepted_time'] = pd.to_datetime(raw_data['picking_accepted_time'])
raw_data['order_date'] = raw_data['picking_finished_time'].dt.date
raw_data['DOW'] = raw_data['picking_finished_time'].dt.weekday

conditions = [(raw_data['DOW'] == 5) | (raw_data['DOW'] == 6)]
raw_data['work_on_weekend'] = np.select(conditions, ['yes'], default='no')

#print(raw_data[raw_data["shopper_id"] == 6912830])

result = raw_data.groupby(["shopper_id"]).apply(lambda x: x.work_on_weekend.max())
print(result)