#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import holidays

def calendar_holidays():
    us_holidays = []
    yrs = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
    for yr in yrs:
        for date, name in sorted(holidays.US(years=yr).items()):
            us_holidays.append([date,name])

    us_holidays = pd.DataFrame.from_records(us_holidays)
    us_holidays.columns = ['ds','holiday']
    us_holidays['ds'] = pd.to_datetime(us_holidays['ds'])
    us_holidays = us_holidays.drop_duplicates(subset=['ds'])

    us_holidays.sort_values(by='ds',inplace=True)
    us_holidays.reset_index(inplace=True,drop=True)
    us_holidays.set_index('ds',inplace=True)
    us_holidays.loc['2014-02-01'] = 'Superbowl (Observed)'
    us_holidays.loc['2014-02-02'] = 'Superbowl'
    us_holidays.loc['2015-01-31'] = 'Superbowl (Observed)'
    us_holidays.loc['2015-02-01'] = 'Superbowl'
    us_holidays.loc['2016-02-06'] = 'Superbowl (Observed)'
    us_holidays.loc['2016-02-07'] = 'Superbowl'
    us_holidays.loc['2017-02-04'] = 'Superbowl (Observed)'
    us_holidays.loc['2017-02-05'] = 'Superbowl'
    us_holidays.loc['2018-02-03'] = 'Superbowl (Observed)'
    us_holidays.loc['2018-02-04'] = 'Superbowl'
    us_holidays.loc['2019-02-02'] = 'Superbowl (Observed)'
    us_holidays.loc['2019-02-03'] = 'Superbowl'
    us_holidays.loc['2020-02-01'] = 'Superbowl (Observed)'
    us_holidays.loc['2020-02-02'] = 'Superbowl'
    us_holidays.loc['2021-02-06'] = 'Superbowl (Observed)'
    us_holidays.loc['2021-02-07'] = 'Superbowl'
    us_holidays.loc['2022-02-05'] = 'Superbowl (Observed)'
    us_holidays.loc['2022-02-06'] = 'Superbowl'
    us_holidays.loc['2023-02-04'] = 'Superbowl (Observed)'
    us_holidays.loc['2023-02-05'] = 'Superbowl'
    us_holidays.loc['2024-02-03'] = 'Superbowl (Observed)'
    us_holidays.loc['2024-02-04'] = 'Superbowl'
    us_holidays.loc['2025-02-01'] = 'Superbowl (Observed)'
    us_holidays.loc['2025-02-02'] = 'Superbowl'
    
    us_holidays.loc['2014-02-14'] = 'Valentines'
    us_holidays.loc['2015-02-14'] = 'Valentines'
    us_holidays.loc['2016-02-14'] = 'Valentines'
    us_holidays.loc['2017-02-14'] = 'Valentines'
    us_holidays.loc['2018-02-14'] = 'Valentines'
    us_holidays.loc['2019-02-14'] = 'Valentines'
    us_holidays.loc['2020-02-14'] = 'Valentines'
    us_holidays.loc['2021-02-14'] = 'Valentines'
    us_holidays.loc['2022-02-14'] = 'Valentines'
    us_holidays.loc['2023-02-14'] = 'Valentines'
    us_holidays.loc['2024-02-14'] = 'Valentines'
    us_holidays.loc['2025-02-14'] = 'Valentines'
    
    us_holidays.loc['2014-05-10'] = 'Mothers Day (Observed)'
    us_holidays.loc['2014-05-11'] = 'Mothers Day'
    us_holidays.loc['2015-05-09'] = 'Mothers Day (Observed)'
    us_holidays.loc['2015-05-10'] = 'Mothers Day'
    us_holidays.loc['2016-05-07'] = 'Mothers Day (Observed)'
    us_holidays.loc['2016-05-08'] = 'Mothers Day'
    us_holidays.loc['2017-05-13'] = 'Mothers Day (Observed)'
    us_holidays.loc['2017-05-14'] = 'Mothers Day'
    us_holidays.loc['2018-05-12'] = 'Mothers Day (Observed)'
    us_holidays.loc['2018-05-13'] = 'Mothers Day'
    us_holidays.loc['2019-05-11'] = 'Mothers Day (Observed)'
    us_holidays.loc['2019-05-12'] = 'Mothers Day'
    us_holidays.loc['2020-05-09'] = 'Mothers Day (Observed)'
    us_holidays.loc['2020-05-10'] = 'Mothers Day'
    us_holidays.loc['2021-05-08'] = 'Mothers Day (Observed)'
    us_holidays.loc['2021-05-09'] = 'Mothers Day'
    us_holidays.loc['2022-05-07'] = 'Mothers Day (Observed)'
    us_holidays.loc['2022-05-08'] = 'Mothers Day'
    us_holidays.loc['2023-05-13'] = 'Mothers Day (Observed)'
    us_holidays.loc['2023-05-14'] = 'Mothers Day'
    us_holidays.loc['2024-05-11'] = 'Mothers Day (Observed)'
    us_holidays.loc['2024-05-12'] = 'Mothers Day'
    us_holidays.loc['2025-05-10'] = 'Mothers Day (Observed)'
    us_holidays.loc['2025-05-11'] = 'Mothers Day'
    
    us_holidays.loc['2014-04-19'] = 'Easter (Observed)'
    us_holidays.loc['2014-04-20'] = 'Easter'
    us_holidays.loc['2015-04-04'] = 'Easter (Observed)'
    us_holidays.loc['2015-04-05'] = 'Easter'
    us_holidays.loc['2016-03-26'] = 'Easter (Observed)'
    us_holidays.loc['2016-03-27'] = 'Easter'
    us_holidays.loc['2017-04-15'] = 'Easter (Observed)'
    us_holidays.loc['2017-04-16'] = 'Easter'
    us_holidays.loc['2018-03-31'] = 'Easter (Observed)'
    us_holidays.loc['2018-04-01'] = 'Easter'
    us_holidays.loc['2019-04-20'] = 'Easter (Observed)'
    us_holidays.loc['2019-04-21'] = 'Easter'
    us_holidays.loc['2020-04-11'] = 'Easter (Observed)'
    us_holidays.loc['2020-04-12'] = 'Easter'
    us_holidays.loc['2021-04-03'] = 'Easter (Observed)'
    us_holidays.loc['2021-04-04'] = 'Easter'
    us_holidays.loc['2022-04-16'] = 'Easter (Observed)'
    us_holidays.loc['2022-04-17'] = 'Easter'
    us_holidays.loc['2023-04-08'] = 'Easter (Observed)'
    us_holidays.loc['2023-04-09'] = 'Easter'
    us_holidays.loc['2024-03-30'] = 'Easter (Observed)'
    us_holidays.loc['2024-03-31'] = 'Easter'
    us_holidays.loc['2025-04-19'] = 'Easter (Observed)'
    us_holidays.loc['2025-04-20'] = 'Easter'
    
    
    us_holidays.reset_index(inplace=True)
    us_holidays.sort_values(by='ds',inplace=True)
    us_holidays.reset_index(drop=True,inplace=True)
    
    return us_holidays


# In[ ]:




