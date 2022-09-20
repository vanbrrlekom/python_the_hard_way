from collections import namedtuple
from dbm.ndbm import library
from logging import PlaceHolder

Option = namedtuple("Option", ["label", "callback"])

class Menu:

    SEPARATOR = '-'

    _title = ''
    _options = []

    def __init__(self, title, options):
        self._title = title

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

    def callback(self, i):
        if i <= len(self._options):
            return self._options[i - 1].callback

class ItemEncyclopedia(object):
    pass

class Item(object):
    def __init__(self, name, description):
        pass



class Character(object):
    def __init__(self, name, description, dialogue):
        self.description = description
        self.name = name
        self.dialogue = dialogue
    
    def talk():
        pass

Emma_Atalle = Character(
    name = "Emma_Atale",
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?",
    dialogue= "She looks at you dismissively. \n\n \tEmma:\n \tHello?")

class Room(object):
    def __init__(self, opening, description, character, clues):
        self.opening = opening
        self.character = character
        self.clues = clues
        self.description = description
    

Library = Room(
    opening= "You are in the library. There is a dead body here.\n The door is locked.  How did this happen?\n \n",
    description = "The library has many books. \n",
    character= Emma_Atalle,
    clues = "Clues in the room",
)

class Engine(object):
    def __init__(self, room, menu):
        self.room = room
        self.main_menu = menu
    

    #Describe the current room
    def play(self):

        print(self.room.description + self.room.character.description)
        print(self.main_menu.display())

        
        choice = int(input("> "))
        print(self.main_menu.callback(choice))


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

main_menu = Menu(
    "What do you want to do?" , [
    ("Investigate", library.room.description),
    ("Talk", library.character.dialogue),
    ("Move", "Moving not yet implemented"),
    ("Present", "Presenting not yet implemented")]
)


game = Engine(Library, main_menu)
game.play()
