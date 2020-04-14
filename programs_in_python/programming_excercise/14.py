'''

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

'''

def upper_and_lower(sentence):
	upper_count, lower_count = 0, 0
	for letter in sentence:
		if(letter.isalpha() and letter.isupper()):
			upper_count += 1
		if(letter.isalpha() and letter.islower()):
			lower_count += 1
	return upper_count, lower_count

upper_count, lower_count = upper_and_lower('Hello world!')

print(f"UPPER CASE {upper_count}\nLOWER CASE {lower_count}")
		
