import argparse
from trading.backtester.backtester import Backtester, load_sample_data
from trading.backtester.strategy import Strategy
from trading.backtester.dashboard import display_results


def main():
    parser = argparse.ArgumentParser(description="Run a simple backtest")
    parser.add_argument("--symbol", default="AAPL", help="Symbol to backtest")
    parser.add_argument("--timeframe", default="D", help="Pandas time frame e.g. 'D' for daily")
    parser.add_argument("--periods", type=int, default=100, help="Number of bars to simulate")
    args = parser.parse_args()

    data = load_sample_data(args.symbol, args.timeframe, args.periods)
    strategy = Strategy()
    backtester = Backtester(data, strategy)
    results = backtester.run()
    display_results(results)

if __name__ == "__main__":
    main()
