# Storytelling with Graphs

import matplotlib.pyplot as plt

# Sample data
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [120, 150, 90, 60]

# 1. Bar Chart
plt.bar(fruits, sales, color='skyblue')
plt.title("Fruit Sales - Bar Chart")
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.show()

# 2. Pie Chart
plt.pie(sales, labels=fruits, autopct='%1.1f%%', colors=['red','yellow','pink','brown'])
plt.title("Fruit Sales - Pie Chart")
plt.show()

# 3. Histogram
ages = [22, 25, 30, 22, 24, 28, 25, 30, 27]
plt.hist(ages, bins=5, color='green', edgecolor='black')
plt.title("Age Distribution - Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Short Data Story
print("\nData Story:")
print("1. Bananas are the best-selling fruit, making up 37.5% of sales.")
print("2. Apples follow closely behind at 30%.")
print("3. Cherries and Dates are less popular.")
print("4. Age distribution shows most people are in early to mid-20s.")
print("5. Visualizations help quickly understand trends and distribution.")
