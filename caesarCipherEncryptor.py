def caesarCipherEncryptor(string, key):
	newLetters = []
	newkey = key % 26
	for letter in string:
		newLetters.append(getNewletter(letter,newkey))
	return "".join(newLetters)

def getNewletter(letter,key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96+newLetterCode % 122)

caesarCipherEncryptor("abc", 54)
