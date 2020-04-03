myfile = open('myfile.txt')
# To read lines: 
print(myfile.read())

# To seek the read pointer to particular index:
myfile.seek(5)
print(myfile.read())

myfile.seek(0)
# To read file and convert lines into list with each element pointing to each line:
print(myfile.readlines())

# The first line of code requires to close the file after all operations using following line: 
myfile.close()

# Now, its not a good practice to always write file.close() line to close the file after doing only some operations. Therefore, python has following way after using it we do not require to close the file as it automaically closes the file after performing the operations. 

with open('myfile.txt') as myfile:
	contents = myfile.read()
	print(contents)
