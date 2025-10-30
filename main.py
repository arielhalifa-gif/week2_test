if __name__ == "__main__":
    import core.deck as d, core.game_logic as game, core.player_io as pl
    deck = d.build_standard_deck()
    shuffled_deck = d.shuffle_by_suit(deck)
    player = {"hand": []}
    dealer = {"hand": []}
    game.run_full_game(deck, player, dealer)