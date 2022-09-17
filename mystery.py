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

main_menu = Menu(
    "What do you want to do?", [
    ("Investigate", "Oh look"),
    ("Talk", "hey"),
    ("Move", "distance"),
    ("Present", "oh nice")]
)

class item_encyclopedia(object):

class Item(object):
    def __init__(self, name, description)


class Room(object):
    def __init__(self, description, character, clues):
        self.character = None
        self.clues = None
        self.description = None

Library = Room(
    description= "This is a placeholder description of the library"
)

class Engine(object):

class Engine(object):
    def __init__(self, current_room, room_map, character_list, main_menu):
        self.current_room = Library
        self.room_map = room_map
        self.character_list = character_list
        self.main_menu = Menu(
            "What do you want to do?", [
             ("Investigate", investigate()),
             ("Move", move()),
             ("Present", present())])

    def play(self):

        print(self.current_room.description)
        print(self.main_menu.display)

        while True:
            choice = int(input("> "))
            self.main_menu.callback(choice)


        current_room = self.room_map.opening_rom()
        ending = self.room_map.next_room("The end")

        while current_room != ending:
            next_room_name = current_room.enter()

            current_room = self.room_map.next_room(next_room_name)
            current_room.enter()



    def play(self):
        print()
        current_room = self.room_map.opening_rom()
        ending = self.room_map.next_room("The end")

        while current_room != ending:
            next_room_name = current_room.enter()

            current_room = self.room_map.next_room(next_room_name)
            current_room.enter()


class Character(object):
    pass


class Information(Clue):
    pass

class Room_map(object):
    rooms = {
        "Room1": room1(),
        "Room2": room2(),
        "Room3": room3()
    }

    def __init__(self, first_room):
        self.first_room = first_room
    
    def next_room(self, room_name):
        val = Room_map.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.first_room)

