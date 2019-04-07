import itertools


def permutations(string):
	new_arr = []
	for a in list(set(itertools.permutations(string, len(string)))):
		c = list(a)
		new_arr.append(''.join(c)) 
		#new_arr.append(''.join([*a]))  # *a didn't work in CodeWars task, but it works in sublime
	return new_arr


print(permutations('ab'))
