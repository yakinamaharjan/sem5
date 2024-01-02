keys = [[0] * 3 for i in range(3)]

msg = [[0] for i in range(3)]

ciphers = [[0] for i in range(3)]

def getkeys(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keys[i][j] = ord(key[k]) % 65
			k += 1

def encrypt(msg):
	for i in range(3):
		for j in range(1):
			ciphers[i][j] = 0
			for x in range(3):
				ciphers[i][j] += (keys[i][x] *
									msg[x][j])
			ciphers[i][j] = ciphers[i][j] % 26

def Hill(message, key):

	getkeys(key)

	for i in range(3):
		msg[i][0] = ord(message[i]) % 65

	encrypt(msg)

	cipher = []
	for i in range(3):
		cipher.append(chr(ciphers[i][0] + 65))

	print("cipher: ", "".join(cipher))


if __name__ == "__main__":

	message = "ACT"

	key = "GYBNQKURP"

	Hill(message, key)
