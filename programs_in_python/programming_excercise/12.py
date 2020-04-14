'''

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''

def check_num(num):
	n = num
	while(num > 0):
		rem = num % 10 
		if(rem%2 != 0):
			return "False"
			break
		num = num // 10
	else:
		return n

	
def even_digits(start, end):
	num_list = []
	for num in range(start, end+1):
		if(num%2 == 0):
			if(num == check_num(num)):
				num_list.append(num)
		
	return num_list

print(even_digits(1000, 3000))
