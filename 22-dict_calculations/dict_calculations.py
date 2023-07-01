stock = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN':623
}

min_price = min(zip(stock.values(), stock.keys()))
print(min_price)
max_price = max(zip(stock.values(), stock.keys()))
print(max_price)