import numpy as np

n = [4, 5, 6]
print(n[0:2])
print(n[-1], "\n")

a = np.array([4, 5, 6])
print(a[0:2])
print(a[-1], "\n")

a =np.array([[4, 5, 6], [1, 2, 3], [8, 7, 9]])
print(a)
print(a[1, 2], "\n")      # row 1 , column 2

print(a[0:2, 2], "\n")    # row 0 row 1 and column 2

print(a[-1], "\n")    # [8, 7, 9]

print(a[-1, 0:2], "\n")     # [8 7]

print(a[:, 1:3])
