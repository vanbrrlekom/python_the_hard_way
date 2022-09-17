from sys import argv

script, user_name = argv
prompt = "input here"

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s" % user_name

likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Allright, so you sad %r about liking me. 
You live in %r. Not sure where that is. 
And ou have %r computer. Nice.
""" % (likes, lives, computer)