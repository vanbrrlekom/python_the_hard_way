print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant ber here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    if bear == "1":
        print "The bear didn't like that! It's coming at you and, uh oh, IT'S GOT A GUN!!"
        gun = raw_input("> ")

        if gun == "I take the gun":
            print "Wow, somehow, that works, you take the gun. Good job, it looks like you're safe"
        elif gun == "Run":
            print "You run away"
        else:
            print "Did you really think that was going to work? Well, it didn't. You die."

    elif bear == "2":
        print "The eats your legs off. Good job!"
    else:
        print "well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare inte the endluss abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else: 
        print "The insanity rots your eyes into a pool of muck. Good job!"

else: 
    print "You stumble around and fall on a knife and die. Good job!"
