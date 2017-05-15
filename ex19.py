def add(a,b):
	print "ADDING %d + %d = " %(a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACT %d - %d = " %(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLY %d * %d = " %(a,b)
	return a*b

def divide(a,b):
	print "DIVIDE %d/%d = " %(a,b)
	return a/b

print "Lets do mathematics with just functions"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "AGE: %d\nHEIGHT: %d\nWEIGHT: %d\nIQ: %d" %(age,weight,height,iq)

#a puzzle

print "puzzle==>"
print "%d" %add(age,subtract(height,multiply(weight,divide(iq,2))))
