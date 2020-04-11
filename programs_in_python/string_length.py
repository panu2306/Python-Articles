s = "Hello World"

# without using len():

count = 0
for i in s:
	count+=1

print("String Length using counter: {}".format(count))	


# Pythonic Way:

print("String Length using len() function: {}".format(len(s)))	
