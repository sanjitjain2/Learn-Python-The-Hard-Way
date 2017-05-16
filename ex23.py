print "You enter a dark room with two doors.Do you go through Door 1 or Door 2 ??"

door = int(raw_input(">> "))

if door == 1:
	print "There is a giant bear here eating a cheese cake.What do you do??"
	print "1.Take the cake"
	print "2.Scream at the bear"
	
	bear  = int(raw_input(">> "))
	
	if bear == 1:
		print "The bear eats your head off"
	elif bear == 2:
		print "the bear eats your legs off"
	else:
		print "Well doing %d is better.Bear runs away" %bear

elif door == 2:
	print "You start at an endless abyss"
	print "1.Blueberries"
	print "2.Yellow jacket clothespin"
	print "3.Understanding revolvers yelling melodies"

	insanity = int(raw_input(">> "))
	
	if insanity == 1 :
		print "Your body survives powered by a mind of jello.Good Job!"
	else:
		print "The insanity rots your eyes into a pool of muck.Good Job"

else:	
	print "You stumble and fall ona knife and die.Good Job"

