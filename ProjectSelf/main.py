from basics.battle import *
from basics.character import *
from basics.enemy import *
if __name__ == "__main__":
    hero = Character("Player")
    hero.starting_gear()
    hero.show_stats()
    goblin = Enemy("Goblin", hp=8, defense=2, attack=10, mana=0, speed=12)
    orc = Enemy("Orc", hp=16, defense=3, attack=12, mana=3, speed=8)
    ent = Enemy("Ent", hp = 20, defense = 4, attack = 8, mana=0, speed = 6)
    print(goblin.__str__())
    print(orc.__str__())
    print(ent.__str__())
    test = Battle(hero, [goblin, orc, ent])
    test.start_battle()


