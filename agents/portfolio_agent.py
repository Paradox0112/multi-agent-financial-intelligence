def analyze_portfolio(portfolio):

    total_value = sum(portfolio.values())

    diversification = len(portfolio)

    return {
        "total_value": total_value,
        "assets": diversification
    }
