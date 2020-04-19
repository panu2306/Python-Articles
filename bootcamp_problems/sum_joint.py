def digits_sum(num):
	sum = 0
	while(num > 0):
		rem = num % 10
		sum += rem
		num = num // 10
	return sum

def compute_join_points(s1, s2):
	sum1 = 0
	sum2 = 1
	while(s1 != s2):
		sum1 = s1 + digits_sum(s1)
		sum2 = s2 + digits_sum(s2)
		s1 = sum1
		s2 = sum2
		if(s1 == s2):
			return s1
 
			
print(compute_join_points(471, 480))

