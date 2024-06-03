# import sqlite3 for sql database
import sqlite3
# import alpaca api for trading
import alpaca_trade_api as tradeapi
# import os modul;e for environment variables
import os
# import necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# load variables from .env file
load_dotenv()

# connect to the database
connection = sqlite3.connect('app.db')

# create a cursor
cursor = connection.cursor()

# # populate the database
# cursor.execute("INSERT INTO stock (symbol, company) VALUES ('ADOBE', 'Adobe INC.')")
# cursor.execute("INSERT INTO stock (symbol, company) VALUES ('VZ', 'Verizon')")
# cursor.execute("INSERT INTO stock (symbol, company) VALUES ('Z', 'Zillow')")

# # delete the database
# cursor.execute("DELETE FROM stock")

api = tradeapi.REST(os.getenv("API_KEY"), os.getenv("SECRET_KEY"), os.getenv("BASE_URL"))
assets = api.list_assets()

# insert the stock data into the database
for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)
# commit
connection.commit()