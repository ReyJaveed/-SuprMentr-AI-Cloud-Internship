# Customer Segmentation using K-Means (Repeat)

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset: Customers with Age and Annual Income
data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Age": [25, 34, 22, 45, 23, 36, 52, 40, 28, 30],
    "AnnualIncome": [50000, 60000, 45000, 80000, 42000, 65000, 90000, 70000, 52000, 58000]
}

df = pd.DataFrame(data)

# K-Means clustering
X = df[['Age', 'AnnualIncome']]
kmeans = KMeans(n_clusters=2, random_state=42)  # Using 2 clusters this time
df['Cluster'] = kmeans.fit_predict(X)

print("Customer Segmentation (Repeat):\n", df)

# Visualize clusters
plt.scatter(df['Age'], df['AnnualIncome'], c=df['Cluster'], cmap='coolwarm')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.title('Customer Segmentation (Repeat)')
plt.show()
