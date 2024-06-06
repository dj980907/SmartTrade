# import sqlite3, config for sql database
import sqlite3, config
# import alpaca api for trading
import alpaca_trade_api as tradeapi

# connect to the database
connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row

# create a cursor
cursor = connection.cursor()

# get all the companies that we have in the database
cursor.execute("""
    SELECT symbol, name FROM stock
""")

# fetch all the datas and store them in rows
rows = cursor.fetchall()

# create a symbols list
symbols = [row['symbol'] for row in rows]

# connect to Alpaca API
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)

# save the assets
assets = api.list_assets()

# go through each asset and insert it into our database 
for asset in assets:
    try:
        # if the stock is active and tradable and was not in the list of our already ecisting database
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            # print the stock
            print(f"Added a new stock {asset.symbol, asset.name}")
            # add it to the database
            cursor.execute("INSERT INTO stock (symbol, name) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        # print the symbol of the stock that gave me the error
        print(asset.symbol)
        # print the error itself
        print(e)

# commit
connection.commit()