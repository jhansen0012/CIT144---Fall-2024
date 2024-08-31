import random

word_list = []

def select_word():
    
    user_ini = input(str("Give me five words, each with four letters, and I will pick one at random. Then, you will have to guess the letters.  \n"))
    word_list.append(user_ini)
    
    for user_ini in range (4):
        user_ini = input(str("Anything else?  \n"))
        word_list.append(user_ini)    
    
    return random.choice(word_list)
    
def game():
    
    cpu_word = select_word()
            
    printed_word = ["_"] *len(cpu_word)
    
    attempt = 0
    right = 0
    count = cpu_word.count('i')
    
    while right < 4:
        print("Your word is: " + " ".join(printed_word))
        user_sec = input(str("Try and guess the letters!"  )).lower()
        
        if user_sec in cpu_word:
            print("Correct! Try guessing another.")
            
            for i in range(len(cpu_word)):
                if cpu_word[i] == user_sec:
                    printed_word[i] = user_sec
                    right += 1
        else:
            print("Sorry, that letter is not part of the word.  ")
    print("You guessed the whole word! Great job!")
              
game()