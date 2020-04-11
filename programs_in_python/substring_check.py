s1 = "Helllo"
s2 = "lo"

# Pythonic Way:
print(s2 in s1)

# Normal Way:
def isSubstring(s1, s2):
	for letter1 in s1:
		for letter2 in s2:
			if(letter2 != letter1):
				break
		if(s2.index(letter2) + 1 == len(s2)):
			return "True"
		else:
			return "False"

print(isSubstring(s1, s2))
