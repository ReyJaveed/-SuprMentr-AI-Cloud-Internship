import pandas as pd

# Sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 22, 28, 24],
    "Marks": [85, 78, 92, 67, 74],
    "City": ["New York", "Los Angeles", "New York", "Chicago", "Chicago"]
}

df = pd.DataFrame(data)

# Display top rows
print("Top rows of dataset:\n", df.head())

# Find column with highest value
max_column = df.max(numeric_only=True).idxmax()
print(f"\nColumn with highest value: {max_column}")

# Count missing values
missing = df.isnull().sum()
print("\nMissing values in each column:\n", missing)

# Insights
print("\nInsights:")
print("1. Highest marks scored:", df['Marks'].max())
print("2. Average age:", df['Age'].mean())
print("3. Cities include:", df['City'].unique())
print("4. Dataset has no missing values")
print("5. Topper student is:", df.loc[df['Marks'].idxmax(), 'Name'])
