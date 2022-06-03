import pandas as pd
import numpy as np
import get_data

raw_data = get_data.get_data()

##Task 1
raw_data['picking_finished_time'] = pd.to_datetime(raw_data['picking_finished_time'])
raw_data['picking_accepted_time'] = pd.to_datetime(raw_data['picking_accepted_time'])
raw_data['order_date'] = raw_data['picking_finished_time'].dt.date
raw_data['DOW'] = raw_data['picking_finished_time'].dt.weekday
conditions = [(raw_data['DOW'] == 5) | (raw_data['DOW'] == 6)]
raw_data['work_on_weekend'] = np.select(conditions, ['yes'], default='no')
#print(raw_data[raw_data['work_on_weekend'] == 'yes'])
#print(raw_data.head())
shopper_id = raw_data['shopper_id'].unique()
#shopper_data = raw_data.groupby('shopper_id').max()

##Second task
#print(raw_data['store_id'].unique())
result_2 = raw_data.groupby(["store_id", "order_date"]).agg({'products_ordered': ['sum']})
result_2 = result_2.reset_index()
result_2 = result_2.pivot(columns='store_id',index='order_date')
#print(result_2)

##Third Task
result_3 = raw_data.groupby(["shopper_id"]).agg({'products_ordered': ['count','sum'],'picking_minutes': ['sum']})
result_3 = result_3.reset_index()
result_3.columns = ['_'.join(col) for col in result_3.columns.values]
result_3 = result_3.groupby(["products_ordered_count"]).agg({'products_ordered_sum': ['sum'],'picking_minutes_sum': ['sum']})
result_3.columns = result_3.columns.get_level_values(0)
result_3['picking_speed min/product'] = result_3['picking_minutes_sum']/result_3['products_ordered_sum']
print(result_3)

#Fourth is more detail on third task