'''

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''

def sorted_words(word_string):
	sorted_word_list = sorted(word_string.split(','))
	return sorted_word_list

print(','.join(sorted_words('without,hello,bag,world')))
