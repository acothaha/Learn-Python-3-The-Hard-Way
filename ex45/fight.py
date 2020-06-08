from suit import suit


def fight(hero, foe, death):

    if foe.hp <= 0:
        print(f"\n\t\t\tYOU DEFEAT {foe.name}")
        return 1

    elif hero.hp <= 0:
        death.enter()
        exit(1)

    else:
        pass

    print(f"\n\t\t\t{hero.name}: {hero.hp} HP VS {foe.hp} HP :{foe.name}\n")
    battle = suit()

    if battle == "lose":
        hero.hp = hero.hp - foe.atk
        fight(hero, foe, death)

    elif battle == "win":
        foe.hp = foe.hp - hero.atk
        fight(hero, foe, death)

    else:
        print("something wrong")
