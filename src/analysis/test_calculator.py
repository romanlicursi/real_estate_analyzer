from financial_calculator import FinancialCalculator

# Example property details
price = 300000
down_payment = 20  # Percent
interest_rate = 5  # Annual interest rate in percent
loan_term = 30  # Loan term in years
rent = 2500  # Monthly rent
expenses = 500  # Monthly expenses

calculator = FinancialCalculator(price, down_payment, interest_rate, loan_term)
analysis = calculator.analyze_property(rent, expenses)

print("Property Analysis:")
for key, value in analysis.items():
    print(f"{key}: {value}")

