
from sqlalchemy import URL, create_engine, text
import numpy as np
import pandas as pd
import requests
connection_string = URL.create(
    'postgresql',
    username='admin',
    password='LIQztHkfYr37',
    host='ep-patient-dream-a2pmp0ut.eu-central-1.pg.koyeb.app',
    database='koyebdb',
    query={
        'sslmode': 'require',
        'options': 'endpoint=ep-patient-dream-a2pmp0ut'  # Add your endpoint ID here
    }
)
engine = create_engine(connection_string)


endpoint = 'https://api.binance.com/api/v3/exchangeInfo'
response = requests.get(endpoint)
exchange_info = response.json()
exchange_info = pd.DataFrame(exchange_info['symbols'])
exchange_info = exchange_info[exchange_info['status'] == 'TRADING']
exchange_info = exchange_info[["symbol", "baseAsset"]]
print(exchange_info)

try:
    exchange_info.to_sql("randomDatabaseTable",engine, if_exists = "replace")
except Exception as e:
    print(e)


try:
    with engine.connect() as connection:
        q = """SELECT * FROM "public"."randomDatabaseTable";"""
        print(pd.read_sql(text(q),connection))
except Exception as e:
    print(f"An error occurred: {e}")
