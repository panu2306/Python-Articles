def isprime(num):
	if(num > 1):
		for i in range(2, num//2+1):
			if(num%i == 0):
				break
		else:
			return True
	else:
		return False
			

if(__name__ == '__main__'):
	num = 10
	for i in range(1, num+1):
		if(num%i == 0 and isprime(i)):
			print(i)

