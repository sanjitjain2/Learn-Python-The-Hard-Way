from sys import argv

script,user_name = argv
prompt = '>'

print "hi %s i m the %s script" %(user_name,script)
print "i d like to ask u a few questions"
print "do you like me %s??" %user_name
likes = raw_input(prompt)

print "where do u live??"
live = raw_input(prompt)

print "which computer do you have?"
computer = raw_input(prompt)

print """alright so you said %r about liking me.
you live in %r,and u have a %r computer.nice"""  %(likes,live,computer)
