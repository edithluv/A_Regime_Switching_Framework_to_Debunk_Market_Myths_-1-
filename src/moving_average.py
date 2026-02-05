import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional, Union


def plot_moving_average(
    csv_file: str,
    price_col: str = "Close",
    date_col: Union[str, int] = 0,
    window: int = 20,
    output: Optional[str] = None,
) -> None:
    """Read a CSV of stock prices, compute a moving average, and plot it.

    Parameters
    ----------
    csv_file : str
        Path to the CSV file containing stock prices.
    price_col : str, optional
        Name of the column containing price information. Default is ``"Close"``.
    date_col : str or int, optional
        Column name or index for dates. Default is the first column (0).
    window : int, optional
        Moving-average window length. Default is ``20``.
    output : str, optional
        If provided, save the plot to this path instead of showing it.
    """

    if window <= 0:
        raise ValueError("window must be positive")

    data = pd.read_csv(csv_file, parse_dates=[date_col])
    date_col_name = data.columns[date_col] if isinstance(date_col, int) else date_col
    data = data.sort_values(date_col_name)
    data.set_index(date_col_name, inplace=True)

    if price_col not in data.columns:
        raise ValueError(f"'{price_col}' column not found in {csv_file}")

    ma_col = f"{window}d_ma"
    data[ma_col] = data[price_col].rolling(window=window).mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data.index, data[price_col], label="Price")
    ax.plot(data.index, data[ma_col], label=f"{window}-Day MA")
    ax.set_title(f"{window}-Day Moving Average")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    if output:
        fig.savefig(output)
        plt.close(fig)
    else:
        plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Plot moving average from a CSV file"
    )
    parser.add_argument("csv_file", help="Path to CSV file with date and price columns")
    parser.add_argument("--price-col", default="Close", help="Name of the price column")
    parser.add_argument(
        "--date-col",
        default=0,
        help="Name or index of the date column (default: first column)",
    )
    parser.add_argument("--window", type=int, default=20, help="Length of the moving-average window")
    parser.add_argument("--output", help="Optional path to save the plot")
    args = parser.parse_args()

    plot_moving_average(
        args.csv_file,
        price_col=args.price_col,
        date_col=args.date_col,
        window=args.window,
        output=args.output,
    )
