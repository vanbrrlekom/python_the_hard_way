tent_things = "Apples oranges Crows Telephone Light Sugar"

print("Wait, there are not ten things on that list, lets fix that")

stuff = tent_things.split(" ") # split(ten_things, " ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #pop(more_stuff)
    print("adding:", next_one)
    stuff.append(next_one) #append(stuff, next_one)
    print(f"there are {len(stuff)} items now.")

print("there we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1]) #whoah, fancy!
print(stuff.pop()) #print(pop(stuff))
print(" ".join(stuff)) #what?? Cool! join(" ", "stuff")
print("#".join(stuff[3:5])) #join(#, stuff[3:5])
