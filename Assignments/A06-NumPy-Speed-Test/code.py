# NumPy Speed Test

import time
import numpy as np

# Using Python list
list_data = list(range(1_000_000))
start = time.time()
squared_list = [x**2 for x in list_data]
end = time.time()
print(f"Python list time: {end - start:.4f} seconds")

# Using NumPy array
array_data = np.arange(1_000_000)
start = time.time()
squared_array = array_data**2
end = time.time()
print(f"NumPy array time: {end - start:.4f} seconds")

# Observations
print("\nObservations:")
print("1. NumPy operations are significantly faster than Python lists.")
print("2. NumPy uses vectorized operations instead of loops.")
print("3. NumPy arrays are memory-efficient.")
