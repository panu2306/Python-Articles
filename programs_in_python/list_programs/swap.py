def swap(i1, i2, l):
	l[i1], l[i2] = l[i2], l[i1]
	return l

l = [1, 2, 3, 4, 5]
print("Before swap:",l)
swap(2, 4, l)
print(f'After swap: {l}')

