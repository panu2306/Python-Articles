'''

OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'

'''

def old_macdonald(s):
	s1 = []
	s = s.capitalize()
	for i in range(len(s)):
		if(i==3):
			s1.append(s[i].upper())
		else:
			s1.append(s[i])
	return ''.join(s1)

print(old_macdonald('macdonald'))

