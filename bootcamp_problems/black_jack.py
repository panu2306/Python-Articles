'''

BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19

'''

def black_jack(*args):
	if(sum(args) <= 21):
		return sum(args)
	elif(11 in args):
		return sum(args)-10
	else:
		return 'BUST'
	
print(black_jack(9, 9, 11))
