import pymysql
from sqlalchemy import create_engine
import pandas as pd

# MySQL connection details
username = 'root'
password = 'ommeh'  # replace with your actual password
host = '127.0.0.1'
port = 3306
database = 'nujoom'

# Create engine (the connector to your database)
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Now load data using pandas
restaurants = pd.read_sql("SELECT * FROM restaurants", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)
campaigns = pd.read_sql("SELECT * FROM campaigns", engine)
crm = pd.read_sql("SELECT * FROM crm_interactions", engine)
account_managers = pd.read_sql("SELECT * FROM account_managers", engine)

print("✅ Data loaded successfully!")


