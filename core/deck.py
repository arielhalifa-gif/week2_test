import random

def build_standard_deck() -> list[dict]: 
    # בונה חפיסת קלפים שלימה
    suite_cards = ["H","C","D","S"]
    cards = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    full_deck = []
    for i in suite_cards:
        for j in cards:
            full_deck.append({"rank": j, "suite": i})
    return full_deck


def convert_value(rank: str) -> int:
    list_chek = ["J", "Q", "K"]
    if rank == "A":
        return 1
    else:
        return 10

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    list_chek = ["A", "J", "Q", "K"]
    for s in range(swaps):
        index_i = random.randint(0,51)
        card_i = deck[index_i]
        is_j_ok = False
        while not is_j_ok:
            index_j = random.randint(0,51)
            card_j = deck[index_j]
            if index_j != index_i:
                if card_j["suite"] == "H":
                    if card_j["rank"] in list_chek:
                        value = convert_value(card_j["rank"])
                    else:
                        value = int(card_j["rank"])
                    if value %5 == 0:
                        is_j_ok = True


                elif card_j["suite"] == "C":
                    if card_j["rank"] in list_chek:
                        value = convert_value(card_j["rank"])
                    else:
                        value = int(card_j["rank"])
                    if value %3 == 0:
                        is_j_ok =True

                elif card_j["suite"] == "D":
                    if card_j["rank"] in list_chek:
                        value = convert_value(card_j["rank"])
                    else:
                        value = int(card_j["rank"])
                    if value %2 == 0:
                        is_j_ok = True
                else: # == "S"
                    if card_j["rank"] in list_chek:
                        value = convert_value(card_j["rank"])
                    else:
                        value = int(card_j["rank"])
                    if value %7 == 0:
                        is_j_ok = True
        deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
    return deck


