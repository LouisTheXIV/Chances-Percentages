import random
import os, sys

A_CHANCE = 75
A_PERCENTAGE = 0.75
B_CHANCE = 50
B_PERCENTAGE = 0.50
C_CHANCE = 25
C_PERCENTAGE = 0.25
EMPTY_CHANCE = 50
EMPTY_PERCENTAGE = 0.50

options = ["A", "B", "C"]

def generate_table(chance=None):
    table = [0, 0, 0]
    if chance is None:
        for x in range(3):
            isempty = bool(random.randint(0,101) < EMPTY_CHANCE)
            if not isempty:
                for i in options:
                    istrue = bool(random.randint(1,101) < get_chance(i))
                    if istrue:
                        table[x] = i
            else:
                pass
        chances = []
        for x in table:
            chance = get_chance(x, True)
            chances.append(chance)
            
        total_chance = chances[0] * chances[1] * chances[2]
        return f"Tabel: {table[0]} {table[1]} {table[2]}\nValues: {chances[0]}, {chances[1]}, {chances[2]}\nTotal Chance: {total_chance}"
    
    else:
        while True:
            valid = False

            while not valid:
                x_ = random.choice(options)
                x1_ = random.choice(options)
                x2_ = random.choice(options)
                x = get_chance(x_, True)
                x1 = get_chance(x1_, True)
                x2 = get_chance(x2_, True)
                result = x * x1 * x2
                try:
                    with open("tries.txt", "r") as f:
                        if result not in f.readlines():
                            valid=True
                        else:
                            pass
                except FileNotFoundError:
                    with open("tries.txt", "w") as f:
                        f.close()
            
            if result == chance:
                os.remove("tries.txt")
                return f"Tabel: {x_}, {x1_}, {x2_}\nValues: {x}, {x1}, {x2}\nTotal Chance: {chance}"
            else:
                with open("tries.txt", "a") as f:
                    f.write(f"{result}\n")
                    f.close()
        
        

def get_chance(option, ispercentage=False):
    if ispercentage == False:
        if option == "A":
            return A_CHANCE
        elif option == "B":
            return B_CHANCE
        elif option == "C":
            return C_CHANCE
        elif option == 0:
            return EMPTY_CHANCE
    else:
        if option == "A":
            return A_PERCENTAGE
        elif option == "B":
            return B_PERCENTAGE
        elif option == "C":
            return C_PERCENTAGE
        elif option == 0:
            return EMPTY_PERCENTAGE       
