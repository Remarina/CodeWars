"""
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.
"""

def pig_it(text):
	return ' '.join([''.join([item[1:],item[0],'ay']) if item.isalpha() \
		else item for item in text.split() ])

print(pig_it('Quis custodiet ipsos custodes ?'))