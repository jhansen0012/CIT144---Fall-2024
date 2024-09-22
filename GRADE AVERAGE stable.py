#Justin-Hansen

import sys

scores = []

loop_control = True

while loop_control == True:
    user_ini = input("Please enter grades for calculation. Type END to calculate, or PRINT to display grades to be calculated.").lower()
    if user_ini == "print":
        print(scores)
        continue
    
    elif user_ini == "end":
        if not scores:
            print("No grades entered.")
            continue            
        total = len(scores)
        average = round(sum(scores) / total, 2)
        print(f"Average test score is {average}, out of {total} grades.")
        sys.exit()
            
    conv_int = int(user_ini)
    if 0 <= conv_int <= 100:
        scores.append(conv_int)
    elif conv_int > 100:
        print("Data unacceptable, please try again.")
        continue