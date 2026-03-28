# Build Your First Dataset

import pandas as pd
import matplotlib.pyplot as plt

# Create dataset: Study Hours vs Marks
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [50, 55, 60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Features and Labels
X = df[['Study_Hours']]  # Feature
y = df['Marks']          # Label

print("\nFeatures (X):\n", X)
print("\nLabels (y):\n", y)

# Simple plot to visualize relationship
plt.scatter(X, y, color='blue')
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
