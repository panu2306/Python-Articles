'''

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

'''

def calculate_digits_and_letters(sentence):
	digit_count, letter_count = 0, 0
	for i in sentence:
		if(i.isdigit()):
			digit_count += 1
		if(i.isalpha()):
			letter_count += 1
	return digit_count, letter_count

digit_count, letter_count = calculate_digits_and_letters('hello world! 123')

print("LETTERS {}\nDIGITS {}".format(letter_count, digit_count))
