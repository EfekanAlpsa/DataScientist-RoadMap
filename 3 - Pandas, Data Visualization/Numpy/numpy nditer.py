import numpy as np

a = np.arange(12).reshape(3, 4)

print(a, "\n")

# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

for cell in a.flatten():
    print(cell)

print("\n")

for x in np.nditer(a, order='C'):       # There is a 2 option : C Order and Fortran Order
    print(x)

# If you want to go column by column instead of row by row
print("\n")

for x in np.nditer(a, order='F'):
    print(x)

print("\n")

# If we want to print an entire column on each iteration [0,4,8][1,5,9]...

for x in np.nditer(a, order='F', flags=["external_loop"]):
    print(x)

print("\n")

for x in np.nditer(a, op_flags=["readwrite"]):
    x[...] = x*x

print("\n")
print(a)

# Now let's iterate two arrays simultaneously

b = np.arange(3, 15, 4).reshape(3, 1)

print(b, "\n")

for x,y in np.nditer([a, b]):
    print(x, y)
