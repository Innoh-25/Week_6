import matplotlib.pyplot as plt

# -------------------------------
# 📊 Bar Chart: Population of 5 Countries
# -------------------------------
countries = ['USA', 'India', 'China', 'Brazil', 'Nigeria']
populations = [331, 1391, 1444, 213, 206]  # in millions

plt.figure(figsize=(8, 5))
plt.bar(countries, populations, color='skyblue')
plt.title('Population of 5 Countries')
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -------------------------------
# 🥧 Pie Chart: Student’s Daily Time Allocation
# -------------------------------
activities = ['Sleep', 'Study', 'Exercise', 'Leisure', 'Meals', 'Others']
hours = [8, 6, 2, 4, 2, 2]

plt.figure(figsize=(6, 6))
plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title('Student Daily Time Allocation (24 Hours)')
plt.tight_layout()
plt.show()

# -------------------------------
# 🌡️ Line Chart: Temperature Changes During the Day
# -------------------------------
times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [20, 30, 25, 18]  # in °C

plt.figure(figsize=(8, 5))
plt.plot(times, temperatures, marker='o', linestyle='-', color='orange')
plt.title('Temperature Changes During the Day')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()
