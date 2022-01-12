#!/usr/bin/env python
# coding: utf-8

# In[18]:


def clean_items_stores_sales(): 
   
    import pandas as pd
    from datetime import timedelta, datetime
    import numpy as np
    import matplotlib.pyplot as plt
    from acquire import merge_items_stores_sales
    
    # get df
    items_stores_sales = merge_items_stores_sales()
    
    # convert the sale_date column in our df to pandas datetime object
    items_stores_sales['sale_date'] = pd.to_datetime(items_stores_sales.sale_date)
    
    # show dist using histograms
    items_stores_sales[['sale_amount', 'item_price']].hist(figsize=(12,8))
    
    # set index to sale_date
    items_stores_sales = items_stores_sales.set_index('sale_date').sort_index()
    
    # add month as a column
    items_stores_sales['month'] = items_stores_sales.index.month_name()
    
    # add day_of_week as column
    items_stores_sales['day_of_week'] = items_stores_sales.index.day_name()
    
    # multiply sale_amount and item_price to get sales_total column
    items_stores_sales['sales_total'] = items_stores_sales['sale_amount'] * items_stores_sales['item_price']

    
    return items_stores_sales
    
    


# In[27]:


# items_stores_sales = clean_items_stores_sales()


# In[26]:


# items_stores_sales.head(1)


# In[21]:


def clean_germany_power_data(): 
    
    import pandas as pd
    from datetime import timedelta, datetime
    import numpy as np
    import matplotlib.pyplot as plt
    from acquire import get_germany_power_csv
    
    # get df
    germany_power_data = get_germany_power_csv()
    
    # convert the Date column in our df to pandas datetime object
    germany_power_data['Date'] = pd.to_datetime(germany_power_data.Date)
    
    # show dist using histograms
    germany_power_data.hist(figsize=(20,15));
    
    # set index to Date
    germany_power_data = germany_power_data.set_index('Date').sort_index()
    
    # add month as column
    germany_power_data['month'] = germany_power_data.index.month_name()
    
    # add year as column
    germany_power_data['year'] = germany_power_data.index.year
    
    # fillna to fill missing values
    germany_power_data.fillna(0, inplace=True)

    return germany_power_data
    
    
    


# In[25]:


# germany_power_data = clean_germany_power_data()


# In[24]:


# germany_power_data.head()


# In[ ]:




