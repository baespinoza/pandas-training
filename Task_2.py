import pandas as pd
import numpy as np
import get_data

raw_data = get_data.get_data('raw_data.csv')

##Second task
raw_data['picking_finished_time'] = pd.to_datetime(raw_data['picking_finished_time'])
raw_data['picking_accepted_time'] = pd.to_datetime(raw_data['picking_accepted_time'])
raw_data['order_date'] = raw_data['picking_finished_time'].dt.date
result_2 = raw_data.groupby(["store_id", "order_date"]).agg({'products_ordered': ['sum']})
result_2 = result_2.reset_index()
result_2 = result_2.pivot(columns='store_id',index='order_date')
print(result_2)