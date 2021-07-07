import random

def shuffleDeck():
    # search google for python samples for cards to make it looks real
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []

    # create deck of 52 cards
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)

    # shuffle the deck and return
    random.shuffle(deck)
    return deck

def dealTheCards(deck , player):
    card = deck.pop()
    player.append(card)
    return card

def totalCardsValue(hand):
    cardsValues = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                   "J": 10, "Q": 10, "K": 10}
    result = 0
    AcesCount = 0
    # check how many aces on hand
    for card in hand :
        result += cardsValues[card[0]]
        if card[0] == 'A':
            AcesCount += 1

    while result > 21 and AcesCount > 0:
        result -= 10
        AcesCount -= 1
    return result


def comparePlayersTotalAndDeclareWinner(house , player):
    houseTotal = total(house)
    playerTotal = total(player)
    if (playerTotal < houseTotal <= 21) or playerTotal > 21 or houseTotal ==21:
        print('You lose!')
    elif houseTotal > 21 or playerTotal == 21 or (houseTotal < playerTotal <= 21):
        print('You won !')
    else:
        print("it's a Tie!")

def main():
    deck = shuffleDeck()
    house = []
    player = []
    for i in range(2):
        dealTheCards(deck, player)
        dealTheCards(deck, house)
    print('Dealer Show Card:\n{:>7}'.format(house[0]))
    print('YourCards:\n{:>7}  {:7}'.format(player[0], player[1]))


if __name__ == "__main__":
    main()

