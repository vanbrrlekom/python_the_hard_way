from collections import namedtuple
#from dbm.ndbm import library
from logging import PlaceHolder
from sys import exit

Option = namedtuple("Option", ["label", "callback"])
Inventory = []

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
    def __init__(self, name, description):
        self.name = name
        self.description = description


#Some items
Knife = Item(name = "Bloody knife", description = "A bloody knife. There's an inscription on the hilt. You take take a closer look. The inscryption is... your initials. How strange. Eh, probably it probably doesn't mean anything.")
Book = Item(name = "A boring book", description = "Just a boring old book")


# When implementing dialogue, it's important to make it in then
# format Menu("title", ["question", "answer"], ["back", "placeholder"])
class Character(object):
    def __init__(self, name, description, dialogue, n_dialgue_opts):
        self.description = description
        self.name = name
        self.dialogue = dialogue
        self.n_dialgue_opts = n_dialgue_opts + 1


    def talk(self):
        print(self.dialogue.display())
        question = int(input("> "))
        while question < self.n_dialgue_opts:
            print(self.dialogue.callback(question))
            question = int(input("> "))
            



Emma_Atalle = Character(
    name = "Emma Atalle",
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?\n \n",
    dialogue= Menu(
        "The woman very pointedly ignores you. \n What do you say?" , [
        ("Who are you", "None of your business"),
        ("What is your name?","Never ask the name a lady her name"),
        ("What is going on?", "You tell me, you're the mureder"),
        ("Back", "Back *has* been implemented, so if this message comes up, somethings's gone wrong")]
    ),
    n_dialgue_opts = 3
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
    n_dialgue_opts = 3
)

class Room(object):
    def __init__(self, opening, description, character, clues, n_clues):
        self.opening = opening
        self.character = character
        self.clues = clues
        self.description = description
        self.n_clues = n_clues

    def describe(self):
        print(self.description)

    ###This code still needs cleaning up a little bit, but in the main it works. Pretty cool!
    def investigate(self):
        investigation_menu = Menu(
            "You look around and the following items stand out to you:", [
                ("The knife buried in the body", 1),
                ("A book sitting loose in the shelf", 2),
                ("Back", 3)
            ]
        )
        print(investigation_menu.display())
        investigation_choice = int(input("> "))
        while investigation_choice <= self.n_clues: #This is what I was talking about earlier. 5‡‡
            print(self.clues[investigation_choice-1].description)
            Inventory.append(self.clues[investigation_choice-1])
            #remove duplicates from inventory
            Inventory = [*set(Inventory)]  
            investigation_choice = int(input("> "))
            
            



Library_opening = Room(
    opening= "\n \nYou are in the library. There is a dead body here.\n\nThe door is locked.  How did this happen?\n \n",
    description = "\nThe library has many books. \n",
    character= Emma_Atalle,
    clues = [Knife, Book],
    n_clues = 2
)

Library = Room(
    opening= "\n \nYou return to library. The dead body is still.\n\nNow the door is unlocked... because you unlocked it.\n \n",
    description = "\nThe library has many books. \n",
    character= Emma_Atalle,
    clues = "Clues in the room",
    n_clues= 1
)


Parlor = Room(
    opening= "\n \nThis is the parlor?\n \n",
    description = "\nI don't actually know what a parlor is, but parlorlike things I assume \n",
    character= Doctor_Innocente,
    clues = "Clues in the room",
)

class Engine(object):

    def __init__(self, room):
        self.room = room


    #Allows player to choose a new room and move into it. Prints the opening description of that room
    def move(self):
        print("choose a room:\n1. Library \n2. Parlor")
        rooms = {
            1: Library,
            2: Parlor
        }
        room_choice = int(input("> "))
        self.room = rooms.get(room_choice)
        print(self.room.opening + self.room.character.description)


    Inventory : []
    


    def present(self):
        print("presenting not yet implemented")

    main_menu = Menu(
        "What do you want to do?" , [
        ("Look around", 1),
        ("Talk", 2),
        ("Move", 3),
        ("Present", 4),
        ("Investigate", 5)]
    )

#for some reason, have to make this a function. I don't understand why,
#but I couldn't get it to work otherwise.
#I also have no idea why putting the parentheses
#where I've put them works, but clearly it works, and not doing it like this doesn't work.

    def getoptions(self,choice):

        options = [
            self.room.describe,
            self.room.character.talk,
            self.move,
            self.present,
            self.room.investigate
        ]
        return options[choice - 1]()

    #Describe the current room
    def play(self):
        print(self.room.opening + self.room.character.description)
        while True:
            print(self.main_menu.display())

            choice = int(input("> "))
            self.getoptions(choice)


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
