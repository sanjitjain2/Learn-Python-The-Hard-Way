the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quaters']

#the first kind of for-loop goes through a list

for number in the_count:
	print "this is count %d" %number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" %fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" %i

#we can also build lists,first start with an empty one

elements = []
#elements = range(0,6) #a way to skip the next for loop

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list" %i
	#append is a funtion that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Element was %d" %i
