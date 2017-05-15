from sys import argv
from os.path import exists

script,from_file,to_file = argv

#print "Copying %s to %s" %(from_file,to_file)

#in_file = open(from_file)
#indata = (in_file).read()

#print "Input file is %d bytes long" %(len(indata))

#print "does the output file exits?? %r" %(exists(to_file))

#print "Ready,hit ENTER to continue,CTRL+C to abort"

#raw_input()

#out_file = open(to_file,'w')

(open(to_file,'w')).write((open(from_file)).read())

#print "Alright!! Its done"

#out_file.close()
#in_file.close()
