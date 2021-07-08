import random
import csv


def shuffleDeck():
    # search google for python samples for cards to make it looks real
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    #  since the console want names for suits instead of pics so lets stick to it
    # suits = [' of Hearts' , ' of Spades' , ' of Clubs' , ' of Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []

    # create deck of 52 cards
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    # shuffle the deck and return
    random.shuffle(deck)
    return deck


def readFile():
    try:
        with open("Bet.csv", "r") as file:
            reader = csv.reader(file)
            Bet = []
            for row in reader:
                Bet.append(row)
            print(f'money: {Bet[0][0]} $')
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print()


def writeFile():
    try:
        with open("Bet.csv", "w") as file:
            writer = csv.writer(file)
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print()


def dealTheCards(deck, player):
    card = deck.pop()
    player.append(card)
    return card


def totalCardsValue(hand):
    try:
        cardsValues = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                       "J": 10, "Q": 10, "K": 10}
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
    except ValueError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print()


def comparePlayersTotalAndDeclareWinner(house, player):
    houseTotal = totalCardsValue(house)
    playerTotal = totalCardsValue(player)
    if playerTotal == 21 or (houseTotal < playerTotal <= 21) or houseTotal > 21:
        print('You won!')
    elif houseTotal == 21 or (playerTotal < houseTotal <= 21) or playerTotal > 21:
        print('You lose !')
    else:
        print("it's a Tie!")


def main():
    print('Black Jack!\nBlack jack payout is 3:2\n')
    readFile()
    BetAmount = input('Bet amount:\t')
    print()
    house = []
    player = []
    deck = shuffleDeck()

    for i in range(2):
        dealTheCards(deck, house)
        dealTheCards(deck, player)
    print('Dealer Show Card:\n', house[0], '\n')
    print('YourCards:\n', player[0], '\n', player[1])

    #  start asking user for hit or stand
    # i need to use a while loop here
    choice = input('\nHit or Stand? (hit/stand):')

    while choice.lower() == "hit":
        print('\nYour Cards:')
        card = dealTheCards(deck, player)
        for i in range(len(player)):
            print(player[i])

        if totalCardsValue(player) > 21:
            print('You bust! ...house wins!')
            return
        if totalCardsValue(player) == 21:
            print('You win!')
            return
        choice = input('\nHit or Stand? (hit/stand):')

    # from what i learnt from videos the house has to play again once the user stand and house score is less than 17
    # so lets try it
    # remember to use a while loop here as well
    while totalCardsValue(house) < 17:
        print('\nDealer Cards::')
        card = dealTheCards(deck, house)
        for i in range(len(player)):
            print(player[i])
        if totalCardsValue(house) > 21:
            print('house bust! ...you wins!')
            return
        comparePlayersTotalAndDeclareWinner(house, player)

    #     last thing to check after the house exceeds 16 we need to compare the results and declare winner.
    comparePlayersTotalAndDeclareWinner(house, player)

    return


if __name__ == "__main__":
    main()
