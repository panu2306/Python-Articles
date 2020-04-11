def factorial(num):
	if(num == 0):
		return 1
	else:
		return factorial(num-1)*num

def factorial_sum(num):
	sum = 0
	while(num != 0):
		r = num % 10
		num = num // 10
		sum += factorial(r)
	return sum

num = 145
if(factorial_sum(num) == num):
	print("Number is strong number")
else:
	print("Number is not strong number")
