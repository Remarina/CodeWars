def find_missing_letter(chars):
	ords = list(map(lambda char: ord(char), chars))
	must_be = list(range(ords[0],ords[-1]+1))
	for i in must_be:
		if i not in ords:
			return chr(i)
			

print(find_missing_letter(['a','b','c','d','f']))