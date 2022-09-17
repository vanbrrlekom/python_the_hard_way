from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two on one line too, how?
indata = open(from_file).read()

print "the input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" % exists(to_file)

out_file = open(to_file, "w")
out_file.write(indata)

print "Allright, all done"

out_file.close()
