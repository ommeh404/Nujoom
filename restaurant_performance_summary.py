import pymysql
from sqlalchemy import create_engine
import pandas as pd

# Step 0: Connect to MySQL
username = 'root'
password = 'ommeh'  # Replace this
host = '127.0.0.1'
port = 3306
database = 'nujoom'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Step 1: Load data
orders = pd.read_sql("SELECT * FROM orders", engine)
restaurants = pd.read_sql("SELECT * FROM restaurants", engine)
account_managers = pd.read_sql("SELECT * FROM account_managers", engine)

# Step 2: Convert date
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Step 3: Aggregate order metrics
perf = orders.groupby('restaurant_id').agg({
    'order_id': 'count',
    'revenue': 'sum',
    'deliver_time': 'mean',
    'customer_rating': 'mean'
}).rename(columns={
    'order_id': 'total_orders',
    'revenue': 'total_revenue',
    'deliver_time': 'avg_delivery_time',
    'customer_rating': 'avg_rating'
}).reset_index()

# Step 4: Merge with restaurant and manager info
perf = perf.merge(restaurants, on='restaurant_id')
perf = perf.merge(account_managers, on='account_manager_id', suffixes=('', '_manager'))

# Step 5: Churn flag
order_cutoff = perf['total_orders'].quantile(0.25)
perf['churn_risk'] = perf['total_orders'] < order_cutoff

# Step 6: Export
perf.to_csv('restaurant_performance_summary.csv', index=False)
print("✅ Exported: restaurant_performance_summary.csv")
