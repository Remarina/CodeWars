def iq_test(numbers):
	new_arr = [int(num)%2 for num in numbers.split(' ')]
	for i in new_arr:
		if new_arr.count(i)==1:
			return new_arr.index(i) + 1 


print(iq_test("1 2 2"))