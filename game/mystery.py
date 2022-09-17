from collections import namedtuple
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

class item_encyclopedia(object):
    pass

class Item(object):
    def __init__(self, name, description):
        pass


class Room(object):
    def __init__(self, opening, description, character, clues):
        self.opening = opening
        self.character = character
        self.clues = clues
        self.description = description
    

Library = Room(
    opening= "You are in the library. The library has not been described yet.\n \n",
    description = "The library has many books",
    character= "Characters in the room",
    clues = "Clues in the room",
)

class Engine(object):
    def __init__(self, start, menu):
        self.start = start
        self.main_menu = menu
    
    #Describe the current room
    def play(self):

        print(self.start.description)
        print(self.main_menu.display())

        
        choice = int(input("> "))
        print(self.main_menu.callback(choice))


    

class Character(object):
    pass


#class Information(Clue):
   # pass

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
    ("Investigate", Library.description),
    ("Talk", "Talking not yet implemented"),
    ("Move", "Moving not yet implemented"),
    ("Present", "Presenting not yet implemented")]
)


game = Engine(Library, main_menu)
game.play()
