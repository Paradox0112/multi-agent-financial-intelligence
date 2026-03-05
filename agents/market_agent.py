import random

def analyze_market(ticker):

    price = round(random.uniform(100, 300), 2)
    volatility = round(random.uniform(0.1, 0.4), 2)

    return {
        "ticker": ticker,
        "price": price,
        "volatility": volatility
    }
