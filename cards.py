import random
suits = ['\u2660', '\u2661', '\u2662', '\u2663']
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# create a function to shuffle the deck
def shuffleDeck():
    try:
        deck = []
        # create deck of 52 cards
        for suit in suits:
            for rank in ranks:
                deck.append(rank + suit)
        random.shuffle(deck)
        if len(deck) <= 26:
            deck.clear()
            for suit in suits:
                for rank in ranks:
                    deck.append(rank + suit)
            random.shuffle(deck)
            return deck
        return deck
    except KeyError as e:
        print(10, "has this issue", e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)

# function to deal the cards
def dealTheCards(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card

# function to print the player cards
def printCards(hand):
    # for i in range(len(hand)):
    s = ""
    for card in hand:
        s = s + "\t _______ "
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|{}     |".format(card[:2])
        else:
            s = s + "\t| {}     |".format(card[0][0])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|   {}   |".format(card[2:3])
        else:
            s = s + "\t|   {}   |".format(card[1])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|     {}|".format(card[:2])
        else:
            s = s + "\t|     {} |".format(card[0])
    print(s)

    s = ""
    for card in hand:
        s = s + "\t'-------'"
    print(s)

    print()
def UnShownCard(hand):
    # for i in range(len(hand)):
    s = ""
    s = s + "\t _______\t _______ "
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|{}     |\t| ??    |".format(card[:2])
        else:
            s = s + "\t| {}     |\t| ??    |".format(card[0][0])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|   {}   |\t|   ??  |".format(card[2:3])
        else:
            s = s + "\t|   {}   |\t|   ??  |".format(card[1])
    print(s)

    s = ""
    for card in hand:
        if card[:2] == '10':
            s = s + "\t|     {}|\t|     ??|".format(card[:2])
        else:
            s = s + "\t|     {} |\t|     ??|".format(card[0])
    print(s)

    s = ""
    s = s + "\t'-------'\t'-------'"
    print(s)
    print()

def displayPlayerCards(player):
    print("Your Cards:")
    printCards(player)

def displayDealerCards(house):
    print("Dealer Cards:")
    printCards(house)


def totalCardsValue(hand):
    try:
        cardsValues = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                       "8": 8, "9": 9, "1": 10, "J": 10, "Q": 10, "K": 10}
        result = 0
        AcesCount = 0
        # check how many aces on hand
        for card in hand:
            result += cardsValues[card[0]]
            if card[0] == 'A':
                AcesCount += 1

                while result > 21 and AcesCount > 0:
                    result -= 10
                    AcesCount -= 1
        return result
    except KeyError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)


def displayTotalPoints(house, player):
    displayDealerCards(house)
    print('YOUR POINTS:\t', totalCardsValue(player))
    print('DEALER POINTS:\t', totalCardsValue(house), "\n")
