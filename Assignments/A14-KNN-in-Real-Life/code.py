# KNN in Real Life - Small Similarity Example

from sklearn.neighbors import NearestNeighbors
import numpy as np

# Sample user ratings for movies (rows = users, columns = movies)
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])

# Fit KNN model
model = NearestNeighbors(n_neighbors=2, metric='cosine')
model.fit(ratings)

# Find 2 nearest neighbors for first user
distances, indices = model.kneighbors([ratings[0]])

print("Nearest neighbors for User 1:")
for i, idx in enumerate(indices[0]):
    print(f"Neighbor {i+1}: User {idx+1} at distance {distances[0][i]:.2f}")
