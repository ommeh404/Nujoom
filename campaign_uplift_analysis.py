import pymysql
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

# Step 0: Connect to MySQL
username = 'root'
password = 'ommeh'  # Replace this
host = '127.0.0.1'
port = 3306
database = 'nujoom'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Step 1: Load data
orders = pd.read_sql("SELECT * FROM orders", engine)
campaigns = pd.read_sql("SELECT * FROM campaigns", engine)
restaurants = pd.read_sql("SELECT * FROM restaurants", engine)

# Step 2: Ensure date columns are datetime
orders['order_date'] = pd.to_datetime(orders['order_date'])
campaigns['start_date'] = pd.to_datetime(campaigns['start_date'])

# Step 3: Calculate uplift
uplift_rows = []

for _, row in campaigns.iterrows():
    rid = row['restaurant_id']
    start = row['start_date']
    end = row['end_date']
    ctype = row['campaign_type']
    
    rest_orders = orders[orders['restaurant_id'] == rid]
    
    before = rest_orders[(rest_orders['order_date'] >= start - pd.Timedelta(days=7)) & 
                         (rest_orders['order_date'] < start)]
    after = rest_orders[(rest_orders['order_date'] >= start) & 
                        (rest_orders['order_date'] < start + pd.Timedelta(days=7))]
    
    orders_before = before.shape[0]
    orders_after = after.shape[0]
    
    uplift_pct = np.nan
    if orders_before > 0:
        uplift_pct = round(((orders_after - orders_before) / orders_before) * 100, 2)
    
    uplift_rows.append([
        rid, ctype, start.date(), orders_before, orders_after, uplift_pct
    ])

# Step 4: Build final DataFrame
uplift_df = pd.DataFrame(uplift_rows, columns=[
    'restaurant_id', 'campaign_type', 'start_date', 'orders_before', 'orders_after', 'uplift_percent'
])

# Step 5: Merge with restaurant info
uplift_df = uplift_df.merge(restaurants[['restaurant_id', 'name', 'city']], on='restaurant_id', how='left')

# Step 6: Export
uplift_df.to_csv('campaign_uplift_analysis.csv', index=False)
print("✅ Exported: campaign_uplift_analysis.csv")
