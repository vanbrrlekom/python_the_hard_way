from sys import argv

script, filename = argv #gives pythong an argument to do something with

# just prints the gext, with formant, to use the user-generated value
print "We're going to erase %r" % filename
print "If you won't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") #let's user input enter

print "Opening the file..."
target = open(filename, 'w') #open file, write mode

print "Truncating the file. Goodbeye!" #erasing everything in the file
target.truncate()

print "Now I'mg going to ask you for three lines"

line1 = raw_input("Line 1: ") 
line2 = raw_input("Line 2: ")
line3 = raw_input("line 3: ")

print "I'm gping to write these to the file."

target.write("%s, %s, %s" % (line1, line2, line3)) 


print "And finally, we close it."
target.close()