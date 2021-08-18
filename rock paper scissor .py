
# get infromation for rounds-----
player1_wins = 0               #|
player2_wins = 0               #|
roundToWin = 5                 #|
# get infromation for rounds-----


# title------------------------------------
print("welcome to my game".upper())      #|
print("\nROCK ....")                     #|
print("PAPER ....")                      #|
print("scisseros ....".upper())          #|
print(f"\nWIN {roundToWin} ROUND TO WIN")#|
# title------------------------------------ 


# while for end game in 3 round-----------------------------------
while player1_wins < roundToWin and player2_wins < roundToWin : #|
# while for end game in 3 round-----------------------------------


    # random move from computer-------------
    from random import randint            #|
    computerMove = randint(0,2)           #|
    if computerMove == 0 :                #|
        computerMove = "ROCK"             #|
    elif computerMove == 1 :              #|
        computerMove = "ROCK"             #|
    elif computerMove == 2 :              #|
        computerMove = "SCISSEROS"        #|
    # random move from computer-------------


    #get moves------------------------------------------------------------------------------------
    player_1 = input("\nplayer 1 make your move :".upper()).upper()                             #|
    if player_1 == "q".upper() or player_1 == "quit".upper() or player_1 == "exit".upper() :    #|
        print("\nPLAYER ONE QUIT THE GAME")                                                     #|
        break                                                                                   #|
    player_2 = computerMove                                                                     #|
    print(f"\nplayer 2 make your move :{computerMove}".upper())                                 #|
    #get moves------------------------------------------------------------------------------------


    #game logic----------------------------------------------------------------
    if player_1 == player_2:                                                 #|
        print("\nWOW THE MOVES ARE THE SAME")                                #|
    elif player_1 == "ROCK":                                                 #|
        if player_2 == "ROCK":                                               #|
            print("\nPLAYER TWO WIN THIS ROUND")                             #| 
            player2_wins+=1                                                  #|
        elif player_2 == "SCISSEROS":                                        #|
            print("\nPLAYER ONE WIN THIS ROUND")                             #|
            player1_wins+=1                                                  #|
    elif player_1 == "PAPER":                                                #|
        if player_2 =="ROCK":                                                #|
            print("\nPLAYER ONE WIN THIS ROUND")                             #|
            player1_wins+=1                                                  #|
        elif player_2 == "SCISSEROS" :                                       #|
            print("\nPLAYER TWO WIN THIS ROUND")                             #|
            player2_wins+=1                                                  #|
    elif player_1 == "SCISSEROS":                                            #|
        if player_2 == "ROCK":                                               #|
            print("\nPLAYER TWO WIN THIS ROUND")                             #|
            player2_wins+=1                                                  #|
        elif player_2 == "PAPER":                                            #|
            print("\nPLAYER ONE WIN THIS ROUND")                             #|
            player1_wins+=1                                                  #|
    else :                                                                   #|
        print("\nWELL THERE IS A PROBLEM ")                                  #|
    print(f"\nPLAYER ONE : {player1_wins} \t PLAYER TWO : {player2_wins} ")  #|
    #game logic----------------------------------------------------------------


# final massage---------------------------------------------------------------------------------------------------------------------
if player1_wins > player2_wins and (not (player_1 == "q".upper() or player_1 == "quit".upper() or player_1 == "exit".upper())) :  #|
    print(f"\nCONGRAJLATION PLAYER ONE IS THE FINAL WINNER")                                                                      #|
else :                                                                                                                            #|
    print(f"\nCONGRAJLATION PLAYER TWO IS THE FINAL WINNER")                                                                      #|
# final massage---------------------------------------------------------------------------------------------------------------------
