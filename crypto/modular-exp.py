
def fast_exp(b, n, m):
    print("\nb \t n \t m \t r")
    r = 1
    if 1 & n:
        r = b
    while n:
        print(f"{b} \t {n} \t {m} \t {r}")
        n >>= 1
        b = (b * b) % m
        if n & 1: 
            r = (r * b) % m
    return r

b = int(input("\n\nEnter b: "))
n = int(input("Enter n: "))
m = int(input("Enter m: "))

r = fast_exp(b, n, m)

print(f"\n{b} ^ {n} mod {m} = {r}")

