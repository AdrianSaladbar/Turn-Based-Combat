import random
class Battle:
    def __init__(self, solo_fighter, enemy_team):
        self.solo = solo_fighter
        self.enemies = enemy_team
        self.all_combatants = [self.solo] + self.enemies
        self.all_combatants.sort(key=lambda e: e.speed, reverse=True)
        
    def get_player_target_choice(self):
        living_enemies = [e for e in self.enemies if e.is_alive()]
        print("\nChoose your target:")
        for idx, enemy in enumerate(living_enemies):
            print(f"{idx + 1}. {enemy.name} (HP: {enemy.hp})")

        while True:
            try:
                choice = int(input("Enter target number: ")) - 1
                if 0 <= choice < len(living_enemies):
                    return living_enemies[choice]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")

    def start_battle(self):
        print(f"Battle Begins: {self.solo.name} vs {[e.name for e in self.enemies]}\n")
        turn_num = 1
        while self.solo.is_alive() and any(e.is_alive() for e in self.enemies):
            print(f"--- Turn {turn_num} ---")
            for fighter in self.all_combatants:
                if not fighter.is_alive():
                    continue

                if fighter == self.solo:
                    target = self.get_player_target_choice()
                else:
                    target = self.solo if self.solo.is_alive() else None

                if target:
                    fighter.attack_enemy(target)
                    if not target.is_alive():
                        print(f"{target.name} has been defeated!\n")
            turn_num += 1

        print("\nBattle Over")
        if self.solo.is_alive():
            print(f"{self.solo.name} wins!")
        else:
            print(f"{', '.join([e.name for e in self.enemies if e.is_alive()])} win!")


