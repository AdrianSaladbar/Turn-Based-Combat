from basics.battle import *
from basics.character import *
from basics.enemy import *
if __name__ == "__main__":
    hero = Character("Player")
    hero.starting_gear()
    hero.show_stats()
    goblin = Enemy("Goblin", hp=8, defense=2, attack=5, mana=0, speed=6)
    orc = Enemy("Orc", hp=16, defense=3, attack=8, mana=3, speed=5)
    test = Battle(hero, [goblin, orc])
    test.start_battle()


