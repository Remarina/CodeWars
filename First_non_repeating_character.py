"""
Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.
"""
from collections import Counter

def first_non_repeating_letter(string):
	for key, val in Counter(string.lower()).items():
		if val == 1: 
			return string[list(string.lower()).index(key)]
	else:
		return ''


print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))