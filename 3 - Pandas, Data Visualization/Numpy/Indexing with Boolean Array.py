import numpy as np

a = np.arange(12).reshape(4, 3)
print(a, "\n")

b = a > 4
print(b, "\n")

print(a[b], "\n")
# It looked at b array and then wherever it found true it returned those elements from this original array

a[b] = -1
print(a)    # Replace it with minus 1
