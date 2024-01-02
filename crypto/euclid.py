def gcd(a, b):
    if a < b:
        (a,b) = (b,a)
    while (a % b != 0):
        (a, b) = (b, a % b)
    return b



a = int(input("\n\nEnter a: "))
b = int(input("Enter b: "))
print("\ngcd (a, b) = ", gcd(a, b))