def multiplicative_congruent(x0, a, m, n):
    x1 = 0
    print("Sequence of random numbers are: ")
    for i in range(0, n):
        x1 = (a * x0) % m
        r = x1 / m
        print(f"{round(r, 2)}")
        x0 = x1


x0 = int(input("Enter the value of seed x0: "))
a = int(input("Enter the value of multiplier a: "))
m = int(input("Enter the value of modulo m: "))
n = int(input("Enter no. of elements in the sequence: "))

multiplicative_congruent(x0, a, m, n)