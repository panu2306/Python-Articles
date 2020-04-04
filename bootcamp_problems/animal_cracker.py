'''

ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False

'''

def animal_crackers(text):
	return text.split()[0][0].lower() == text.split()[1][0].lower()

print(animal_crackers('Pratik, ranav'))
