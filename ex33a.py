print "What number to start with?"
start = int(raw_input("> "))
print "What number to finish at?"
finish = int(raw_input("> "))

i = start
numbers = []

def change_limits(i, finish):
	while i < finish:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	

change_limits(start, finish)
	
print "The numbers: "

for num in numbers:
	print num