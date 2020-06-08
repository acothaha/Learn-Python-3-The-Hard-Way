class Player(object):
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.pow = 10


player = Player("asping")
print(player.hp)
player.hp = 40
print(player.hp)
