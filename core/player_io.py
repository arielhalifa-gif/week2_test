def ask_player_action() -> str:
    action = input("please enter youre action (S or H)\n")
    while action != "S" or action != "H":
        print("your input is not valid")
        action = input("please enter youre action (S or H)\n")
    return action