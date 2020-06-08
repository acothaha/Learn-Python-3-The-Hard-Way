from random import randint
from sys import exit
from time import sleep

def suit():
    dict = {
        "1" : "STRENGTH",
        '2' : "AGILITY",
        '3' : "INTELLIGENT"
        }

    comp = dict[str(randint(1,3))]

    print("Choose your move!!!")
    choose = input("1 for STRENGTH, 2 for AGILITY and 3 for INTELLIGENT : ")

    if choose in ['1', '2', '3']:
        player = dict[choose]
        pass

    elif choose == "surrender":
        exit(1)

    else:
        print("That's not a proper move, so you perform weak ass move.")
        sleep(2)
        print("TAKKK!!! you got punish.")
        return "lose"

    print(f"You use {player} move and your enemy use {comp} move.")

    if comp == player:
        sleep(2)
        print("BRAKK!!!! It's a tie.\n")
        replay = suit()
        return replay

    elif comp == "STRENGTH" and player == "INTELLIGENT":
        sleep(2)
        print("WHACKK!!! you got hit.")
        return "lose"

    elif comp == "AGILITY" and player == "STRENGTH":
        sleep(2)
        print("BUAAKK!!! you got counter.")
        return "lose"

    elif comp == "INTELLIGENT" and player == "AGILITY":
        sleep(2)
        print("BRACKKK!! you hit the wall.")
        return "lose"

    else:
        sleep(2)
        print("POWWW!!! you hit your enemy.")
        return "win"
