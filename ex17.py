def cheese_and_crackers(cheese_count,crackers_count):
	print "You have %d boxes of cheese" %cheese_count
	print "You have %d boxes of crackers" %crackers_count
	print "Thats enough fro the party"
	print "Get a Blanket\n"

print "We can just give the fncs numbers directly"
cheese_and_crackers(20,30)

print"OR we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can do math inside too"
cheese_and_crackers(10+50,70-20)


