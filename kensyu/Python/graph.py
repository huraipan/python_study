import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('./data/005930_2023.01.01_2023.03.08.csv')

# Clean and transform the data
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.sort_index(inplace=True)

# Create the plot
sns.set_style('darkgrid')
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the closing prices on the first y-axis
ax1.plot(df['close'], label='Closing Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')

# Create a second y-axis for the trading volume
ax2 = ax1.twinx()
ax2.plot(df['volume'], color='orange', label='Trading Volume')
ax2.set_ylabel('Volume')

# Set the x-ticks
num_ticks = 10  # Set the number of tick marks
xtick_labels = [df.index[i].strftime('%Y-%m-%d') for i in range(0, len(df), len(df) // num_ticks)]
xtick_positions = [df.index[i] for i in range(0, len(df), len(df) // num_ticks)]
ax1.set_xticks(xtick_positions)
ax1.set_xticklabels(xtick_labels, rotation=90)

# Adjust the plot size and padding of the x-tick labels
plt.subplots_adjust(bottom=0.2)

# Show the legend
fig.legend(loc='upper right', bbox_to_anchor=(0.88, 0.85))

# Set the title
plt.title('Stock Closing Prices and Trading Volumes')

# Show the plot
plt.show()





# df = pd.read_csv('./data/005930_2023.01.01_2023.03.08.csv')