def calc_random(new_length, string):

    mid = round(new_length / 2)
    random_number = int(string[mid - 1:mid + n - 1])
    return random_number


n = int(input("Enter no. of digits in seed x0: "))
x0 = int(input("Enter the value of seed x0: "))
numInSequence = int(input("Enter no. of numbers in sequence: "))

print("Sequence of random numbers: ")
for i in range(0, numInSequence):
    x0_square = x0 ** 2
    string = str(x0_square)
    length = len(string)

    if length < 2 * n:
        for j in range(0, 5):
            string = '0' + string
            new_length = len(string)
            if new_length == 2*n:
                break
        random = calc_random(new_length, string)
    elif length == 2 * n:
        random = calc_random(length, string)

    print(random / 1000)
    x0 = random
    