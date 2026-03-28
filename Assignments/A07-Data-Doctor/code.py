# Data Doctor: Dataset Cleaning

import pandas as pd

# Sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Alice"],
    "Age": [25, None, 22, 28, None, 25],
    "City": ["New York", "Los Angeles", "new york", "Chicago", "Chicago", "New York"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. Standardize text (Title case for City)
df['City'] = df['City'].str.title()

print("\nCleaned DataFrame:\n", df)

# Explanation
print("\nCleaning Summary:")
print("- Removed duplicate rows")
print("- Filled missing 'Age' with mean")
print("- Standardized 'City' names to Title Case")
