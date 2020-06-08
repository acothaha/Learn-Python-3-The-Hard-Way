from textwrap import dedent
from fight import fight
import char

class Scene(object):
    pass

class Death(Scene):
    quips = [
        "Your hand gets chopped off.",
        "Your limb gets stabbed.",
        "Your back gets slashed.",
        "Your leg gets cleaved."
        ]

    def enter(self):
        print(dedent(f'''
        Your feel so exhausted... then suddenly you realize, your enemy is
        too close to you and....
        WHACK!!! {self.quips[randint(0,3)]}'''),
        "\n\n\t\t\t GAME  OVER")

class Opening(Scene):
    def enter(self):
        print(dedent(f'''
        your name is {player.name}, you are a {job} in the southern part of
        Nowhere Kingdom, one day, the gang of looters invades your land, takes
        you as a prisoner and sells you to the ransom broker. Unfortunately,
        because of your good build, you are sold to a noble who then makes you
        a gladiator in somekind of colloseum. Now, begin the story of you
        being a slavesword just to satisfy your master's amusement.
        '''
        ))

        return 'stage1'

class Stage1(Scene):
    def enter(self):
        print(dedent(f'''
        Now you are in the Colloseum, you don't have any idea what to expect.
        Suddenly your name is called by someone, turn out, it is the game
        master, he tells you to take some equipment before you enter the arena,
        so you go to the armory, there are not a lot of equipments there, just
        a basic one, so you decide to take a set of light armor and a worn out
        sword...
        Now you are ready for your first fight. You stand in front of the
        gate, and you can hear a glimps of the shouting from the spectators...
        KRAKKK!!! the gate is open...
        you rush into the arena and find your first enemy...
        '''))

        enemy1 = char.Enemy("Puki the Foul",75,10)

        fight1 = fight(player, enemy1, death)

        return 'stage2'

class Stage2(Scene):
    def enter(self):
        print(dedent(f'''
        "That was some fighting you put out there" says the game master, you
        just ignore him and try to tend your wound. Eventhough that fight was
        not that hard, you still have some injury ({player.hp} HP left). After
        a short rest (get to full hp), you gain your energy back, and the game
        master calls you again, he tells you to get ready for the next
        fight... You go to the gate and prepare your body and mind to face the
        next enemy...
        KRAKKK!!! the gate is open...
        this time, you can see clearly what your opponent looks like, he is
        HUGE....
        '''))
        player.hp = char.vit(job)

        enemy2 = char.Enemy("Tobron the Giant",150,15)

        fight2 = fight(player, enemy2, death)

        return 'stage3'

class Stage3(Scene):
    def enter(self):
        print(dedent(f'''
        you didn't anticipate to face that kind of man, and the fact that the
        next opponent will be stronger and fiercer than the last one makes you
        can't calm your mind. While tending your wounds, you can't get rid off
        that concern... as the result, you don't have a proper rest (restore
        25 HP). You are still with your wornout armor and sword, you cannot
        fathom why they didn't give you a new one, but screw them, you just
        have to kill your enemy to stay alive, it's that simple... You already
        stand in front of the gate without the game master saying...
        KRAKKK!!! the gate is open...
        Not like the last time, now your enemy is kinda... too small,
        even he looks like a dwarf, for a moment you feel a relief, but...

        '''))

        if player.hp >= char.vit(job) - 25 and player.hp <= char.vit(job):
            player.hp = char.vit(job)

        else:
            player.hp += 25

        enemy3 = char.Enemy("Palkon the Deadly",100,25)

        fight3 = fight(player, enemy3, death)

        return 'last_stage'


class LastStage(Scene):
    def enter(self):
        print(dedent('''
        You don't care anymore, you don't care wether you will be alive of
        dead after this last fight, your enemy is the renown "Edi the
        Invicible". the chance of you winning, or maybe even living after your
        confrontation with him is slim to none, but there is nothing you can
        do. As a slave you can't do anything really, accept your fate is the
        only choice you have.... and surely they don't give you any time to
        rest, but strangely enough, for this last fight, you
        are given a new pair of equipments, a set of steel armor (+50 HP) and
        a new shining sword (+10 atk) instead. Now you look like a real
        warrior at last... finally the game master calls you, you then go to
        the gate and
        wait patienly until the get open......
        KRAKKK!!! the gate is open...
        you can hear the loud shouting around the arena, but the one thing
        that catches your sense the most is the presence that "Edi the
        Invicible" emmitted, is so great you almost run with your tail between
        your legs, but you can't.....
        '''))

        player.hp += 50
        player.atk += 10

        enemy4 = char.Enemy("Edi the Invicible",200,35)

        fight4 = fight(player, enemy3, death)

        return 'victory'

class Victory(Scene):
    def enter():
        print(dedent('''
        you are now the champion of the colloseum!!!!

        \t\t\t\THE END
        '''))



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
        last_scene = self.scene_map.next_scene('victory')

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
    'opening' : Opening(),
    'stage1' : Stage1(),
    'stage2' : Stage2(),
    'stage3' : Stage3(),
    'last_stage' : LastStage(),
    'victory' : Victory()
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

name = input("what is your name ?\n")
job = input(dedent("""
    what do you do?
    farmer (Higher HP)
    hunter (Higher ATK)
    """))

player = char.Player(name, char.vit(job), char.pow(job))
death = Death()
map = Map('opening')
client = Engine(map)
client.play()
