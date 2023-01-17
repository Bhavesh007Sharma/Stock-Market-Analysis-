import pandas as pd
import numpy as np

class StockAnalysis:
    def __init__(self, data):
        self.data = data

    def ehler_fisher_transform(self, period):
        high = self.data['High'].values
        low = self.data['Low'].values
        close = self.data['Close'].values

        # Calculate the Ehler Fisher Transform
        fisher = 0.5 * np.log((high + low + close) / (high - low))
        fisher_ma = fisher.rolling(window=period).mean()

        return fisher, fisher_ma

    def elder_force_index(self, period):
        close = self.data['Close'].values
        volume = self.data['Volume'].values

        # Calculate the Elder Force Index
        force_index = close * volume
        force_index_ma = force_index.rolling(window=period).mean()

        return force_index, force_index_ma

    def elder_ray_index(self, period):
        high = self.data['High'].values
        low = self.data['Low'].values
        close = self.data['Close'].values

        # Calculate the Elder Ray Index
        bull_power = close - low
        bear_power = high - close
        elder_ray = bull_power - bear_power
        elder_ray_ma = elder_ray.rolling(window=period).mean()

        return elder_ray, elder_ray_ma

    def fractal_chaos_bands(self, period):
        close = self.data['Close'].values

        # Calculate the Fractal Chaos Bands
        fractal_chaos = close.rolling(window=period).mean()
        fractal_chaos_std = close.rolling(window=period).std()
        upper_band = fractal_chaos + fractal_chaos_std
        lower_band = fractal_chaos - fractal_chaos_std

        return fractal_chaos, upper_band, lower_band
