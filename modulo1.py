# Create 2 new lists height and weight
height = [1.46,  1.84, 1.56]
weight = [44,      78,  65]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)
print(height)
print(type(bmi))

print(bmi[bmi>23])