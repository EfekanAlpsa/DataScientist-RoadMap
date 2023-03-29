import numpy as np

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])

print(a, "\n")

for row in a:
    print(row)

print("\n")

for cell in a.flat:
    print(cell)