def fibonacci_series(num):
	a = 1
	b = 1
	for i in range(num+1):
		print(a, end=' ')
		a, b = b, a+b
	print()

def fibonacci_series_rec(num):
	a = 1
	if(num <= 1):
		return 1
	else:
		return fibonacci_series_rec(num-1) + fibonacci_series_rec(num-2)

limit = 10
fibonacci_series(limit)

print(fibonacci_series_rec(limit))
