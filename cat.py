import random

kitty_counter = 0

class Cat:
    def __init__(self, name, breed, color, sound, action):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound
        self.action = action
        self.floof = False
        self.loaf = False

    def main(self):
        roll = random.randint(0, 14)  # Random number between 0 and 14
        if roll < 7:
            self.floof = True
            self.loaf = False
        else:
            self.loaf = True
            self.floof = False

c = Cat("Curry", "long haired", "brown", "meow", "jump")

while kitty_counter < 10:
    c.main()  # Determine the state of the cat
    user_ini = input("Pet the kitty? Type Y or N! ").upper()
    
    if user_ini == "Y":
        if c.floof:
            print(f"The {c.breed} cat tried to {c.sound} at you!")
            kitty_counter += 1
        elif c.loaf:
            print(f"The {c.color} cat tried to {c.action} at you!")
            kitty_counter += 1
    elif user_ini == "N":
        print("The cat ran away...")
        break
    
    if kitty_counter == 10:
        print("The cat ran away...")
   
