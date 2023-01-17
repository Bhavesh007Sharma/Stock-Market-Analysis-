import pandas as pd

class TechnicalIndicators:
    def __init__(self, period_MA, period_RSI, period_Stoch, period_MACD):
        self.period_MA = period_MA
        self.period_RSI = period_RSI
        self.period_Stoch = period_Stoch
        self.period_MACD = period_MACD
        
    def moving_average(self, data):
        ma = data['close'].rolling(self.period_MA).mean()
        return ma
    
    def relative_strength_index(self, data):
        delta = data['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(self.period_RSI).mean()
        avg_loss = loss.rolling(self.period_RSI).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def stochastic_oscillator(self, data):
        lows = data['low'].rolling(self.period_Stoch).min()
        highs = data['high'].rolling(self.period_Stoch).max()
        k = 100 * ((data['close'] - lows) / (highs - lows))
        d = k.rolling(3).mean()
        return k, d
    
    def macd(self, data):
        ema_12 = data['close'].ewm(span=12).mean()
        ema_26 = data['close'].ewm(span=26).mean()
        macd = ema_12 - ema_26
        signal = macd.ewm(span=9).mean()
        return macd, signal
