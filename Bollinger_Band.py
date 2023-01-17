import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class BollingerBands:
    def __init__(self, data, window=20, std_dev=2):
        self.data = data
        self.window = window
        self.std_dev = std_dev

    def calculate_bands(self):
        self.data['SMA'] = self.data['Close'].rolling(window=self.window).mean()
        self.data['STD'] = self.data['Close'].rolling(window=self.window).std()
        self.data['Upper Band'] = self.data['SMA'] + (self.data['STD'] * self.std_dev)
        self.data['Lower Band'] = self.data['SMA'] - (self.data['STD'] * self.std_dev)

    def plot_bands(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Close'], label='Close')
        plt.plot(self.data['SMA'], label='SMA')
        plt.plot(self.data['Upper Band'], label='Upper Band')
        plt.plot(self.data['Lower Band'], label='Lower Band')
        plt.legend(loc='best')
        plt.show()

    def detect_reversals(self):
        buy_signals = self.data[(self.data['Close'] < self.data['Lower Band']) & (self.data['Close'].shift(-1) > self.data['Lower Band'].shift(-1))]
        sell_signals = self.data[(self.data['Close'] > self.data['Upper Band']) & (self.data['Close'].shift(-1) < self.data['Upper Band'].shift(-1))]
        return buy_signals, sell_signals

    def detect_double_bottoms(self):
        double_bottoms = self.data[(self.data['Close'] > self.data['Lower Band']) & (self.data['Close'].shift(-1) > self.data['Lower Band'].shift(-1)) & (self.data['Close'].shift(-2) < self.data['Lower Band'].shift(-2))]
        return double_bottoms

    def detect_riding_bands(self):
        riding_bands = self.data[(self.data['Close'] > self.data['SMA']) & (self.data['Close'].shift(-1) > self.data['SMA'].shift(-1)) & (self.data['Close'].shift(-2) > self.data['SMA'].shift(-2))]
        return riding_bands

    def detect_bollinger_squeeze(self):
        bollinger_squeeze = self.data[(self.data['Upper Band'] - self.data['Lower Band']) < (self.data['Upper Band'].rolling(window=20).mean() * 0.1)]
        return bollinger_squeeze
