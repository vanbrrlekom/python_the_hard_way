from sys import exit
from random import randint
from textwrap import dedent



class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)
        

class Engine(object):
    def __init__(self, scene_map): ## load the game, select a map, entered by user
        self.scene_map = scene_map # from self, load the scene map attribute and set it to scene map

    def play(self):
        current_scene = self.scene_map.opening_scene() #set current scene to opening scene, contained in scene map
        last_scene = self.scene_map.next_scene("finished") #set the last scene to the finished scene from scene map

        while current_scene != last_scene: #now this piece of code. Do the following for all but the last scenees
            next_scene_name = current_scene.enter() #This is going to set the valueof the next scene name to
            #whichever value is determine by the enter function in the current scene. And each scene has
            #an enter function which returns a value. 

            current_scene = self.scene_map.next_scene(next_scene_name) #okay, but what does this do? well,
            # self, is a_game, it calls the scene map, from the scene map, calls the next_scene function,
            # which takes self and the name of a scene as arguments to play, well, the next scene. 

            #be sure to print out the last scene
            current_scene.enter()

class Death(Scene):
    #starts by creating a list of quips

    quips = [
        "You died. But you also tried!",
        "Whoah, I'm not going to do a mom joke. Way harsh zed! But you, player, are dead",
        "You're a winner at heart! But you did lose the game",
        "Puppies are cute! But you did lose",
        "Nice dad jokes! But also, you're dead. Sorry."
    ]

    # randomly select one of the quips to print
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            Imagine I'm describing a gruesome scene where aliens have invaded 
            your ship. Oh no! You have to get to the weapons armory, geth the bomb, 
            put it in the bridge and destroy the ship after
            getting into an escape.
            
            Oh no, there's an alien! he's trying ot shoot!
            """))

        action = input("> ")

        if "shoot" in action:
            print(dedent(""" 
                You shoot, but it doesn't go well. He eats you"""))
            return "death"

        elif "dodge" in action: 
            print(dedent("""
                You doge, but it doesn't go well. 
                He eats you
                """))
            return "death"
        
        elif action == "tell a joke":
            print(dedent("""
                Wow, that worked!
                I can't believe that worked!
                You head for the Weapon armory.
                """))
            return "laser_weapon_armory"

        else: print("WHOAHHH. That prompt is on another dimension. Try again")
        return "central_corridor"

            

class TheBridge(Scene):
    
    def enter(self):
        print(dedent("""
            The bridge has more aliens! 
            What do you do what do you do
            what do you do what do you do?"""))
        
        action = input("> ")
        exit(1)

class EscapePod(Scene):
    
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print(dedent("""
            this is the armory!
            Where do you search for the guns? You have to enter a random code here. Okay!"""))
        code = f"{randint(1,9)}, {randint(1,9)}, {randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses <9:
            print("Uh oh! Wrong code!")
            guesses += 1
            guess = input("[keypad]> ")
        
        if guess == code: 
            print("Ya nailed it. Ya grab teh bomb and head for the bridge.")
            return "The_Bridge"
        
        else:
            print("You failed this comletely reasonable puzzle. The ship blows up and you die")
            return "death"

class Finished(Scene):
    def enter(self):
        pass

class Map(object):

    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "The_Bridge": TheBridge(),
        "Escape_pod": EscapePod(),
        "death": Death(),
        "finished": Finished()

    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map("central_corridor") #creates an instance of the map with the starting map being "central corridor"
a_game= Engine(a_map) #creates an instance of the game using that map, set to starting point
a_game.play()
