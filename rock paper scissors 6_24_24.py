import random

game_active = True

while game_active == True:
       num_rounds = int(input("Welcome to Rock, Paper, Scissors. How many rounds would you like to play?"))
       rounds_played = 0
       c_win = 0
       p_win = 0
       
       options_list = ["rock", "paper", "scissors"]
       
       while num_rounds > rounds_played:
              p_choice = str(input("Cool. Make your choice then...rock, paper, or scissors?"))
              c_choice = random.choice(options_list)
              
              if p_choice == c_choice:
                     print("It appears to be a tie. Try again!")
                     rounds_played += 1
              
              elif p_choice == "rock" and c_choice == "paper":
                     print("Paper covers rock...you lose this round!")
                     rounds_played += 1
                     c_win += 1
                     print("your score:", p_win)
                     print("CPU score:", c_win)
              
              elif p_choice == "rock" and c_choice == "scissors":
                     print("Rocks smash scissors...you win this round!")
                     rounds_played += 1
                     p_win += 1
                     print("your score:", p_win)
                     print("CPU score:", c_win)
              
              elif p_choice == "scissors" and c_choice == "rock":
                     print("Rocks smash scissors...you lose this round!")
                     rounds_played += 1
                     c_win += 1
                     print("your score:", p_win)
                     print("CPU score:", c_win)
              
              elif p_choice == "scissors" and c_choice == "paper":
                     print("Scissors cut paper...you win this round!")
                     rounds_played += 1
                     p_win += 1
                     print("your score:", p_win)
                     print("CPU score:", c_win)
              
              elif p_choice == "paper" and c_choice == "rock":
                     print("Paper covers rock...you win this round!")
                     rounds_played += 1
                     p_win += 1
                     print("your score:", p_win)
                     print("CPU score:", c_win)
              
              elif p_choice == "paper" and c_choice == "scissors":
                     print("Paper cuts scissors...you lose this round!")
                     rounds_played += 1
                     c_win += 1
                     print("your score:", p_win)
                     print("CPU score:", c_win)
                     
              if rounds_played == num_rounds:
                     print("Good game! Let's play again some time.")
                     
              if rounds_played == num_rounds and p_win > c_win:
                     print("Looks like I lost...good game! Let's play again some time.")
                     
              if rounds_played == num_rounds and c_win > p_win:
                     print("I won! That was fun. let's play again some time!")
                            
                     game_active = False
       
               
             
             