'''

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

'''
import math 

def distance(p1, p2):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	return round(d)

x = 0 
y = 0
i =''
while(True):
	i = input()
	if(not i):
		break
	l = i.split(' ')
	if(l[0] == 'UP'):
		y += int(l[1])
	if(l[0] == 'DOWN'):
		y -= int(l[1])
	if(l[0] == 'RIGHT'):
		x += int(l[1])
	if(l[0] == 'LEFT'):
		x -= int(l[1])

p1 = (0, 0)
p2 = (x, y)
print(distance(p1, p2))







