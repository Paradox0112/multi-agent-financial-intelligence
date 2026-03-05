def calculate_risk(portfolio):

    total = sum(portfolio.values())

    risk_profile = {}

    for asset, value in portfolio.items():

        weight = round(value / total, 2)

        if weight > 0.5:
            risk = "High Exposure"
        elif weight > 0.2:
            risk = "Moderate Exposure"
        else:
            risk = "Low Exposure"

        risk_profile[asset] = risk

    return risk_profile
