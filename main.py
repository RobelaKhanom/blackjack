import art
import random

def results(total_player, total_dealer):
    """processes the results and outputs for 3 out of 4 conditions"""
    if total_dealer >= 21 and total_player < 21:
        print('You win!')
    elif total_player >=21 and total_dealer < 21:
        print('You lose')
    elif total_player >= 21 and total_dealer >=21:
        print("it's a draw")

def drawcards(player, dealer, cards):
    """draws a random card for each of the players"""
    player.append(random.choice(cards))
    cards.remove(player[-1])
    dealer.append(random.choice(cards))
    cards.remove(dealer[-1])
    return player, dealer, cards

def calculate_score(player, dealer):
    total_player = sum(player)
    total_dealer = sum(dealer)
    return total_player, total_dealer

def drawcards_decision(card_draw_decision, player, dealer, cards):
    """Draws random card for player/dealer based on whether player chose to draw or pass"""
    if card_draw_decision == 'y':
        player, dealer, cards = drawcards(player, dealer, cards)
    elif card_draw_decision == 'n':
        dealer.append(random.choice(cards))
        cards.remove(dealer[-1])
    return player, dealer, cards

def blackjack():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    dealer = []
    player = []

    for i in range(2):
        player, dealer, cards = drawcards(player, dealer, cards)

    total_player, total_dealer = calculate_score(player, dealer)
    if total_dealer >= 21 or total_player >= 21:
        results(total_player,total_dealer)

    print(f"Your hand is {player} \n computer's' first draw is {dealer}")
    card_draw_decision = input("Would you like to draw another card y or n for pass?\n")
    player, dealer, cards = drawcards_decision(card_draw_decision, player, dealer, cards)
    total_player, total_dealer = calculate_score(player, dealer)

    print(f"Your hand is {player} \n computer's' first draw is {dealer}")
    results(total_player, total_dealer)

    while total_dealer < 21 and total_player < 21:
        card_draw_decision = input("Would you like to draw another card y or n for pass?\n")
        player, dealer, cards = drawcards_decision(card_draw_decision, player, dealer, cards)
        total_player, total_dealer = calculate_score(player, dealer)
        results(total_player, total_dealer)

    continue_game = input("Would you like to play again?")
    if continue_game == 'y':
        blackjack()
    if continue_game == 'n':
        return

blackjack()