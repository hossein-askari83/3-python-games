from hangman_logic_game import start_game

whant_to_play = input("WELCOME TO MY GAME \nARE YOU WHAT TO PLAT A GAME ? ")
valid_awnsers_yes = ['yes', 'ok', 'letsgo', 'yeah', 'ya', 'y', 'iwant']
valid_awnsers_no = ['no', 'na', 'not', 'idont', 'n']
if whant_to_play.lower() in valid_awnsers_yes:
    start_game()
elif whant_to_play in valid_awnsers_no:
    print("OK HAVE A GOOD DAY")
else:
    print("INVALID ANSWER")
