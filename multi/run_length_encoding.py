init_string = "aaaaaccccccbbbbbbbdddddddddeeeeeeeee"
print(f"Initial string is {init_string}")
n = len(init_string)
print(f"Initial length of string is {n}")

new_string = ""
index_num = 0
i = 0

while i < n - 1:
    count = 1   
    while i < n - 1 and init_string[i] == init_string[i + 1]:
        count += 1
        i += 1
    i += 1
    new_string += init_string[i - 1] + str(count)

print(f"Encoded String is {new_string}")
print(f"Length of new encoded string is {len(new_string)}")