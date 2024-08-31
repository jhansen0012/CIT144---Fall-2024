shopping_list = []

loop_control = False

item_ini = input(str("Welcome! We are going to make a shopping list. What is your first item?"))
shopping_list.append(item_ini)
loop_control = True

while loop_control == True:
    prompt = input(str("Is this your last item?"))
    
    if prompt == "no":
        list_item = input(str("What is your next item?"))
        shopping_list.append(list_item)
    
    if prompt == "yes":
        loop_control == False    
        break
        
print(*shopping_list, sep = "\n")
prompt = input(str("Are you satisfied with the list above?"))

if prompt == "yes":
    print("Glad I could help. Goodbye!")

if prompt == "no":
    loop_control == True
    input(str("What else would you like to add?"))