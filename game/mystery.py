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

#ambient items
mean_tweets = Item(
    name = "A printout of some mean tweets",
    description= open("docs/debugging.txt"),
    portable = True
)

#Library items
Knife = Item(
    name = "Bloody knife", 
    description =  open("docs/debugging.txt"),#"A bloody knife. There's an inscription on the hilt. You take take a closer look. The inscryption is... your initials. How strange. Eh, probably it probably doesn't mean anything. You pick it up, you freak.",
    portable= True)
Letter = Item(
    name = "Pocket letter",
    description= open("docs/pocket_letter_description.txt"),
    portable = True)
key = Item(
    name = "Library key",
    description= open("docs/debugging.txt"),
    portable = True
)
ampule = Item(
    name= "Glass amuple",
    description= open("docs/debugging.txt"),
    portable = True
)
fireplace = Item(
    name= "fireplace",
    description= open("docs/debugging.txt"),
    portable = True
)
Book = Item(
    name = "A boring book", 
    description = open("docs/debugging.txt"),
    portable = True)
brochure = Item(
    name = "Castle brochure",
    description= open("docs/brochure.txt"),
    portable = True
)

#Parlor items
Incrmination_docs = Item(
    name = "Incriminating documents", 
    description = "It's a piece of paper. The text says \"it was me i did it\". The signature is... your signature.",
    portable= True)
Library_book = Item(
    name = "A fun book", 
    description= "this book is way more fun",
    portable = True)
building_permits = Item(
    name = "Some boring looking documents",
    description= open("docs/debugging.txt"),
    portable = True
)

#Orangery Items
leftovers = Item(
    name = "A half-eaten plate",
    description= open("docs/debugging.txt"),
    portable= True
)

glass_ceiling = Item(
    name = "The clear glass ceiling",
    description= open("docs/debugging.txt"),
    portable= True
)

#Cellar items
drink = Item(
    name = "A bottle of alcohol",
    description= open("docs/debugging.txt"),
    portable= TRUE
)

# When implementing dialogue, it's important to make it in then
# format Menu("title", ["question", "answer"], ["back", "placeholder"])
class Character(object):
    def __init__(
            self, name, description, dialogue, dialogue_opts, n_dialgue_opts, key_item, 
            key_item_dialogue, wrong_item_dialogue, key_item_outcome, disaster_dialogue
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
        self.disaster_dialogue = disaster_dialogue


    def talk(self):
        print(self.dialogue.display())
        choice = input("> ")
        if choice.isnumeric():
            while choice < len(self.dialogue_opts)+1:
                choice = int(choice)
                slowprint(self.dialogue_opts[choice -1])
                print(self.dialogue.display())
                choice = int(input("> "))
        else:
            print("Come on wiseguy. You know the drill. It's numbers. That's what I want to see. None of this \"not numbers\" business")
            input("Return to main menu.")
        
    
            

Emma_Atalle = Character(
    name = "Emma Atalle",
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?\n \n",
    dialogue= Menu(
        "The woman eyes you very suspicously. You get the sense that maybe she suspects you of something. \n What do you talk about?" , [
        ("Don't move?", "None of your business"),
        ("The victim.","Never ask the name a lady her name"),
        ("This place.", "You tell me, you're the mureder"),
        ("Back", "Back *has* been implemented, so if this message comes up, somethings's gone wrong")]
    ),
    dialogue_opts= [open("docs/emma_dialogue1.txt"), open("docs/emma_dialogue2.txt"), open("docs/emma_dialogue3.txt")],
    n_dialgue_opts = 4,
    key_item = Letter,
    wrong_item_dialogue = open("docs/emma_wrong_item_dialogue.txt"),
    key_item_dialogue = open("docs/emma_key_item_dialogue.txt"),#open("docs/debugging.txt"),
    key_item_outcome = "Unlock",
    disaster_dialogue= open("docs/debugging.txt")
)

Emma_Atalle_2 = Character(
    name = "Emma Atalle",
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?\n \n",
    dialogue= Menu(
        "The woman eyes you very suspicously. You get the sense that maybe she suspects you of something. \n What do you talk about?" , [
        ("Don't move?", "None of your business"),
        ("The victim.","Never ask the name a lady her name"),
        ("This place.", "You tell me, you're the mureder"),
        ("Back", "Back *has* been implemented, so if this message comes up, somethings's gone wrong")]
    ),
    dialogue_opts= [open("docs/emma_dialogue1.txt"), open("docs/emma_dialogue2.txt"), open("docs/emma_dialogue3.txt")],
    n_dialgue_opts = 3,
    key_item = Letter,
    wrong_item_dialogue = "EMMA: Oh dear. Please stop waving that around, someone could get hurt.",
    key_item_dialogue = open("docs/debugging.txt"),#open("emma_key_item_dialogue.txt"),
    key_item_outcome = "Unlock",
    disaster_dialogue= open("docs/debugging.txt")

)

Doctor_Innocente = Character(
    name = "Alma Innocent",
    description = "In the room, you see a fidgeting man in a lab coat and a stethoscope around his neck\n \n",
    dialogue= Menu(
        "What do you talk about?" , [
        ("The victim", 1),
        ("Last night?","Uh... It's Vincent"),
        ("Suspitions", "Uh... somone died. What a second. It was you who died! No wait, that's wrong..."),
        ("Back", "Back *has* been implemented, so if this message comes up, somethings's gone wrong")]
    ),
    dialogue_opts= [open("docs/alma_dialogue1.txt"), open("docs/alma_dialogue2.txt"), open("docs/alma_dialogue3.txt")],
    n_dialgue_opts = 3,
    key_item= Incrmination_docs,
    key_item_dialogue= open("docs/debugging.txt"),
    wrong_item_dialogue= "ALMA: What a lovely little object. What do you want me to do with it?",
    key_item_outcome= "Unlock library",
    disaster_dialogue= open("docs/debugging.txt")
)

Brothers_Mook = Character(
    name = "The Brothers Mook",
    dialogue= Menu("The brothers give you a withering stare. You consider carefully which topic to bring up.", [
        ("Apology", 1),
        ("Last night", 2),
        ("Link to the victim", 3),
        ("Back", 4)
    ]),
    dialogue_opts= [open("docs/mook_dialogue1.txt"), open("docs/mook_dialogue2.txt"), open("docs/mook_dialogue3.txt")],
    n_dialgue_opts= 3,
    description = "I suspect that this is redundant now",
    key_item = building_permits,
    key_item_dialogue = open("docs/debugging.txt"),
    wrong_item_dialogue = "Placeholder: The brothers glance contemptuously at the thing you've showed them.",
    key_item_outcome= "Don't know yet",
    disaster_dialogue= open("docs/debugging.txt")
)

Omar = Character(
    name= "Omar",
    description= open("docs/debugging.txt"),
    dialogue = Menu("Placeholder", [("docs/debugging.txt", 1)]),
    dialogue_opts= [open("docs/debugging.txt")],
    n_dialgue_opts= 1,
    key_item= mean_tweets,
    wrong_item_dialogue= "Placeholder",
    key_item_dialogue= open("docs/debugging.txt"),
    disaster_dialogue= open("docs/debugging.txt"),
    key_item_outcome= "Unlock"
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
    opening=  open("docs/library_opening.txt"),#open("docs/debugging.txt"),
    description = open("docs/library_description.txt"),
    character= Emma_Atalle,
    clues = [Knife, Letter, Book, brochure, fireplace],
    n_clues = 5,
    investigation_menu = Menu(
            "You look around and the following items stand out to you:", [
                ("The knife buried in the body", 1),
                ("The rest of the body",2),
                ("A book sitting loose in the shelf", 3),
                ("The fireplace"),
                ("Some sort of brochure on the fireplace mantle"),
                ("Back", 4)
            ]
        )
)

Library = Room(
    opening= "\n \nYou return to library. The dead body is still.\n\nNow the door is unlocked... because you unlocked it.\n \n",
    description = "\nThe library has many books. \n",
    character= Emma_Atalle,
    clues = [Library_book, Knife, Letter, Book, brochure],
    n_clues= 1,
    investigation_menu = Menu(
            "You look around and the following items stand out to you:", [
                ("A book sitting loose in the shelf", 2),
                ("Back", 3)
            ]
        )
)


Parlor = Room(
    opening= open("docs/parlor_opening.txt"),
    description =open("docs/parlor_description.txt"),
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

Orangery = Room(
    opening = open("docs/orangery_opening.txt"),
    description= open("docs/orangery_description.txt"),
    character= Brothers_Mook,
    clues = [glass_ceiling, leftovers],
    n_clues= 2,
    investigation_menu= Menu(
        "Withering the suspicious glares of the brothers Mook, you try to discretely investigate the orangery", [
            ("The glass ceiling", 1),
            ("A plate of leftovers", 2)
        ]
    )
)

Cellar = Room(
    opening = open("docs/debugging.txt"),
    description= open("docs/debugging.txt"),
    character= Omar,
    clues = []

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
            2: Parlor,
            3: Orangery,
            4: Cellar
        }
        room_choice = int(input("> "))
        self.room = rooms.get(room_choice)
        slowprint(self.room.opening)

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

        disaster_opts = [Incrmination_docs]
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

                elif Inventory[int(item_choice) - 1] in disaster_opts:
                    slowprint(self.room.character.disaster_dialogue)
                    self.quit()

                else:
                    slowprint(self.room.character.wrong_item_dialogue)

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
