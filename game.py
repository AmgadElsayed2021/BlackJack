import cards
import win
def hitLoop(deck, player):
    if cards.totalCardsValue(player) < 21 :
        choice = input('Hit or Stand? (hit/stand):')
        print()
        while choice.lower() == "hit":
            cards.dealTheCards(deck, player)
            cards.displayPlayerCards(player)
            if cards.totalCardsValue(player) >= 21:
                return
            choice = input('Hit or Stand? (hit/stand):')
            print()

def stand(deck, house, player):
    while cards.totalCardsValue(house) < 17 and cards.totalCardsValue(player) < 21 :
#         if cards.totalCardsValue(house) < cards.totalCardsValue(player):
        cards.dealTheCards(deck, house)

def GameStart(deck , house , player):
    cards.dealTheCards(deck, house)
    for i in range(2):
        cards.dealTheCards(deck, player)
    if cards.totalCardsValue(player) < 21 and cards.totalCardsValue(house) < 21:
        cards.UnShownCard(house)
        cards.dealTheCards(deck, house)
        cards.displayPlayerCards(player)
    else:
        cards.displayDealerCards(house)
        cards.dealTheCards(deck, house)
        cards.displayPlayerCards(player)
        win.BlackJack(house, player)
