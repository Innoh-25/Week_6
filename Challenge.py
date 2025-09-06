# 📦 Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# ----------------------------------------
# 🔢 NumPy: Create array and calculate mean
# ----------------------------------------
nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value = np.mean(nums)
print(f"NumPy Array: {nums}")
print(f"Mean of array: {mean_value}")

# ----------------------------------------
# 📊 Pandas: Load dataset and show summary
# ----------------------------------------
# Creating a small dataset manually
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 25, 22],
    'Score': [88, 76, 90]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# ----------------------------------------
# 🌐 Requests: Fetch data from public API
# ----------------------------------------
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_price = bitcoin_data['bpi']['USD']['rate']
    print(f"\nCurrent Bitcoin Price in USD: ${usd_price}")
else:
    print("\nFailed to fetch data from API.")

# ----------------------------------------
# 📈 Matplotlib: Plot a simple line graph
# ----------------------------------------
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='green')
plt.title('Simple Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.tight_layout()
plt.show()
