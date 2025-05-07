import random
from things.weaponsandarmor import *
class Character:
    
    name = ""
    hp = 0
    acthp = 0
    defense = 0
    atk = 0
    mana = 0
    spd = 0
    equipment = {}
    bag = []
    thp = 0
    tdefense = 0
    tatk = 0
    tmana = 0
    tspd = 0

    def __init__(self,name):
        self.name = name
        self.hp = random.randrange(1,11)
        self.defense = random.randrange(1,11)
        self.atk = random.randrange(1,11)
        self.mana = random.randrange(1,11)
        self.spd = random.randrange(1,11)
        self.equipment = {"weapon":None,"armor":None,"necklace":None}
        self.bag = []
        self.thp = 0
        self.tdefense = 0
        self.tatk = 0
        self.tmana = 0
        self.tspd = 0
        self.acthp = 0
        self.speed = 0
    # Helpful functions
    def calcHp(self):
        self.acthp = self.hp + self.thp
    def calcSpd(self):
        self.speed = self.spd + self.tspd
    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"  HP: {self.hp} + {self.thp}")
        print(f"  Mana: {self.mana} + {self.tmana}")
        print(f"  Attack: {self.atk} + {self.tatk}")
        print(f"  Defense: {self.defense} + {self.tdefense}")
        print(f"  Speed: {self.spd} + {self.tspd}")
    # Get Functions
    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getDef(self):
        return self.defense

    def getAtk(self):
        return self.atk
    
    def getMana(self):
        return self.mana

    def getSpd(self):
        return self.spd
    # Set Functions
    def setName(self,name):
        self.name = name
        return 
    
    def setHp(self,hp):
        self.hp = hp
        return 
    
    def setDef(self,defense):
        self.defense = defense
        return 
    
    def setAtk(self,atk):
        self.atk =  atk
        return 
        
    def setMana(self,mana):
        self.mana = mana
        return 
    
    def setSpd(self,spd):
        self.spd = spd
        return 
    # Bag functions
    def add_item(self,itm):
        self.bag.append(itm)
        return
    def remove_item(self,itm):
        self.bag.remove(itm)
        return
    def show_items(self):
        for x in self.bag:
            print(x)
    
    # Equipment Functions
    def set_weapon(self,w):
        if self.equipment["weapon"] == None:
            self.equipment["weapon"] = w
            self.bag.remove(w)
        else:
            self.bag.append(self.equipment["weapon"])
            self.equipment["weapon"] = w
            self.bag.remove(w)
        return
    def set_armor(self,a):
        if self.equipment["armor"] == None:
            self.equipment["armor"] = a
            self.bag.remove(a)
        else:
            self.bag.append(self.equipment["armor"])
            self.equipment["armor"] = a
            self.bag.remove(a)
        return
        
    def set_necklace(self,n):
        if self.equipment["necklace"] == None:
            self.equipment["necklace"] = n
            self.bag.remove(n)
        else:
            self.bag.append(self.equipment["necklace"])
            self.equipment["necklace"] = n
            self.bag.remove(n)
        return
    
    def set_temps(self):
        self.thp = getArmorHp(self.equipment["armor"]) + getNecklaceHp(self.equipment["necklace"])
        self.tatk = getWeaponAtk(self.equipment["weapon"]) + getNecklaceAtk(self.equipment["necklace"])
        self.tdefense = getArmorDef(self.equipment["armor"]) + getNecklaceDef(self.equipment["necklace"])
        self.tmana = getNecklaceMana(self.equipment["necklace"]) + getWeaponMana(self.equipment["weapon"])
        self.tspd = getArmorSpd(self.equipment["armor"]) + getWeaponSpd(self.equipment["weapon"])
    
    # Battle Functions
    def attack_enemy(self,other):
        print(f"{self.name} attacks {other.name}!")
        other.take_damage(self.atk + self.tatk)
        
    def take_damage(self, damage):
        actual_damage = max(0, damage - (self.defense + self.tdefense))
        self.acthp = max(0, self.acthp - actual_damage)
        print(f"{self.name} took {actual_damage} damage! Remaining HP: {self.hp}")
        
    def is_alive(self):
        return self.acthp > 0
    # Start Functions
    def starting_gear(self):
        self.equipment["armor"] = "Leather"
        self.equipment["necklace"] = "Nature Necklace"
        print("\nChoose your Weapon:")
        print("1: Sword or 2: Staff")

        while True:
            try:
                choice = int(input("Enter target number: "))
                if choice == 1:
                    self.equipment["weapon"] = "Wood Sword"
                    self.set_temps()
                    self.calcHp()
                    self.calcSpd()
                    return
                elif choice == 2:
                    self.equipment["weapon"] = "Wood Staff"
                    self.set_temps()
                    self.calcHp()
                    self.calcSpd()
                    return
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        