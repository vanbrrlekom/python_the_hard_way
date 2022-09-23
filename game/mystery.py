from collections import namedtuple
#from dbm.ndbm import library
from logging import PlaceHolder
from sys import exit

Option = namedtuple("Option", ["label", "callback"])
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

class ItemEncyclopedia(object):
    pass

class Item(object):
    def __init__(self, name, description):
        pass


# When implementing dialogue, it's important to make it in then
# format Menu("title", ["question", "answer"], ["back", "placeholder"])
class Character(object):
    def __init__(self, name, description, dialogue):
        self.description = description
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        while True:
            print(self.dialogue.display())
            choice = int(input("> "))
            print(self.dialogue.callback(choice))

Emma_Atalle = Character(
    name = "Emma_Atale",
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?\n \n",
    dialogue= Menu(
        "Emma continues to look at you disinterestedly" , [
        ("Who are you", "None of your business"),
        ("What is your name?","Never ask the name a lady her name"),
        ("What is going on?", "You tell me, you're the mureder"),
        ("Back", "Whelp, feature not implemented, this is going to be an endless loop. Sorry!")]
    )
)


class Room(object):
    def __init__(self, opening, description, character, clues):
        self.opening = opening
        self.character = character
        self.clues = clues
        self.description = description

Library = Room(
    opening= "\n \nYou are in the library. There is a dead body here.\n\nThe door is locked.  How did this happen?\n \n",
    description = "\nThe library has many books. \n",
    character= Emma_Atalle,
    clues = "Clues in the room",
)

class Engine(object):

    def __init__(self, room):
        self.room = room


    main_menu = Menu(
        "What do you want to do?" , [
        ("Investigate", Library.description),
        ("Talk", Library.character.dialogue),
        ("Move", "Moving not yet implemented"),
        ("Present", "Presenting not yet implemented")]
    )

#for some reason, have to make this
    def getoptions(self,choice):

        options = [
            self.room.description,
            self.room.character.talk(),
            "Moving not yet implemented",
            "Presenting not yet implemented"
            ]
        return options[choice - 1]

    #Describe the current room
    def play(self):

        print(self.room.opening + self.room.character.description)
        print(self.main_menu.display())

        choice = int(input("> "))
        print(self.getoptions(choice))


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




game = Engine(Library)
game.play()
