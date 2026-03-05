from orchestrator import run_financial_agent

portfolio = {
    "AAPL": 5000,
    "TSLA": 3000,
    "NVDA": 2000
}

result = run_financial_agent(portfolio)

print("Financial Intelligence Report\n")

print(result)
