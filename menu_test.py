from collections import namedtuple


game_runs = True

Option = namedtuple("Option", ["label", "callback"])


class Menu:

    SEPARATOR = '-'

    title = ''
    options = []

    def __init__(self, title, options):
        self.title = title

        #Set the options to whatever the nemu is meant to contain
        for option in options:
            self.options.append(Option(option[0], option[1]))

    #Make a separated header
    def header(self, text):
        line = self.SEPARATOR * (len(text) + 2)
        return f"{line}\n {text}\n{line}\n"

    #Display the options
    def display(self):
        string = self.header(self.title)

        for i, option in enumerate(self.options):
            string += f"{i + 1} {option.label}\n"

        return string
    #Return the user's choice
    def callback(self, choice):
        if choice <= len(self.options):
            return self.options[choice - 1].callback

def inv():
    print("investigate")

main_menu = Menu(
    "What do you want to do?", [
    ("Investigate", "Oh look"),
    ("Talk", "hey"),
    ("Move", "distance"),
    ("Present", "oh nice")]
)

print(main_menu.display())

choice = int(input("> "))
main_menu.callback(choice)()
