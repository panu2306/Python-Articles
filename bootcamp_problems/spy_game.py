'''

SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

'''

def spy_game(l):
	count = 0
	for i in l:
		if(i==0):
			count+=1
		if(count >= 2):
			if(i==7):
				return True
	return False
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
