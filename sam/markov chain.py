n = int(input("Enter the number of purchase: "))
x0 = [[0.5, 0.5]]

p = [[0.8, 0.2],
     [0.3, 0.7]]

x1 = [[]]
for n1 in range(n):
    temp = [[0, 0]]
    for i in range(len(x0)):
        for j in range(len(p[0])):
            for k in range(len(p)):
                temp[i][j] += x0[i][k] * p[k][j]
    x1[0] = temp
    x0 = temp

print(f"After {n} purchase, the matrix is: ")
for x in x1:
    print(x)
