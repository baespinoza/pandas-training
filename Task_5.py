import pandas as pd
import numpy as np
import get_data

def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)
    percentile_.__name__ = 'percentile_%s' % n
    return percentile_

raw_data = get_data.get_data('raw_data.csv')

##Task 1
raw_data['picking_finished_time'] = pd.to_datetime(raw_data['picking_finished_time'])
raw_data['picking_accepted_time'] = pd.to_datetime(raw_data['picking_accepted_time']).round('20min')
raw_data['order_hour'] = raw_data['picking_accepted_time'].dt.time
raw_data['picking_speed'] = raw_data['picking_minutes']/raw_data['products_ordered']
#print (raw_data)
raw_data = raw_data.groupby('order_hour').agg({'picking_speed': ['mean','median',percentile(25),percentile(75)]})
print (raw_data)