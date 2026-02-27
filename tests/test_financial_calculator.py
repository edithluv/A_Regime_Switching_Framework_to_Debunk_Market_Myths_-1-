import unittest

from financial_calculator import (
    compound_interest,
    future_value_annuity,
    monthly_loan_payment,
    simple_interest,
)


class FinancialCalculatorTests(unittest.TestCase):
    def test_simple_interest(self):
        self.assertAlmostEqual(simple_interest(1000, 5, 2), 1100.0, places=2)

    def test_compound_interest(self):
        self.assertAlmostEqual(
            compound_interest(1000, 12, 1, compounds_per_year=12),
            1126.825030,
            places=4,
        )

    def test_monthly_loan_payment(self):
        self.assertAlmostEqual(monthly_loan_payment(200000, 6, 30), 1199.10, places=2)

    def test_future_value_annuity(self):
        self.assertAlmostEqual(
            future_value_annuity(500, 6, 20, contributions_per_year=12),
            231020.45,
            places=2,
        )


if __name__ == "__main__":
    unittest.main()
