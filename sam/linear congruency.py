def linear_congruent(x0, a, c, m, n):
    x1 = 0
    print("Sequence of random numbers are: ")
    for i in range(0, n):
        x1 = (a * x0 + c) % m
        r = x1 / m
        print(f"{round(r, 2)}")
        x0 = x1

print("\n")
x0 = int(input("Enter the value of seed x0: "))
a = int(input("Enter the value of multiplier a: "))
c = int(input("Enter the value of constant c: "))
m = int(input("Enter the value of modulo m: "))
n = int(input("Enter no. of elements in the sequence: "))

linear_congruent(x0, a, c, m, n)
