'''

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81

'''

def square_odd(input_string):
	l = [str(int(item)**2) for item in input_string.split(',') if(int(item)%2 != 0)]
	return l

print(','.join(square_odd('1,2,3,4,5,6,7,8,9')))
