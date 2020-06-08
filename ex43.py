# Basic Object_Oriented Analysis and Design

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    pass


class Death(Scene):
    predeath = """
    You just can not answer it
    You can not take this anymore
    You just feel like
    """

    quips = [
    'You are just not worthy...\nand suddenly you hear \n"Only death can save you from your unworthiness"\n(You decide to end you life)',
    'You do not have enough intelligence...\nand suddenly you hear \n"Only death can save you from your foolishness.\n(You decide to end you life)',
    'Your mind goes crazy...\nand suddenly you hear \n"Only death can save you from your madness."\n(You decide to end you life)',
    'You just cannot do it by yourself...\nand suddenly you hear \n"Only death can save you from your loneliness."\n(You decide to end you life)'
    ]

    def enter(self):
        print(self.predeath,self.quips[randint(0,len(self.quips)-1)], "\n\nGAME OVER")
        exit(1)

class FirstFloor(Scene):
    def enter(self):
        print(dedent('''
        You wake up, you don't remember what happened to you, and where are
        you right now, but for unknown reason, you have a dagger on your right
        hand. You try to remember anything, but nothing come out of your mind,
        after a while, you get the grasp of yourself and start to look around...
        it is a wide room with all white features, and there, a door, golden door
        with no handle... suddenly, "Welcome mortal, you came here to fulfill your
        most desire, but you have to climb to the top of this tower to get what
        you desire the most, so, first, you have to answer all of my question, mortal...
        what is the only certainty in the world? "\n
        '''))

        guesses = 0

        while True :
            answer = input("Your answer mortal? ")
            guesses += 1
            if answer == "uncertainty":
                print('''
                "You answered well, mortal...
                you may ascend... "
                the golden door open
                you move through it
                and see a staircase upwards...
                ''')
                return 'second_floor'
            elif guesses == 3:
                return 'death'
            else:
                pass

class SecondFloor(Scene) :
    def enter(self):
        print(dedent("""
        You arrive on the second floor, you realize that it is nothing different
        than the first one, except now, the door is made out of silver.........
        you presume... You shout "Hey tower, what is your next question!!?" that
        mysterious voice appears again "Welcome to the second floor mortal, the
        question is...
        Every mortals wants more of it to feel special, yet the more they have of
        it the less special they feel, what is it?
        """))

        guesses = 0

        while True :
            answer = input("Your answer mortal? ")
            guesses += 1
            if answer == "knowledge":
                print('''
                "You answered well, mortal...
                you may ascend... "
                the silver door open
                you move through it
                and see a staircase upwards...
                ''')
                return 'third_floor'
            elif guesses == 3:
                return 'death'
            else:
                pass

class ThirdFloor(Scene) :
    def enter(self):
        print(dedent("""
        Your patience is getting thinner, you just want to get out of here as soon
        as possible, after you reach the third floor,you do not bother to look
        around, and immediately say "just give me the question!!", "Welcome to..",
        "Save your sorry ass greeting, I already have enough", but the voice still
        continue with its greeting "... mortal, the question is... If you have me,
        you want to share me. If you share me, you haven’t got me. What am I?"
        """))

        guesses = 0

        while True :
            answer = input("Your answer mortal? ")
            guesses += 1
            if answer == "secret":
                print('''
                "You answered well, mortal...
                you may ascend... "
                the bronze door open
                you move through it
                and see a staircase upwards...
                ''')
                return 'final_floor'
            elif guesses == 3:
                return 'death'
            else:
                pass

class FinalFloor(Scene) :
    def enter(self):
        print(dedent("""
        With a realization that if you interupting the voice nothing
        will change, so, you decide to remain silent until you have to
        answer... and after you set your foot on the next floor, you notice
        there is no door whatsoever... "is it the top of the tower?"
        you talk to yourself, and that strange voice come out of no where
        "Welcome to the final floor, mortal, you have done well... the question is...
        I can be cracked, I can be made. I can be told, and I can be played…
        What am I?"
        """))

        guesses = 0

        while True :
            answer = input("Your answer mortal? ")
            guesses += 1
            if answer == "joke":
                print('''
                "You answered well, mortal...
                you are right, this is all
                just a 'joke', i am just toying
                with you by building this tower
                and putting you in it, solely for
                my own amusement...
                but be not sullen mortal, i will
                free you from your suffering and
                give what you really desire,
                'PEACE'.....

                WHAHAHAHAHAHA!!!! "

                without realizing, you already stab yourself...
                as confused as you are, your sight started
                to darken, and you can barely hear a laugh cracking
                on the air.... now your vision completely pitch
                black and you ..............................

                GAME OVER

                ''')

                exit(1)

            elif guesses == 3:
                return 'death'
            else:
                pass

class Engine(object):

    # make a variable from an argument inserted in the class Engine
    # which is an object created from the class Map
    def __init__ (self,scene_map):
        self.scene_map = scene_map

    # defining 2 variables using function from class Map
    # current_scene is the scene that will be played
    # last_scene is the last scene that will be used as a comperation
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('final_floor')

        # this loop is for moving from one scene to another
        while current_scene != last_scene:
            # this variable will display the content of current_scene
            # and input a value to the next_scene_name from what
            # the current_scene.enter() will return
            next_scene_name = current_scene.enter()
            # after getting a return value from the enter(), it then go back into the class Map and running next_scene function with an argument from the next_scene value
            # and it will loop until the current_scene is the same with the last_scene
            current_scene = self.scene_map.next_scene(next_scene_name)

        # this enter() function is a fuction to display the last_scene because the while loop earlier is already break
        current_scene.enter()

class Map(object):
    # this is the dict of the necessary key to call a value which is a class Scene to be called in the class Engine
    scenes = {
    'first_floor' : FirstFloor(),
    'second_floor' : SecondFloor(),
    'third_floor' : ThirdFloor(),
    'final_floor' : FinalFloor(),
    'death' : Death(),
    }

    # this is the initiate value that will decide which scene will be the first scene
    def __init__ (self,start_scene):
        self.start_scene = start_scene

    # this is the function to get a value from the dict earlier and will return its value
    def next_scene (self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # this function is solely just for returning the first scene so that the current_scene in the class Engine will have a iniate value/objct of class Map
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('first_floor')
a_game = Engine(a_map)
a_game.play()

'''
class Spam(object):
    def __init__(self, something):
         self.something = something
    def spam(self):
         something.hiYa()

class Hello(object):
    def hiYa(self):
         print("Hello")

something = Hello()
sillyness = Spam(something)
sillyness.spam()
'''
