valid_awnsers_yes = ['yes', 'ok', 'letsgo', 'yeah', 'ya', 'y', 'iwhant']
valid_awnsers_no = ['no', 'na', 'not', 'idont', 'n']


def start_game():
    import random
    print("OK LETS GO >>>> ")
    chanses = 10
    print(f"YOU HAVE {chanses} CHANCES TO GUSS LETTRS")
    words_list = ('watch', 'secret', 'headphone',
                  'cable', 'manitor', 'keyboard')
    random_word = random.choice(words_list)
    blanks = ['-' for letter in range(len(random_word))]
    repat = {'': 0}
    win = False
    while chanses > 0:
        guss = input("GUSS A LETTER >>> ")
        if guss.lower() in random_word:
            if guss.lower() in repat:
                guss_LetterIndex_repeat = random_word.index(
                    guss.lower(), repat[guss]+1)
                blanks[guss_LetterIndex_repeat] = guss.upper()
            else:
                guss_LetterIndex = random_word.index(guss.lower())
                repat[guss] = guss_LetterIndex
                blanks[guss_LetterIndex] = guss
            blanks_join = ''.join(blanks)
            if (blanks_join.lower()) == random_word:
                win = True
                break
            else:
                print(f"NICE! YOUR GUSS IS IN WORD >>> {blanks_join.upper()}")
        else:
            chanses -= 1
            print("OOH IM SORRY YOUR LETTER IS NOT IN WORD")
            print(f"YOU HAVE {chanses} CHANSES")
            print("TRY AGAIN : ")

    if win == True:
        print("CONGRATULATIONS YOU WIN")
        print(f"THE WORD WAS {random_word.upper()} ")
    else:
        print("UNFORTUNATELY YOU LOSE")

    playAgain = input("WANNA PLAY AGAIN ? ")
    if playAgain in valid_awnsers_yes:
        start_game()
    elif playAgain in valid_awnsers_no:
        print("OK HAVE A GOOD DAY")
    else:
        print("INVALID AWNSER")
