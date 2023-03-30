import numpy as np

a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)

print(a, "\n")
print(b, "\n")

print("Vertical : ", np.vstack((a, b)), "\n")      # Vertical

print("Horizontal : ", np.hstack((a, b)), "\n")      # Horizontal

a = np.arange(30).reshape(2, 15)
print("3 Different Equal Size Array : ", np.hsplit(a, 3))

result = np.hsplit(a, 3)
print(result[0])

result = np.vsplit(a, 2)
print(result[1])
