class Enemy:
    def __init__(self, name, hp, defense, attack, mana, speed):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.mana = mana
        self.speed = speed

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        print(f"{self.name} took {actual_damage} damage! Remaining HP: {self.hp}")

    def attack_enemy(self,other):
        print(f"{self.name} attacks {other.name}!")
        other.take_damage(self.attack)
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return (f"{self.name} Stats:\n"
                f"HP: {self.hp}\n"
                f"DEF: {self.defense}\n"
                f"ATK: {self.attack}\n"
                f"MANA: {self.mana}\n"
                f"SPD: {self.speed}")
