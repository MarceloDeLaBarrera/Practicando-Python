for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print("X", end=" ")
        else:
            print("_", end=" ")
    print()
