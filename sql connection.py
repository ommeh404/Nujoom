import pymysql
from sqlalchemy import create_engine, text

# Updated credentials
username = 'root'
password = 'ommeh'  # Replace this
host = '127.0.0.1'
port = 3306
database = 'nujoom'  # <- use your actual DB name

# Connect to MySQL
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Test the connection
try:
    with engine.connect() as conn:
        result = conn.execute(text("SHOW TABLES;"))
        print("✅ Connected to MySQL!")
        print("Tables:", [row[0] for row in result])
except Exception as e:
    print("❌ Connection failed.")
    print("Error:", e)
