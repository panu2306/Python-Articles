s = "abcba"
# Using general way:
flag = 0
for i in range(len(s)): 
	if(s[i] != s[-i-1]):
		flag = 1

if(flag == 0):
	print("string is palindrome")
else:
	print("String is not palindrome")


# Using reversed in python:

if(s == ''.join(reversed(s))): 
	print("String is Palindrome")
else:
	print("String is not Palindrome")
