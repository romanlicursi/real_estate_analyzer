class FinancialCalculator:
    def __init__(self, property_price, down_payment_percent, interest_rate, loan_term_years):
        self.property_price = property_price
        self.down_payment = property_price * (down_payment_percent / 100)
        self.loan_amount = property_price - self.down_payment
        self.interest_rate = interest_rate / 100
        self.loan_term_months = loan_term_years * 12

    def calculate_monthly_mortgage(self):
        """Calculate monthly mortgage payment using the amortization formula."""
        r = self.interest_rate / 12  # Monthly interest rate
        n = self.loan_term_months

        if r == 0:  # Handle zero interest rate case
            return self.loan_amount / n
        monthly_payment = (self.loan_amount * r * (1 + r)**n) / ((1 + r)**n - 1)
        return round(monthly_payment, 2)

    def calculate_cash_flow(self, monthly_rent, expenses):
        """Calculate monthly cash flow."""
        monthly_mortgage = self.calculate_monthly_mortgage()
        total_expenses = monthly_mortgage + expenses
        cash_flow = monthly_rent - total_expenses
        return round(cash_flow, 2)

    def calculate_roi(self, annual_cash_flow):
        """Calculate Return on Investment (ROI)."""
        roi = (annual_cash_flow / self.down_payment) * 100
        return round(roi, 2)

    def analyze_property(self, monthly_rent, monthly_expenses):
        """Comprehensive property analysis."""
        monthly_mortgage = self.calculate_monthly_mortgage()
        monthly_cash_flow = self.calculate_cash_flow(monthly_rent, monthly_expenses)
        annual_cash_flow = monthly_cash_flow * 12
        roi = self.calculate_roi(annual_cash_flow)

        return {
            "monthly_mortgage": monthly_mortgage,
            "monthly_cash_flow": monthly_cash_flow,
            "annual_cash_flow": annual_cash_flow,
            "roi": roi
        }

