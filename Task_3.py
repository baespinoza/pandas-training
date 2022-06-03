import pandas as pd
import numpy as np
import get_data

raw_data = get_data.get_data('raw_data.csv')

##Third Task
result_3 = raw_data.groupby(["shopper_id"]).agg({'products_ordered': ['count','sum'],'picking_minutes': ['sum']})
result_3 = result_3.reset_index()
result_3.columns = ['_'.join(col) for col in result_3.columns.values]
result_3 = result_3.groupby(["products_ordered_count"]).agg({'products_ordered_sum': ['sum'],'picking_minutes_sum': ['sum']})
result_3.columns = result_3.columns.get_level_values(0)
result_3['picking_speed min/product'] = result_3['picking_minutes_sum']/result_3['products_ordered_sum']
print(result_3)