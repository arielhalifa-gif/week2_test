def calculate_hand_value(hand: list[dict]) -> int:
    # יש לי שני קלפים או יותר תלוי בכמות הקלפים וצריך לסכום את כל הקלפים
    sum_hand = 0
    for i in range(len(hand)):
        if isinstance(hand[i]["rank"], int):
            sum_hand += int(hand[i]["rank"])
        elif hand[i]["rank"] == "A":
            sum_hand += 1
        else:
            sum_hand += 10
    return sum_hand


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    # מחלקים 2 קלפים ועוד 2 קלפים ומוציאים אותם מהחפיסה
    # מדפיסים את הסכומים של שני הידיים
    for i in range(2):
        player["hand"].append(deck.pop())
    print(calculate_hand_value(player["hand"]))
    for i in range(2):
        dealer["hand"].append(deck.pop())
    print(calculate_hand_value(dealer["hand"]))


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    # בודקים שהערך פחות או שווה 17
    # אם הערך עבר את 21 מדפיס פסילה ומחזיר (False)
    # בין 17 ל21 הדילר סיים את המשחק True
    dealer_hand = calculate_hand_value(dealer["hand"])
    while dealer_hand < 17:
        dealer["hand"].append(deck.pop())
        dealer_hand = calculate_hand_value(dealer["hand"])
    if dealer_hand > 21:
        print("the dealer lose the round")
        return False
    return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    player_turn = pl.ask_player_action()
    game_over = False
    while not game_over:
        while player_turn == "H":
            player["hand"].append(deck.pop())
            player_hand = calculate_hand_value(player["hand"])
            print(player_hand)
            if player_hand > 21:
                print("the player lose the game")
                game_over = True
                break
            player_turn = pl.ask_player_action()
        action_dealer = dealer_play(deck, dealer) #בודקים אם הדילר ניפסל נגמר המשחק אם לא אז עושים השוואה
        if action_dealer:
            dealer_hand = calculate_hand_value(dealer["hand"])
            if dealer_hand > player_hand:
                print("the dealer has won the round")
            elif player_hand > dealer_hand:
                print("the player has won the round")
            else:
                print("teco")
        game_over = True