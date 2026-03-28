# House Price Predictor using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset: Size (sq ft) vs Price ($)
data = {
    "Size": [500, 700, 1000, 1200, 1500, 1800, 2000],
    "Price": [150000, 200000, 250000, 300000, 350000, 400000, 450000]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Features and labels
X = df[['Size']]  # Feature
y = df['Price']   # Label

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new house
new_size = [[1600]]
predicted_price = model.predict(new_size)
print(f"\nPredicted price for house of size {new_size[0][0]} sq ft: ${predicted_price[0]:.2f}")

# Model coefficients
print("\nModel Coefficient:", model.coef_[0])
print("Model Intercept:", model.intercept_)
