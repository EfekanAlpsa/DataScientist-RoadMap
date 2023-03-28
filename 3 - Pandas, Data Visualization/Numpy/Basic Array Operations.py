import numpy as np

a = np.array([5, 6, 10])
print(a[0])
print(a[2], "\n")

a = np.array([[1, 2], [3, 4], [5, 6]])
print("Dimension 1 : ", a.ndim, "\n")     # It shows Dimension

a = np.array([7, 8, 9])
print("Dimension 2 : ", a.ndim, "\n")

print("Item Size : ", a.itemsize, "\n")    # It shows item's size

a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)     # We can change type of items
print("Item Size 2 : ", a.itemsize, "\n")

print(a.size, "\n")   # It shows size

print(a, "\n")        # Let's check our array
print(a.shape, "\n")  # It will show (3,2)    --> 3 rows 2 column


a = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
print(a, "\n")

a = np.array([[1, 2], [3, 4], [5, 6]])

# If you want to initialize your array than ,

print(np.zeros((3, 4)), "\n")
print(np.ones((3, 4)), "\n")

# What does range function do ?

l = range(5)
print(l[0])
print(l[1])
print(l[2], "\n")

# Created a list , Numpy has a similar one

print(np.arange(1, 5), "\n")

print(np.arange(1, 5, 2), "\n")   # 1 = Start /  5 = End 2 / 2 = Number of steps

print(np.linspace(1, 5, 10), "\n")      # 1 = Start / 5 = Stop / 10 = Number


# If you want reshape your array than ,

print(a.reshape(2, 3), "\n")

print("Ravel Func : ", a.ravel(), "\n")


# Math Functions

print("Min : ", a.min(), "\n")
print("Max : ", a.max(), "\n")
print("Sum : ", a.sum(), "\n")

print("Sum Axis 0 : ", a.sum(axis=0), "\n")
print("Sum Axis 1 : ", a.sum(axis=1), "\n")

print(np.sqrt(a), "\n")

print("standard deviation : ", np.std(a), "\n")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("A + B : ", a+b, "\n")
print("A * B : ", a*b, "\n")
print("A / B : ", a/b, "\n")

print(a.dot(b))     # It's gonna do matrix products of these two individual matrices


