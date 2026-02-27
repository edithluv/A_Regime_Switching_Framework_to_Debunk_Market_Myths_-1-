"""Command-line financial calculator.

Supports common personal finance calculations:
- simple interest
- compound interest
- loan payment (amortized monthly)
- future value of recurring contributions
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class CalculationResult:
    name: str
    value: float


def simple_interest(principal: float, annual_rate: float, years: float) -> float:
    """Return final balance using simple interest.

    annual_rate is provided as percent (e.g., 5 for 5%).
    """
    return principal * (1 + (annual_rate / 100) * years)


def compound_interest(
    principal: float,
    annual_rate: float,
    years: float,
    compounds_per_year: int = 1,
) -> float:
    """Return final balance using compound interest."""
    rate = annual_rate / 100
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)


def monthly_loan_payment(principal: float, annual_rate: float, years: float) -> float:
    """Return monthly loan payment for a fully amortized loan."""
    months = int(years * 12)
    monthly_rate = annual_rate / 100 / 12

    if monthly_rate == 0:
        return principal / months

    factor = (1 + monthly_rate) ** months
    return principal * (monthly_rate * factor) / (factor - 1)


def future_value_annuity(
    periodic_contribution: float,
    annual_rate: float,
    years: float,
    contributions_per_year: int = 12,
) -> float:
    """Return future value of recurring contributions (ordinary annuity)."""
    periods = int(years * contributions_per_year)
    periodic_rate = annual_rate / 100 / contributions_per_year

    if periodic_rate == 0:
        return periodic_contribution * periods

    return periodic_contribution * (((1 + periodic_rate) ** periods - 1) / periodic_rate)


def _format_result(result: CalculationResult) -> str:
    return f"{result.name}: ${result.value:,.2f}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Financial calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_simple = subparsers.add_parser("simple", help="simple interest")
    p_simple.add_argument("principal", type=float)
    p_simple.add_argument("annual_rate", type=float)
    p_simple.add_argument("years", type=float)

    p_compound = subparsers.add_parser("compound", help="compound interest")
    p_compound.add_argument("principal", type=float)
    p_compound.add_argument("annual_rate", type=float)
    p_compound.add_argument("years", type=float)
    p_compound.add_argument("--compounds-per-year", type=int, default=12)

    p_loan = subparsers.add_parser("loan", help="monthly loan payment")
    p_loan.add_argument("principal", type=float)
    p_loan.add_argument("annual_rate", type=float)
    p_loan.add_argument("years", type=float)

    p_annuity = subparsers.add_parser("annuity", help="future value of recurring contributions")
    p_annuity.add_argument("periodic_contribution", type=float)
    p_annuity.add_argument("annual_rate", type=float)
    p_annuity.add_argument("years", type=float)
    p_annuity.add_argument("--contributions-per-year", type=int, default=12)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "simple":
        value = simple_interest(args.principal, args.annual_rate, args.years)
        result = CalculationResult("Final balance", value)
    elif args.command == "compound":
        value = compound_interest(
            args.principal,
            args.annual_rate,
            args.years,
            args.compounds_per_year,
        )
        result = CalculationResult("Final balance", value)
    elif args.command == "loan":
        value = monthly_loan_payment(args.principal, args.annual_rate, args.years)
        result = CalculationResult("Monthly payment", value)
    else:
        value = future_value_annuity(
            args.periodic_contribution,
            args.annual_rate,
            args.years,
            args.contributions_per_year,
        )
        result = CalculationResult("Future value", value)

    print(_format_result(result))


if __name__ == "__main__":
    main()
