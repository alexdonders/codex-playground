# Trading Backtest Example

This is a minimal example project for running backtests on a trading strategy and displaying the results using a simple dashboard.

## Requirements

- Python 3
- pandas
- matplotlib

Install dependencies (if needed):

```bash
pip install pandas matplotlib
```

## Usage

Run the backtester from the command line, specifying the symbol and timeframe. Timeframes follow pandas offset aliases.

```bash
python main.py --symbol AAPL --timeframe D --periods 100
```

This command generates sample data, runs a moving average crossover strategy, and shows a matplotlib dashboard with cumulative returns.
