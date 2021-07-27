import ccxt
from configs import config


sell = [{'coin': 'USDT', 'quantity': 5500.0}]
buy = [{'coin': 'ETH', 'quantity': 3.8756166382523736}]
base_currency = 'BTC'


exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': config['apiKey'],
    'secret': config['secret'],
})
markets = exchange.load_markets()


def buy_market(dict_):
    if exchange.has['createMarketOrder']:
        type_ = 'market'
        try:
            side_ = 'buy'
            symbol_ = dict_['coin'] + '/' + base_currency
            amount_ = dict_['quantity']
            out = exchange.create_order(symbol_, type_, side_, amount_)
        except ccxt.BadSymbol as e:
            try:
                side_ = 'sell'
                symbol_ = base_currency + '/' + dict_['coin']
                price_base = exchange.fetchTicker(symbol_)['ask']
                amount_quote = dict_['quantity']
                amount_ = exchange.amount_to_precision(symbol_, amount_quote / price_base)
                out = exchange.create_order(symbol_, type_, side_, amount_)
            except Exception as e:
                out = 'buy_market: Error, ' + str(e)
        except Exception as e:
            out = 'buy_market: Error, ' + str(e)
        return out
    else:
        return False


def sell_market(dict_):
    if exchange.has['createMarketOrder']:
        try:
            symbol_ = base_currency + '/' + dict_['coin']
            side_ = 'buy'
            type_ = 'market'
            price_base = exchange.fetchTicker(symbol_)['bid']
            amount_quote = dict_['quantity']
            amount_ = exchange.amount_to_precision(symbol_, amount_quote / price_base)
            out = exchange.create_order(symbol_, type_, side_, amount_)
        except ccxt.BadSymbol as e:
            try:
                symbol_ = dict_['coin'] + '/' + base_currency
                side_ = 'sell'
                type_ = 'market'
                amount_ = dict_['quantity']
                out = exchange.create_order(symbol_, type_, side_, amount_)
            except Exception as e:
                out = 'buy_market: Error, ' + str(e)
        except Exception as e:
            out = 'buy_market: Error, ' + str(e)
        return out
    else:
        return False

# Limit order
# def just_buy():
#     symbol = 'ETH/BTC'
#     type = 'limit'  # or 'market', other types aren't unified yet
#     side = 'sell'
#     amount = 123.45  # your amount
#     price = 54.321  # your price
#     # overrides
#     params = {
#         'stopPrice': 123.45,  # your stop price
#         'type': 'stopLimit',
#     }
#     return exchange.create_order(symbol, type, side, amount, price, params)


print(buy_market(buy[0]))
print(sell_market(sell[0]))
