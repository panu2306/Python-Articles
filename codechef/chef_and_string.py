"""
Link to problem: https://www.codechef.com/problems/RECNDSTR
"""

def L(x):
	s = x[1:]
	c = x[0]
	return s+c
	
def R(x):
	s = x[:-1]
	c = x[-1]
	return c+s

N = int(input("Enter Number of test cases:"))
for i in range(N):
	s = input()
	if(R(s) == s and R(s) == s):
		print("YES")
	else:
		print("NO")

