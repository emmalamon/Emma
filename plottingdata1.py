import matplotlib.pyplot as plt
import pandas as pd

file_path = 'cleandata1.csv'
data = pd.read_csv(file_path, na_values=['no data'], encoding= 'utf-8')

df = pd.DataFrame(data)

first_3 = df.head(3)
last_3 = df.tail(3)

# Combine the first 5 and last 5 rows
combined_df = pd.concat([first_3, last_3])

# Get X and Y values from the combined DataFrame
X = list(combined_df.iloc[:, 0])  # Assuming first column is "Country"
Y = list(combined_df.iloc[:, 2])  # Assuming third column is "GDP"

# Plot the data
plt.bar(X, Y, color='g')
plt.title("Top 3 highest and lowest GDP countries")
plt.xlabel("Country")
plt.ylabel("GDP")

#Save the bar chart as a png
plt.savefig('bar_chart.png')
# Show the plot
plt.show()


X = list(df.iloc[:,3])
Y = list(df.iloc[:,1])

plt.scatter(X, Y, color='g') 
plt.title("Happiness in relation to social support") 
plt.xlabel("Social support") 
plt.ylabel("Happiness (out of 10)")

plt.savefig('scatter_chart.png')
plt.show()