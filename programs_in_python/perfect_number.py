num = 28

def divisor(num):
	for i in range(1, num//2+1):
		if(num%i == 0):
			yield(i)

sum = 0
for i in divisor(num):
	sum += i

if(sum == num):
	print("Perfect Number")
