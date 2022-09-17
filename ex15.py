from sys import argv #import argv module

script, filename = argv #tell the computer what the thing should be called

txt = open(filename) #opens the file

print "Here's your file %r" % filename #print message about file
print txt.read #read file

print "Type the filename again:" #prints prompt to user
file_again = raw_input(">") #says user to enter file

txt_again = open(file_again) #opens the file again

print txt_again.read #reads the file again