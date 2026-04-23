#!/usr/bin/env python3
"""Simple CLI invoice generator.

Creates a plain-text invoice from command line arguments and optional line items.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable


@dataclass
class LineItem:
    description: str
    quantity: float
    unit_price: float

    @property
    def total(self) -> float:
        return self.quantity * self.unit_price


def parse_line_item(raw: str) -> LineItem:
    """Parse a single line item formatted as description:quantity:unit_price."""
    parts = raw.split(":")
    if len(parts) != 3:
        raise ValueError(
            f"Invalid item '{raw}'. Use format description:quantity:unit_price"
        )

    description, quantity_str, price_str = parts

    try:
        quantity = float(quantity_str)
        unit_price = float(price_str)
    except ValueError as exc:
        raise ValueError(
            f"Invalid number in item '{raw}'. Quantity and unit_price must be numeric."
        ) from exc

    if quantity < 0 or unit_price < 0:
        raise ValueError(f"Invalid item '{raw}'. Quantity and unit_price must be >= 0.")

    return LineItem(description=description.strip(), quantity=quantity, unit_price=unit_price)


def currency(amount: float) -> str:
    return f"${amount:,.2f}"


def build_invoice(
    invoice_number: str,
    seller: str,
    client: str,
    items: Iterable[LineItem],
    tax_rate: float,
    issue_date: date,
    due_days: int,
) -> str:
    line_items = list(items)
    subtotal = sum(item.total for item in line_items)
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    due_date = issue_date + timedelta(days=due_days)

    width = 78
    lines = [
        "=" * width,
        f"INVOICE #{invoice_number}",
        "=" * width,
        f"Issue Date : {issue_date.isoformat()}",
        f"Due Date   : {due_date.isoformat()} ({due_days} days)",
        "",
        f"From       : {seller}",
        f"Bill To    : {client}",
        "",
        "Items",
        "-" * width,
        f"{'Description':40} {'Qty':>8} {'Unit':>12} {'Line Total':>14}",
        "-" * width,
    ]

    for item in line_items:
        lines.append(
            f"{item.description[:40]:40} {item.quantity:>8.2f} {currency(item.unit_price):>12} {currency(item.total):>14}"
        )

    lines.extend(
        [
            "-" * width,
            f"{'Subtotal':>62} {currency(subtotal):>14}",
            f"{'Tax':>53} ({tax_rate * 100:.2f}%) {currency(tax_amount):>14}",
            f"{'Total':>62} {currency(total):>14}",
            "=" * width,
        ]
    )

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a plain-text invoice")
    parser.add_argument("--invoice-number", required=True, help="Invoice identifier")
    parser.add_argument("--seller", required=True, help="Seller/company name")
    parser.add_argument("--client", required=True, help="Client/company name")
    parser.add_argument(
        "--item",
        action="append",
        default=[],
        metavar="DESCRIPTION:QTY:UNIT_PRICE",
        help="Line item (can be used multiple times)",
    )
    parser.add_argument(
        "--tax-rate",
        type=float,
        default=0.0,
        help="Tax rate as decimal (example: 0.0825 for 8.25%%)",
    )
    parser.add_argument(
        "--due-days",
        type=int,
        default=30,
        help="Days until invoice due date",
    )
    parser.add_argument(
        "--output",
        default="invoice.txt",
        help="Output file path (default: invoice.txt)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.item:
        raise SystemExit("At least one --item is required")

    if args.tax_rate < 0:
        raise SystemExit("--tax-rate must be >= 0")

    if args.due_days < 0:
        raise SystemExit("--due-days must be >= 0")

    try:
        items = [parse_line_item(raw) for raw in args.item]
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    invoice_text = build_invoice(
        invoice_number=args.invoice_number,
        seller=args.seller,
        client=args.client,
        items=items,
        tax_rate=args.tax_rate,
        issue_date=date.today(),
        due_days=args.due_days,
    )

    output_path = Path(args.output)
    output_path.write_text(invoice_text + "\n", encoding="utf-8")
    print(f"Invoice written to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
