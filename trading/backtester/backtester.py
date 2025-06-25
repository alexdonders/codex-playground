import pandas as pd

from .strategy import Strategy

class Backtester:
    def __init__(self, data: pd.DataFrame, strategy: Strategy):
        self.data = data
        self.strategy = strategy

    def run(self):
        """Run the strategy and calculate returns."""
        data_with_signals = self.strategy.generate_signals(self.data)
        data_with_signals['returns'] = data_with_signals['Close'].pct_change()
        data_with_signals['strategy_returns'] = data_with_signals['returns'] * data_with_signals['signal'].shift(1)
        data_with_signals['cum_returns'] = (1 + data_with_signals['returns']).cumprod()
        data_with_signals['cum_strategy'] = (1 + data_with_signals['strategy_returns']).cumprod()
        return data_with_signals

def load_sample_data(symbol: str, timeframe: str, periods: int = 100):
    """Generate sample OHLC data."""
    rng = pd.date_range(end=pd.Timestamp.today(), periods=periods, freq=timeframe)
    df = pd.DataFrame(index=rng)
    df['Open'] = pd.np.random.rand(periods) * 100
    df['High'] = df['Open'] + pd.np.random.rand(periods)
    df['Low'] = df['Open'] - pd.np.random.rand(periods)
    df['Close'] = df['Open'] + (pd.np.random.rand(periods) - 0.5)
    df['Volume'] = pd.np.random.randint(100, 1000, size=periods)
    df['Symbol'] = symbol
    return df
