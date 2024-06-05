# import config
# import alpaca_trade_api as tradeapi

# api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)

# # since the get_barset is depreciated, i am using get_bars
# barsets = api.get_bars(['AAPL', 'MSFT', 'TSLA'], tradeapi.TimeFrame.Day)
# # barsets = api.get_bars(['AAPL', 'MSFT', 'TSLA'], "2024-06-04", "2024-06-04")

# # loop over the keys in the barsets dictionary
# for bar in barsets:
#     print(f"processing symbol {bar.S}")
#     print(bar.t, bar.o, bar.h, bar.l, bar.c, bar.v)


import config
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta

# Initialize the Alpaca API
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)

# Calculate the date range
end_date = datetime.today() - timedelta(days=1)
# 141 days including the end date
start_date = end_date - timedelta(days=140) 

# Convert dates to strings in the format YYYY-MM-DD
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

list_of_symbols = ['AAPL', 'MSFT', 'TSLA']

for symbol in list_of_symbols:
    # Fetch historical bar data for the specified date range
    barsets = api.get_bars(
        symbol, 
        tradeapi.TimeFrame.Day, 
        start=start_date_str, 
        end=end_date_str
    )

    # print(barsets)
    print(f"Processing symbol {symbol}")
    # Loop over the results and print the data
    for bar in barsets:
        print(bar.t, bar.o, bar.h, bar.l, bar.c, bar.v)

