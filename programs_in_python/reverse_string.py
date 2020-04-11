s = "Hello World"

# Using reversed function:
print("Reversed string using reversed function: ", ''.join(reversed(s)))

# Using for loop:
def reverse(s):
	reverse_string = ''
	for i in s:
		reverse_string = i + reverse_string
	return reverse_string

print("Reverse Strign using for loop:", reverse(s))
	
# Using stack in python: 
def create_stack():
	stack = []
	return stack

def push_stack(stack, ele):
	stack.append(ele)

def pop_stack(stack):
	ele = stack.pop()
	return ele

stack = create_stack()

for letter in s:
	push_stack(stack, letter)

reverse_string = ''

for letter in s: 
	reverse_string += pop_stack(stack)

print("Reversed String using Stack:", reverse_string)


# Using Slice :

print("Reversed String using Slicing:", s[::-1])
