'''

COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

count_primes(100) --> 25

By convention, 0 and 1 are not prime.

'''
def is_prime(n):
	if(n == 1 or (n%2 == 0 and n!=2)):
		return False
	else:
		for i in range(3, n, 2):
			if(n%i == 0):
				return False
	return True

def count_primes(n):
	count = 0
	for i in range(1, n+1):
		if(is_prime(i)):
			count+=1
	return count

print(count_primes(100))
