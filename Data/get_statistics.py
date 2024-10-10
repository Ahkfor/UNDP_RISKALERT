import pandas as pd

# Sample DataFrame with a column of date strings
data = {'Date': ['2017/1/1 0:00', '2018/2/15 12:30', '2019/3/10 18:45']}
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the year from the 'Date' column
df['Year'] = df['Date'].dt.year

# Print the DataFrame with the new 'Year' column
print(df)