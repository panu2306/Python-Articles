def remove_nth_occurrence(occ, word, l):
	count = 0
	if(word in l):
		for i in range(len(l)):
			if(word == l[i]):
				count += 1
				if(count==occ):
					l.pop(i)
					break
		return l
	else:
		return "Word is not present in list"

l = ['abc', 'dada', 'baf', 'abc', 'sfdsf', 'abc']
print(remove_nth_occurrence(3, 'abc', l))
			
		
