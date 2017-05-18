ten_things = "Apples Oranges Crows Telephones Light sugar"

print "Wait these are not 10 things"

stuff = ten_things.split (' ')
more_stuff = ["Day","Night","song","Frisbee","Corn","banana","girl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding",next_one
	stuff.append(next_one)
	print "theres %d items now" %len(stuff)

print "There we go",stuff

print "Lets do some things with stuff"

print stuff[1]
print stuff [-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

