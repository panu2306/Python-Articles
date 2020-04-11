num = 370

def armstrong_num(num):
	sum = 0
	while(num != 0):
		rem = num%10
		num = num//10
		sum += rem**3
	return sum

if(armstrong_num(num) == num):
	print("Number is Armstrong Number")
else:
	print("Number is not Armstrong Number")
