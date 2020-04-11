s = "HelloWorld"

# Using sorted: 
print("Using Sorted and Join Methods: ", "".join(sorted(s.lower())))

# Using ASCII Value:
str_list = list(s.lower())
for i in range(len(str_list)):
	for j in range(len(str_list)):
		if(ord(str_list[i]) < ord(str_list[j])):
			str_list[i], str_list[j] = str_list[j], str_list[i]
# Actually we can compare letters directly but I wanted to know ASCII values.
print("Using ASCII value:", ''.join(str_list))
