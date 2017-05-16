i  = 0
numbers = []
while (i<6):
	print "at the top is %d" %i
	numbers.append(i)
	
	i = i + 1
	print "numbers now : ",numbers
	print "Ath the bottom is %d" %i 
print "the numbers:"

for num in numbers:
	print num
