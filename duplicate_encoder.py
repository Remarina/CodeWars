def duplicate_encode(word):
	word = list(word.upper())
	return ''.join(['(' if word.count(letter) == 1 else ')' for letter in word])

print(duplicate_encode("Success"))