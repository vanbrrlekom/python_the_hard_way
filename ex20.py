from sys import argv # import argv package

script, input_file = argv #let's user add an argument in the terminal

#create a function that prints everyting in a text document
def print_all(f):
    print f.read()

#create a function that  goes to the first line in the document
def rewind(f):
    f.seek(0)

# a function with two argument. the first says which line to print, the second which file to read
def print_a_line(line_count, f):
    print line_count, f.readline()

#open the file the user supplied when enterint the line in terminal
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

#here current line is 2
current_line +=  1
print_a_line(current_line, current_file)

#here current line is 3
current_line += 1
print_a_line(current_line, current_file)