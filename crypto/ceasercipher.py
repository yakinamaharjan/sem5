
text = input("Enter plain text: ")
s = int(input("Enter no by which to shift: "))

cipher = ""
for i in range(len(text)):
    char = text[i]
    o = ord(char)
    
    if (char.isupper()):
        cipher += chr((o + s - 65) % 26 + 65)
    else:
        cipher += chr((o + s - 97) % 26 + 97)

print (f"\nPlain text: {text}")
print (f"Cipher text: {cipher}")