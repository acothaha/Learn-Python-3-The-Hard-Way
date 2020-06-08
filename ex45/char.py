class Char(object):
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk



class Player(Char):
    pass

class Enemy(Char):
    pass

def vit(job):
    if job == "farmer":
        hp =  150
        return hp

    elif job == "hunter":
        hp = 100
        return hp

    else:
        pass

def pow(job):
    if job == "farmer":
        atk = 15
        return atk

    elif job == "hunter":
        atk = 25
        return atk

    else:
        pass
