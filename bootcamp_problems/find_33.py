'''

FIND 33:

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False


'''

def find_33(l):
	for i in range(len(l)-1):
		if(l[i] == 3 and l[i+1] == 3):
			return True
		else:
			continue
	return False

print(find_33([1, 3, 4, 3, 3]))
