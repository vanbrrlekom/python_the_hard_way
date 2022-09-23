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


    def play(self):
        choice = int(input("> "))
        print(self.getoptions(choice))

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
    description = "Also in the room stands a tall, bored-looking woman. Has she seen the body?",
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
    opening= "You are in the library. There is a dead body here.\n The door is locked.  How did this happen?\n \n",
    description = "The library has many books. \n",
    character= Emma_Atalle,
    clues = "Clues in the room",
)

Library.character.talk()







test = Engine(Library)
test.play()
