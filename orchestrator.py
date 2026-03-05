from agents.market_agent import analyze_market
from agents.risk_agent import calculate_risk
from agents.portfolio_agent import analyze_portfolio


def run_financial_agent(portfolio):

    market_data = {}

    for asset in portfolio.keys():
        market_data[asset] = analyze_market(asset)

    risk = calculate_risk(portfolio)

    portfolio_summary = analyze_portfolio(portfolio)

    return {
        "market_data": market_data,
        "risk_analysis": risk,
        "portfolio_summary": portfolio_summary
    }
