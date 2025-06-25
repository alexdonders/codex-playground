import matplotlib.pyplot as plt


def display_results(results):
    plt.figure(figsize=(10, 6))
    plt.plot(results.index, results['cum_returns'], label='Buy & Hold')
    plt.plot(results.index, results['cum_strategy'], label='Strategy')
    plt.legend()
    plt.title('Backtest Results')
    plt.xlabel('Time')
    plt.ylabel('Cumulative Returns')
    plt.tight_layout()
    plt.show()
