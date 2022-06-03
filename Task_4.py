import pandas as pd
import numpy as np
import get_data

def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)
    percentile_.__name__ = 'percentile_%s' % n
    return percentile_


raw_data = get_data.get_data('raw_data.csv')

##Third Task
result_3 = raw_data.groupby(["shopper_id"]).agg({'products_ordered': ['count','sum'],'picking_minutes': ['sum']})
result_3 = result_3.reset_index()
result_3.columns = ['_'.join(col) for col in result_3.columns.values]
#print(result_3)
result_3['picking_speed min/product'] = result_3['picking_minutes_sum']/result_3['products_ordered_sum']
result_3 = result_3.groupby(["products_ordered_count"]).agg({'picking_speed min/product': ['mean','median',percentile(25),percentile(75)]})
#result_3 = result_3.groupby(["products_ordered_count"]).agg([np.mean, np.median, percentile(50)])
print(result_3)
