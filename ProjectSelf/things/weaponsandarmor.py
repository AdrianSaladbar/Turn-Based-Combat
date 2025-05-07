weapons = {
    "Wood Sword": {"atk":4,"mana":0,"spd":0},
    "Wood Staff": {"atk":2,"mana":2,"spd":0}
}
armors = {
    "Leather": {"hp":8,"def":2,"spd":6},
    "Chainmail": {"hp":16,"def":6,"spd":4}
}
necklaces = {
    "Nature Necklace":{"hp":2,"atk":2,"def":0,"mana":2},
    "Gem Necklace":{"hp":6,"atk":4,"def":2,"mana":6}
}
def getWeaponAtk(w):
    return weapons[w]["atk"]
def getWeaponMana(w):
    return weapons[w]["mana"]
def getWeaponSpd(w):
    return weapons[w]["spd"]

def getArmorHp(a):
    return armors[a]["hp"]
def getArmorDef(a):
    return armors[a]["def"]
def getArmorSpd(a):
    return armors[a]["spd"]

def getNecklaceHp(n):
    return necklaces[n]["hp"]
def getNecklaceAtk(n):
    return necklaces[n]["atk"]
def getNecklaceDef(n):
    return necklaces[n]["def"]
def getNecklaceMana(n):
    return necklaces[n]["mana"]