from sys import argv

script,filename = argv

print "WE are going to erase %r" %filename
print "If you dont want that hit CTRL+C"
print "If you dop want that hit ENTER"

raw_input("?")

print"Opening File..."
target  = open(filename,'w')

print "Truncating the file"
target.truncate()

print "Now Im going to ask you three lines."

line1 = raw_input("This is line 1:")
line2 = raw_input("This is line 2:")
line3 = raw_input("This is line 3:")

print "I m going to write these to the file"

target.write("%s \n %s \n %s" %(line1,line2,line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And Finally close the file...."
target.close()

