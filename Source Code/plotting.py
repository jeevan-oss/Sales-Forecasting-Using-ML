import matplotlib.pyplot as plt

def plot_forecast(train, test, forecast, title, save_path):
    plt.figure(figsize=(12, 5))
    plt.plot(train.index, train, label="Train")
    plt.plot(test.index, test, label="Actual")
    plt.plot(test.index, forecast, label="Forecast", linestyle="--")
    plt.title(title)
    plt.legend()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
