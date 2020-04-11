s = "1He22L4"

new_s = ''
for letter in s:
	if(not letter.isdigit()):
		new_s += letter

print("New String: ", new_s)		
