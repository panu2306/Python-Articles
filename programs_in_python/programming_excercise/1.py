'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).

The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

# Using List in Python:

def multiple_of_seven(start, end):
	l = []
	for i in range(start, end+1):
		if((i%7 == 0) and (i%5 != 0)):
			l.append(str(i))

	return l

print(','.join(multiple_of_seven(2000, 3200)))
		

# Using yield in Python:
def multiple_seven(start, end):
	for i in range(start, end+1):
		if((i%7==0) and (i%5!=0)):
			yield(str(i))

for i in multiple_seven(2000, 3200):
	print(i, end=',')
