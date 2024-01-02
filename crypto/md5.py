# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal)

import hashlib

str = input("\n\n\nEnter a string to be hashed: ")

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is:")
print(result.hexdigest())
