from collections import namedtuple
#from dbm.ndbm import library
from logging import PlaceHolder
from pickle import TRUE
from sys import exit

Option = namedtuple("Option", ["label", "callback"])
Inventory = []

#A convenience fuction to print long bits of text line by line
def slowprint(x):
    for line in (x):
            print(line.strip())
            input("")



class Menu:
    SEPARATOR = '-'

    _title = ''


    def __init__(self, title, options):
        self._title = title
        self._options = []


        #Set the options to whatever the nemu is meant to contain

        for option in options:
            self._options.append(Option(option[0], option[1]))

    #Make a separated header
    def header(self, text):
        line = self.SEPARATOR * (len(text) + 2)
        return f"{line}\n {text}\n{line}\n"

    #Display the options
    def display(self):
        string = self.header(self._title)

        for i, option in enumerate(self._options):
            string += f"{i + 1} {option.label}\n"

        return string

    #Return somthing depending on user input
    def callback(self, i):
        if i <= len(self._options):
            return self._options[i - 1].callback

#Should the name of the item be consistent with what you'd find in the wild? You could have
#a description in the wild and a description in the inventory. We'll keep that here and 
#implement later
class Item(object):
    def __init__(self, name, description, portable):
        self.name = name
        self.description = description
        self.portable = portable


#Some items
Knife = Item(
    name = "Bloody knife", 
    description =  open("debugging.txt"),#"A bloody knife. There's an inscription on the hilt. You take take a closer look. The inscryption is... your initials. How strange. Eh, probably it probably doesn't mean anything. You pick it up, you freak.",
    portable= True)
Letter = Item(
    name = "Pocket letter",
    description= open("debugging.txt"),#open("pocket_letter_description.txt"),
    portable = True)

Book = Item(
    name = "A boring book", 
    description = "Just a boring old book",
    portable = True)
Incrmination_docs = Item(
    name = "Incriminating documents", 
    description = "It's a piece of paper. The text says \"it was me i did it\". The signature is... your signature.",
    portable= True)
Library_book = Item(
    name = "A fun book", 
    description= "this book is way more fun",
    portable= True)

# When implementing dialogue, it's important to make it in then
# format Menu("title", ["question", "answer"], ["back", "placeholder"])
class Character(object):
    def __init__(
            self, name, description, dialogue, dialogue_opts, n_dialgue_opts, key_item, 
            key_item_dialogue, wrong_item_dialogue, key_item_outcome
            ):
        self.description = description
        self.name = name
        self.dialogue = dialogue
        self.dialogue_opts = dialogue_opts
        self.n_dialgue_opts = n_dialgue_opts + 1
        self.key_item = key_item
        self.key_item_dialogue = key_item_dialogue
        self.key_item_outcome = key_item_outcome
        self.wrong_item_dialogue = wrong_item_dialogue


    def talk(self):
        print(self.dialogue.display())
        choice = int(input("> "))
        while choice < len(self.dialogue_opts):
            slowprint(self.dialogue_opts[choice -1])
            print(self.dialogue.display())
            choice = int(input("> "))
    
            

Emma_Atalle = Character(
    name = "Emma Atalle",
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?\n \n",
    dialogue= Menu(
        "The woman eyes you very suspicously. You get the sense that maybe she suspects you of something. \n What do you talk about?" , [
        ("Don't move?", "None of your business"),
        ("This place","Never ask the name a lady her name"),
        ("Last night", "You tell me, you're the mureder"),
        ("Back", "Back *has* been implemented, so if this message comes up, somethings's gone wrong")]
    ),
    dialogue_opts= [open("emma_dialogue1"), open("emma_dialogue2"), open("emma_dialogue3")],
    n_dialgue_opts = 3,
    key_item = Letter,
    wrong_item_dialogue = """
    The woman looks at you with undisguised annoyance.
    Emma:Oh dear. Please stop waving that around, someone could get hurt.

    """,
    key_item_dialogue = open("debugging.txt"),#open("emma_key_item_dialogue.txt"),
    key_item_outcome = "Unlock"

)

Doctor_Innocente = Character(
    name = "Vincent Innocent",
    description = "In the room, you see a fidgeting man in a lab coat and a stethoscope around his neck\n \n",
    dialogue= Menu(
        "The man figdets fidgetingly. \n What do you say?" , [
        ("Who are you", "Uh... I'm the doc"),
        ("What is your name?","Uh... It's Vincent"),
        ("What is going on?", "Uh... somone died. What a second. It was you who died! No wait, that's wrong..."),
        ("Back", "Back *has* been implemented, so if this message comes up, somethings's gone wrong")]
    ),
    dialogue_opts= [open("emma_dialogue1"), open("emma_dialogue2"), open("emma_dialogue3")],
    n_dialgue_opts = 3,
    key_item= Incrmination_docs,
    key_item_dialogue= """
    Vincent:
    Uh... What's that? It looks like a confession. OH, are YOU confessing?
    """,
    wrong_item_dialogue= """
    Vincent:
    Uh... Why did you show me that?
    """,
    key_item_outcome= "Unlock library"
)

class Room(object):
    def __init__(self, opening, description, character, clues, n_clues, investigation_menu):
        self.opening = opening
        self.character = character
        self.clues = clues
        self.investigation_menu = investigation_menu
        self.description = description
        self.n_clues = n_clues

    locked = False

    def turn_lock(self):
        self.locked = False

    def describe(self):
        slowprint(self.description)

    ###This code still needs cleaning up a little bit, but in the main it works. Pretty cool!
    def investigate(self):
        global Inventory
        print(self.investigation_menu.display())
        investigation_choice = input("> ")
        #yeah, I know, this has too many nested conditionals. But I couldn't come up with a less
        #kludgy way to accomplish the game not crashing if the player doesn't enter an integer.
        if investigation_choice.isnumeric():
            investigation_choice = int(investigation_choice) #it needs to be an integer
            while investigation_choice <= self.n_clues: 
                slowprint(self.clues[investigation_choice-1].description)

                if self.clues[investigation_choice-1].portable == True:
                    Inventory.append(self.clues[investigation_choice-1])
                
                    #remove duplicates from inventory
                    Inventory = [*set(Inventory)]  
                print(self.investigation_menu.display())
                investigation_choice = int(input("> "))
        else:
            print("Yeah, yeah, you tried to see what happens if you enter not a number. Very clever.")
            input("Return to main menu")
            
            



Library_opening = Room(
    opening= open("debugging.txt"), #open("library_opening.txt"),
    description = open("library_description.txt"),
    character= Emma_Atalle,
    clues = [Knife, Letter, Book],
    n_clues = 3,
    investigation_menu = Menu(
            "You look around and the following items stand out to you:", [
                ("The knife buried in the body", 1),
                ("The rest of the body",2),
                ("A book sitting loose in the shelf", 3),
                ("Back", 4)
            ]
        )
)

Library = Room(
    opening= "\n \nYou return to library. The dead body is still.\n\nNow the door is unlocked... because you unlocked it.\n \n",
    description = "\nThe library has many books. \n",
    character= Emma_Atalle,
    clues = [Library_book],
    n_clues= 1,
    investigation_menu = Menu(
            "You look around and the following items stand out to you:", [
                ("A book sitting loose in the shelf", 2),
                ("Back", 3)
            ]
        )
)


Parlor = Room(
    opening= "\n \nThis is the parlor?\n \n",
    description = "\nI don't actually know what a parlor is, but parlorlike things abound, I assume \n",
    character= Doctor_Innocente,
    clues = [Incrmination_docs],
    n_clues = 1,
    investigation_menu = Menu(
            "You look around and the following items stand out to you:", [
                ("A suspicious-looking document sitting on a shelf", 2),
                ("Back", 3)
            ]
        )
)

class Engine(object):

    def __init__(self, room):
        self.room = room
    


    #Allows player to choose a new room and move into it. Prints the opening description of that room
    #make a for loop to populate this dict with available rooms.
    def move(self):
        print("Choose a room:\n1. Library \n2. Parlor")
        rooms = {
            1: Library,
            2: Parlor
        }
        room_choice = int(input("> "))
        self.room = rooms.get(room_choice)
        print(self.room.opening + self.room.character.description)

    def check_inventory(self):
        print("\nThe following items are in your inventory:")
        if Inventory == []:
            print("\nWhat a second. There's *nothing* in your inventory!")
        else:
            for item in Inventory:
                print(item.name)
    
    def get_outcomes(self, input):
        outcomes = {
            "Unlock library": self.room.turn_lock(),
            "Other": self.move
            }

        return outcomes.get(input)

    def present(self):
        print("What would you like to present?:")
        #Show all the items the player has picked up
        if Inventory == []:
            print("\nWt a second. There's *nothing* in your inventory!")

        #Number all the options
        else:
            for item in range(len(Inventory)):
                print(f"{item + 1} " + Inventory[item].name) #add a number to options presented to player
            item_choice = (input("> "))

            if item_choice.isnumeric():
                if Inventory[int(item_choice) - 1] == self.room.character.key_item:
                    slowprint(self.room.character.key_item_dialogue)
                    self.get_outcomes(self.room.character.key_item_outcome)
                else:
                    print(self.room.character.wrong_item_dialogue)

            else: 
                print("You still have to enter a number. The game won't continue until you do. Believe me, I'm a computer, I can wait all day.")
                input("")
    
    def quit(self):
        exit(1)

    def checklock(self):
        print(self.room.locked)
    

    main_menu = Menu(
        "What do you want to do?" , [
        ("Look around", 1),
        ("Talk", 2),
        ("Move", 3),
        ("Check inventory", 4),
        ("Investigate", 5),
        ("Present", 6),
        ("Quit", 8)]
    )

    main_menu_locked = Menu(
        "What do you want to do?" , [
        ("Look around", 1),
        ("Talk", 2),
        ("Check inventory", 4),
        ("Investigate", 5),
        ("Present", 6),
        ("Quit", 8)]
    )

#for some reason, have to make this a function. I don't understand why,
#but I couldn't get it to work otherwise.
#I also have no idea why putting the parentheses
#where I've put them works, but clearly it works, and not doing it like this doesn't work.

    def getoptions(self,choice):
        if self.room.locked:
            options = [
                self.room.describe,
                self.room.character.talk,
                self.check_inventory,
                self.room.investigate,
                self.present,
                self.quit,
            ]
        else: 
             options = [
                self.room.describe,
                self.room.character.talk,
                self.move,
                self.check_inventory,
                self.room.investigate,
                self.present,
                self.quit
            ]
        return options[choice - 1]()


    #Describe the current room
    def play(self):
        self.room.locked = TRUE
        slowprint(self.room.opening)

        print(self.room.opening.read())
        while True:
            if self.room.locked:
                print(self.main_menu_locked.display())
            else:
                print(self.main_menu.display())

            choice = input("> ")
            if choice.isnumeric():
                self.getoptions(int(choice))
            else:
                print("Come on. No funny business. Just enter a number.")
                input("")


# class Information(Clue):
#    pass

class RoomMap(object):
    rooms = {
        "Library": Library
    }

    def __init__(self, first_room):
        self.first_room = first_room

    def next_room(self, room_name):
        val = RoomMap.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.first_room)



game = Engine(Library_opening)
game.play()
