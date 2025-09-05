import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["ENI.MI", "ISP.MI"]
start_date = "2018-01-01"
end_date = "2024-01-01"

# Scarico dati con auto_adjust=True
data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)["Close"]

# Rendimenti giornalieri
returns = data.pct_change().dropna()

# Rendimento cumulato
cumulative_returns = (1 + returns).cumprod() - 1

# Rendimento medio e volatilità annualizzata
mean_annual_return = returns.mean() * 252
volatility_annual = returns.std() * (252 ** 0.5)

print("Rendimento medio annualizzato (%):")
print(mean_annual_return * 100)

print("\nVolatilità annualizzata (%):")
print(volatility_annual * 100)

# Grafico rendimento cumulato
plt.figure(figsize=(12,6))
for ticker in tickers:
    plt.plot(cumulative_returns[ticker], label=f"{ticker} - Rendimento cumulato")
plt.title("Confronto rendimento cumulato: ENI vs Intesa Sanpaolo (2018–2024)")
plt.xlabel("Data")
plt.ylabel("Rendimento cumulato")
plt.legend()
plt.grid(True)
plt.show()
