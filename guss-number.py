

from random import randint
import time
print("WELCOME TO MY GAME")
whant_to_play = input("ARE YOU WHANT PLAY? (Yes/No) ")
if whant_to_play.lower() == "yes" :
    def start_game():
        print("OK LETS GO")
        time.sleep(0.5)
        chanses = 3
        print(f"YOU HAVE {chanses} CHANSE TO GUSS NUMBER")
        time.sleep(0.5)
        randomNumber = randint(0,20)
        if randomNumber < 10:
            time.sleep(0.5)
            print("\nHINT NUMBER ONE ==> NUMBER SMALLER THAN 10 ")
        else:
            time.sleep(0.5)
            print("\nHINT NUMBER ONE ==> NUMBER BIGGER THAN 9 ")
        time.sleep(0.5)
        gussNumber1 = int(input("\nGUSS THE NUMBER ==>"))
        if gussNumber1 == randomNumber:
            time.sleep(0.5)
            print("\nTHATS RIGHT , YOU WIN")
            time.sleep(0.5)
            print(F"\nTHE NUMBER WAS : {randomNumber}")
            time.sleep(0.5)
            whanna_play_again = input("YOU WHANT TO PLAY AGAIN? (Yes/No) ")
            if whanna_play_again.lower() == "no":
                time.sleep(0.5)
                print("OK HAVE A GOOD DAY")
            else :
                start_game()
        else:
            time.sleep(0.5)
            print("\nOHH THATS WRONG LETS TRY AGAIN ")
            chanses-=1
            time.sleep(0.5)
            print(f"\nYOU HAVE {chanses} CHANSES")
            if randomNumber < 10:
                if randomNumber < 5:
                    time.sleep(0.5)
                    print("\nHINT NUMBER TWO ==> NUMBER SMALLER THAN 5")
                else:
                    time.sleep(0.5)
                    print("\nHINT NUMBER TWO ==> NUMBER BIGGER THAN 4 ")
                    i = 3
            else:
                if randomNumber < 15:
                    time.sleep(0.5)
                    print("\nHINT NUMBER TWO ==> NUMBER SMALLER THAN 15 ")
                    i = 4
                else:
                    time.sleep(0.5)
                    print("\nHINT NUMBER TWO ==> NUMBER BIGGER THAN 14 ")
                    i = 5
            time.sleep(0.5)
            gussNumber2 = int(input("\nGUSS THE NUMBER ==>"))
            if gussNumber2 == randomNumber:
                time.sleep(0.5)
                print("\nTHATS RIGHT , YOU WIN")
                time.sleep(0.5)
                print(F"\nTHE NUMBER WAS : {randomNumber}")
                time.sleep(0.5)
                whanna_play_again = input("YOU WHANT TO PLAY AGAIN? (Yes/No) ")
                if whanna_play_again.lower() == "no":
                    time.sleep(0.5)
                    print("OK HAVE A GOOD DAY")
                    
                else :
                    start_game()
            else:
                print("\nOHH THATS WRONG LETS TRY AGAIN ")
                chanses-=1
                print(f"\nYOU HAVE {chanses} CHANSES")
                if randomNumber < 5:
                    hint3 = randint(0, 4)
                    while hint3 == randomNumber or hint3 == gussNumber1 or hint3 == gussNumber2:
                        hint3 = randint(0, 4)
                    print(F"\nHINT NUMBER THREE ==> ITS NOT {hint3}")
                elif i == 3:
                    hint3 = randint(5, 9)
                    while hint3 == randomNumber or hint3 == gussNumber1 or hint3 == gussNumber2:
                        hint3 = randint(5, 9)
                    print(F"\nHINT NUMBER THREE ==> ITS NOT {hint3}")
                elif i == 4:
                    hint3 = randint(10, 14)
                    while hint3 == randomNumber or hint3 == gussNumber1 or hint3 == gussNumber2:
                        hint3 = randint(10, 14)
                    print(F"\nHINT NUMBER THREE ==> ITS NOT {hint3}")
                else:
                    hint3 = randint(15, 20)
                    while hint3 == randomNumber or hint3 == gussNumber1 or hint3 == gussNumber2:
                        hint3 = randint(15, 20)
                    print(F"\nHINT NUMBER THREE ==> ITS NOT {hint3}")
                gussNumber3 = int(input("\nGUSS THE NUMBER ==>"))
                if gussNumber3 == randomNumber:
                    print("\nTAHTS RIGHT YOU WIN")
                    print(F"\nTHE NUMBER WAS : {randomNumber}")
                    whanna_play_again = input("YOU WHANT TO PLAY AGAIN? (Yes/No) ")
                    if whanna_play_again.lower() == "no":
                        print("OK HAVE A GOOD DAY")
                        
                    else :
                        start_game()
                else:
                    print("\nIM SORRY YOU LOSE")
                    print(F"\nTHE NUMBER WAS : {randomNumber}")
                    whanna_play_again = input("YOU WHANT TO PLAY AGAIN? (Yes/No) ")
                    if whanna_play_again.lower() == "no":
                        print("OK HAVE A GOOD DAY")
                        
                    else :
                        start_game()
    start_game()
else : 
    print("OK HAVE A GOOD DAY")