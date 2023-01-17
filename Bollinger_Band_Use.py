# Import the data
data = pd.read_csv('stock_data.csv')

# Create an instance of the BollingerBands class
bb = BollingerBands(data)

# Calculate the Bollinger Bands
bb.calculate_bands()

# Plot the Bollinger Bands
bb.plot_bands()

# Detect Reversals
buy_signals, sell_signals = bb.detect_reversals()
print("Buy signals: \n", buy_signals)
print("Sell signals: \n", sell_signals)

# Detect Double Bottoms
double_bottoms = bb.detect_double_bottoms()
print("Double bottoms: \n", double_bottoms)

# Detect Riding the Bands
riding_bands = bb.detect_riding_bands()
print("Riding the bands: \n", riding_bands)

# Detect Bollinger Band Squeeze
bollinger_squeeze = bb.detect_bollinger_squeeze()
print("Bollinger squeeze: \n", bollinger_squeeze)
