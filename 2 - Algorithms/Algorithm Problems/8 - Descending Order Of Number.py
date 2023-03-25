rows = 10

for i in range(rows, 0, -1):
    n = i
    for j in range(0, i):
        print(n, end=" ")
    print("\r")