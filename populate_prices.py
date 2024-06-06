import sqlite3
import config
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta

# connect to the database
connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row

# create a cursor
cursor = connection.cursor()

# get all the companies that we have in the database
cursor.execute("""
    SELECT id, symbol, name FROM stock
""")

# fetch all the datas and store them in rows
rows = cursor.fetchall()

# # create a symbols list
# symbols = [row['symbol'] for row in rows]

# create symbols list
symbols = []
# create stock dictionary
stock_dict = {}
# iterate through the rows
for row in rows:
    # get the symbol of the row
    symbol = row['symbol']
    # append it to the symbols list
    symbols.append(symbol)
    # populate stock dictionary
    stock_dict[symbol] = row['id']

# Initialize the Alpaca API
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)

# Calculate the date range
end_date = datetime.today() - timedelta(days=1)
# 120 days including the end date
start_date = end_date - timedelta(days=120) 

# Convert dates to strings in the format YYYY-MM-DD
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# declare the chunk size to be 200
chunk_size = 200

# loop through 
for i in range(0, len(symbols), chunk_size):

    symbol_chunk = symbols[i:i+chunk_size]

    barsets = api.get_bars(symbol_chunk, tradeapi.TimeFrame.Day, start=start_date_str, end=end_date_str)

    data_by_ticker = {}

    # Organize data by ticker
    for bar in barsets:
        ticker = bar.S
        if ticker not in data_by_ticker:
            data_by_ticker[ticker] = []
        data_by_ticker[ticker].append(bar)

        # Print data for each ticker
        for ticker, bars in data_by_ticker.items():
            try:
                print(f"Data for {ticker}:")
                for bar in bars:
                    print(f"  Date: {bar.t}")
                    print(f"    Open: {bar.o}")
                    print(f"    High: {bar.h}")
                    print(f"    Low: {bar.l}")
                    print(f"    Close: {bar.c}")
                    print(f"    Volume: {bar.v}")
                    print(f"    VWAP: {bar.vw}")
                    print(f"    Number of Trades: {bar.n}")
                print("\n")
            except Exception as e:
                # print the symbol of the stock that gave me the error
                print(ticker)
                # print the error itself
                print(e)






    # for symbol in symbol_chunk:
    #     # Fetch historical bar data for days
    #     barsets = api.get_bars(
    #         symbol, 
    #         tradeapi.TimeFrame.Day, 
    #         # start=start_date_str, 
    #         # end=end_date_str
    #     )

    #     print(f"Processing symbol {symbol}")
    #     # Loop over the results and print the data
    #     for bar in barsets:
    #         stock_id = stock_dict[symbol]
    #         print(stock_id)
    #         # print(bar.t, bar.o, bar.h, bar.l, bar.c, bar.v)