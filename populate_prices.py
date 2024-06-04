import config
import alpaca_trade_api as tradeapi

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL)

# since the get_barset is depreciated, i am using get_bars
barset = api.get_bars(['AAPL', 'MSFT'], tradeapi.TimeFrame.Day)
print(barset)