#!/usr/bin/env python
# coding: utf-8

# # Acquire Functions for Time Series

# In[8]:


def request_items():
    
    '''
    This function requests api and creates a dictionary from the .json.
    It then turns the dictionary into a dataframe. It asigns the max page number
    to a variable that is used in a loop to exract all pages. 
    '''

    import pandas as pd
    import requests  

    # base URL for api
    base_url = 'https://python.zgulde.net'

    # make request
    response = requests.get('https://python.zgulde.net/api/v1/items')
    
    # make dictionary from .json
    data = response.json()
    
    # turn data into pd df
    sales = pd.DataFrame(data['payload']['items'])

    # create var for max_page 
    max_pages = data['payload']['max_page']

    # loop thru to extract all pages
    for i in range(1,max_pages):

        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        items = pd.concat([sales, pd.DataFrame(data['payload']['items'])])
    
    return items  
 


# In[31]:


# items = request_items()


# In[32]:


# items.head()


# In[11]:


def get_items_data():
    
    import os
    import pandas as pd
    import requests  
    
    '''
    This function checks for a local sales.csv file and reads it into a pandas dataframe, if it exists. 
    If not, it uses the get_sales to request the data and write it locally to a csv file.
    '''
    # If csv file exists locally, read in data from csv file.
    if os.path.isfile('items.csv'):
        df = pd.read_csv('items.csv', index_col=0)
        
    else:
        
        # request and read data from api
        df = request_items()
        
        # Cache data
        df.to_csv('items.csv')
        
    return df


# In[33]:


# items = get_items_data()


# In[34]:


# items.head()


# In[14]:


def request_stores():
    
    '''
    This function requests api and creates a dictionary from the .json.
    It then turns the dictionary into a dataframe. It asigns the max page number
    to a variable that is used in a loop to exract all pages. 
    '''

    import pandas as pd
    import requests  

    # base URL for api
    base_url = 'https://python.zgulde.net'

    # make request
    response = requests.get('https://python.zgulde.net/api/v1/stores')
    
    # make dictionary from .json
    data = response.json()
    
    # turn data into pd df
    stores = pd.DataFrame(data['payload']['stores'])

    # create var for max_page 
    max_pages = data['payload']['max_page']

    # loop thru to extract all pages
    for i in range(1,max_pages):

        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        items = pd.concat([sales, pd.DataFrame(data['payload']['stores'])])
    
    return stores 


# In[36]:


# stores = request_stores()


# In[37]:


# stores.head()


# In[17]:


def get_stores_data():
    
    import os
    import pandas as pd
    import requests  
    
    '''
    This function checks for a local sales.csv file and reads it into a pandas dataframe, if it exists. 
    If not, it uses the get_sales to request the data and write it locally to a csv file.
    '''
    # If csv file exists locally, read in data from csv file.
    if os.path.isfile('stores.csv'):
        df = pd.read_csv('stores.csv', index_col=0)
        
    else:
        
        # request and read data from api
        df = request_stores()
        
        # Cache data
        df.to_csv('stores.csv')
        
    return df


# In[38]:


# stores = get_stores_data()


# In[39]:


# stores.head()


# In[1]:


def request_sales():

    '''
    This function requests api and creates a dictionary from the .json.
    It then turns the dictionary into a dataframe. It asigns the max page number
    to a variable that is used in a loop to exract all pages. 
    '''
    
    import pandas as pd
    import requests  

    # base URL for api
    base_url = 'https://python.zgulde.net'

    # make request
    response = requests.get('https://python.zgulde.net/api/v1/sales')
    
    # make dictionary from .json
    data = response.json()
    
    # turn data into pd df
    sales = pd.DataFrame(data['payload']['sales'])

    # create var for max_page 
    max_pages = data['payload']['max_page']

    # loop thru to extract all pages
    for i in range(1,max_pages):

        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        sales = pd.concat([sales, pd.DataFrame(data['payload']['sales'])])
    
    return sales    
 


# In[40]:


# request_sales()


# In[5]:


def get_sales_data():
    
    import os
    import pandas as pd
    import requests  
    
    '''
    This function checks for a local sales.csv file and reads it into a pandas dataframe, if it exists. 
    If not, it uses the get_sales to request the data and write it locally to a csv file.
    '''
    # If csv file exists locally, read in data from csv file.
    if os.path.isfile('sales.csv'):
        df = pd.read_csv('sales.csv', index_col=0)
        
    else:
        
        # request and read data from api
        df = request_sales()
        
        # Cache data
        df.to_csv('sales.csv')
        
    return df


# In[41]:


# sales = get_sales_data()


# In[42]:


# sales.head()


# In[20]:


def merge_items_stores_sales():
    '''
    This function creates three DFs using get_items_data(), get_stores_data(),
    and get_sales_data(). It then merges these DFs into one. 
    '''

    import pandas as pd

    items = get_items_data()
    stores = get_stores_data()
    sales = get_sales_data()

    sales_stores = pd.merge(sales, stores, how='left', left_on='store' , right_on='store_id')

    items_stores_sales = pd.merge(sales_stores, items, how='left', left_on='item', right_on='item_id')

    return items_stores_sales


# In[43]:


# items_stores_sales = merge_items_stores_sales()


# In[44]:


# items_stores_sales.head()


# In[28]:


def get_germany_power_csv():
    
    '''
    This function reads csv from url and returns a DF. 
    '''
    
    import pandas as pd
    
    csv_url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

    csv_export_url = csv_url.replace('/edit#gid=', '/export?format=csv&gid=')

    germany_power_data = pd.read_csv(csv_export_url)
    return germany_power_data


# In[45]:


# germany_power_data = get_germany_power_csv()


# In[46]:


# germany_power_data.head()


# In[ ]:




