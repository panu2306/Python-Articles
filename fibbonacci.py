# Fibbonacci using a list: 

def fibbonacci(n):
	a = 1
	b = 1
	fibbo_list = []

	for i in range(n+1):
		fibbo_list.append(a)
		a, b = b, a+b

	return fibbo_list

print(fibbonacci(10))

# Fibbonacci using generators: 

def fibbonacci_using_generator(n):
	a = 1
	b = 1
	for i in range(n+1):
		yield(a)
		a, b = b, a+b

for num in fibbonacci_using_generator(10):
	print(num)

