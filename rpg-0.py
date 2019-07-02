"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character():
    def __init__(self, name, health, power,alive):
        self.name = name
        self.health = health
        self.power = power
    def alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, name, health, power, alive):
            super().__init__(name, health, power, alive)

    def attack(self):
        goblin1.health -= hero1.power
        print("You do %d damage to the goblin." % hero1.power)
        if goblin1.health <= 0:
            print("The goblin is dead.")
    
    def print_status(self):
        print("You have %d health and %d power." % (hero1.health, hero1.power))
        if hero1.health <= 0:
                print("You are dead.")
        else:
            print("You are alive!")


class Goblin(Character):
    def __init__(self, name, health, power, alive):
            super().__init__(name, health, power, alive)

    def attack(self):
        hero1.health -= goblin1.power
        print("The goblin does %d damage to you." % goblin1.power)
        if hero1.health <= 0:
            print("You are dead.")
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (goblin1.health, goblin1.power))
        if goblin1.health <= 0:
                print("Goblin is dead.")
        else:
            print("Goblin is alive!")
            


def main():
    while goblin1.alive() and hero1.alive() == True:

        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero1.attack()
            print(hero1.print_status())
            print(goblin1.print_status())
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
        
        else:
            print("Invalid input %r" % user_input)
        if goblin1.health > 0:
            # Goblin attacks hero
            goblin1.attack()

hero1 = Hero('Captain', 10, 5, True)
goblin1 = Goblin('Bo-Bo', 6, 2, True)
main()
