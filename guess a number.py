import random
import sys

loop_control = False

options_list = [1, 2, 3, 4, 5]

user_ini = int(input("Guess my number! It is between 1 and 5."))
cpu_ini = random.choice(options_list)

if user_ini == cpu_ini:
    print("Wow. Okay then, next time I will have to pick something harder!")

while user_ini != cpu_ini:
    loop_control = True
    
    user_ini = int(input("Try again! I'll let you know if you are too high or too low."))
    
    if user_ini > cpu_ini:
        user_ini = int(input("Too high..."))
    
    if cpu_ini > user_ini:
        user_ini = int(input("Too low..."))
    
    if cpu_ini == user_ini:
        print("You got it! good job. Thanks for playing...bye!")
        
        loop_control = False
