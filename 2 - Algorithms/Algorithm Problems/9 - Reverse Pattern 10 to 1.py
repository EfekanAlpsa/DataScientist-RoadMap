rows = 10

for i in range(0, rows+1):
    # inner loop for decrement in i values
    for j in range(rows-i, 0, -1):
        print(j,end=" ")
    print()