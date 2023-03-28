import numpy as np
import sys
import time

l = range(1000)
print("Python List : ", sys.getsizeof(5)*len(l))  # 28000 Bytes

array = np.arange(1000)
print("Numpy Array : ", array.size*array.itemsize)  # 4000 Bytes

# Let's Figure Out it About Time

SIZE = 10000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Python List

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Python List Took : ", (time.time() - start) * 1000)  # Python List Took :  753.8230419158936

# numpy array

start = time.time()
result = a1 + a2
print("numpy Took : ", (time.time() - start) * 1000)    # numpy Took :  84.19632911682129
