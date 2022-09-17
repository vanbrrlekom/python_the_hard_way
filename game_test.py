from sys import exit

# a bunch of setup. Here's the inventory.
inventory = """Your inventory consists of the following:
\t a gun 
\t a a stun baton
\t binoculars
\t heat sensor"""


def end(why):
    print(why)
    exit(0)

def left():
    end("placeholder text for left girl")

def right():
    end("placeholder text for right girl")
   

def heat_sensor():
    print("You use the heat sensor. You see one heat signature close by, one to the right and one to the left")
    while True:

        heat_action = input("> ")

        for i in ["middle", "close", "closest", "front", "nearby"]:
            if i in heat_action:
                end("you are ambushed")

        if "left" in heat_action: 
            left_girl()
        elif "right" in heat_action: 
            right_girl()
        else:
            print("Try something else.")
            
def closer():
    closer_text = open("closer.txt") #open the text file for getting closer
    ambushed = open("ambush1.txt")
    print(closer_text.read())
    closer_action = input("> ")

    for i in ["approach", "walk", "closer", "check out", "check it out"]:
            if i in closer_action:
                 end(ambushed.read())

    if "leave" in closer_action:
        end("You realised it was a trap and get away")
    else:
        end("uh oh, I haven't made this open ended, so because you didn't enter anything coherent, it's game over")

def opening():

    print("It's a post-apocalyptic waistland, you're driving in your car and you think you see something in the distance.\n What do you do?")

    #Opens the inventory

    while True: 
        action = input("> ")

        for i in ["approach", "walk", "closer", "check out", "check it out"]:
            if i in action:
                 closer()

        if "binoculars" in action: 
            print("You use the binoculars, you see someone in the distance")
        elif "inventory" in action:
            print(inventory)
        elif "heat sensor" in action:
            heat_sensor()
        
        else:
            print("Try something else")


opening()
