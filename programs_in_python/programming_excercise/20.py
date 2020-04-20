'''

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

'''
# Using Class Method:

class mycls():
	def __init__(self, n):
		self.n = n
	
	def generate(self):
		for i in range(0, self.n+1):
			if(i%7==0):
				yield(i)

obj = mycls(50)
for i in obj.generate():
	print(i)

# Using function in python:

def putNumbers(n):
    i = 0
    while(i<n):
        j=i
        i=i+1
        if(j%7==0):
            yield(j)

for i in putNumbers(100):
    print(i)
