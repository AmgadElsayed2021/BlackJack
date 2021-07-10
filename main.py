import random
import csv

suits = ['\u2660', '\u2661', '\u2662', '\u2663']
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def shuffleDeck():
    try:
        deck = []
        # create deck of 52 cards
        for suit in suits:
            for rank in ranks:
                deck.append(rank + suit)
        # shuffle the deck and return
        random.shuffle(deck)
        return deck
    except KeyError as e:
        print(10 , "has this issue" , e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)


def readFile():
    try:
        file = open("money.txt", "r")
        line = float(file.readline())
        return line
    except FileNotFoundError:
        print(f'money: {0} $')
        return 0
    except OSError:
        return 0

def writeFile(cashOnHand):
    try:
        with open("money.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(cashOnHand)
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)


def dealTheCards(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card

def printPlayerCards(player):
    print("Your cards:")
    for i in range(len(player)):
        print(player[i])
    print()

def printDealerCards(house):
    print("DEALER CARDS:")
    for i in range(len(house)):
        print(house[i])
    print()

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

def displayTotalPoints(house , player):
    printPlayerCards(player)
    printDealerCards(house)
    print('YOUR POINTS:\t', totalCardsValue(player))
    print('DEALER POINTS:\t', totalCardsValue(house), "\n")

def BetWinOrLose(player, house, BetAmount):
    StartingBalance = readFile()
    if totalCardsValue(house) < totalCardsValue(player) <= 21 or totalCardsValue(house) > 21:
        Earnings = float(BetAmount) * 1.5
        print("Congratulations! You won the Game\n")
        print("you have earned:\t", Earnings)
        Balance = StartingBalance + Earnings
    elif totalCardsValue(player) < totalCardsValue(house) <= 21 or totalCardsValue(player) > 21:
        print("Sorry! House won the Game\n")
        print("you have lost:\t", float(BetAmount))
        Balance = int(StartingBalance) - float(BetAmount)
    else:
        print("It's a Tie!\n")
        Balance = StartingBalance

    print("Your Balance:\t\t", str(Balance))

    try:
        with open("money.txt", "w", newline="") as file:
            file.write(str(Balance))
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)


# lets make the code shorter
def BlackJack(house , player):

    # displayTotalPoints(house, player)
    if totalCardsValue(player) == 21:
        print('\nBlack Jack! You are the winner!')
    elif totalCardsValue(house) == 21:
        print("\nDealer got a black Jack . sorry you lost")

def hitLoop(deck, player):

    choice = input('Hit or Stand? (hit/stand):')
    print()
    while choice.lower() == "hit":
        dealTheCards(deck, player)
        printPlayerCards(player)
        if totalCardsValue(player) >= 21 :
            return
        # comparePlayersTotalAndDeclareWinner(house, player)
        # BlackJack(house, player)

        choice = input('Hit or Stand? (hit/stand):')
        print()

def main():
    house = []
    player = []

    print('Black Jack!\nBlack jack payout is 3:2\n')
    StartingBalance = readFile()
    print(f'money: {StartingBalance} $')
    try:
        BetAmount = float(input('Bet amount:\t'))
    except ValueError:
        print("Enter a valid number greater than zero")

    deck = shuffleDeck()
    for i in range(2):
        dealTheCards(deck, house)
        dealTheCards(deck, player)
    if totalCardsValue(player) < 21 and totalCardsValue(house) < 21:
        print('\nDealer Show Card:\n', house[0], '\n')
        printPlayerCards(player)
        # call the hit loop
        hitLoop(deck, player)

        while totalCardsValue(house) < 17 and totalCardsValue(player) < 21:
            dealTheCards(deck, house)
        BlackJack(house, player)

    # elif totalCardsValue(player) == 21 or totalCardsValue(house) == 21:
    #     BlackJack(house, player)

    displayTotalPoints(house, player)
    # comparePlayersTotalAndDeclareWinner(house, player)
    BetWinOrLose(player, house, BetAmount)

if __name__ == "__main__":
    main()


# def print_cards(cards):
#     s = ""
#     for card in cards:
#         s = s + "\t _______ "
#     print(s)
#
#
#     s = ""
#     for card in cards:
#         if card.rank == '10':
#             s = s + "\t| {}    |".format(card.rank)
#         else:
#             s = s + "\t| {}     |".format(card.rank)
#
#     print(s)
#
#     s = ""
#     for card in cards:
#         s = s + "\t|   {}   |".format(card.suit)
#     print(s)
#
#     s = ""
#     for card in cards:
#         if card.value == '10':
#             s = s + "\t|    {} |".format(card.rank)
#         else:
#             s = s + "\t|    {}  |".format(card.rank)
#     print(s)
#
#     s = ""
#     for card in cards:
#         s = s + "\t|_______|"
#     print(s)
#
#     print()
# def comparePlayersTotalAndDeclareWinner(house, player):
#     houseTotal = int(totalCardsValue(house))
#     playerTotal = int(totalCardsValue(player))
    # if playerTotal > 21:
    #     return
    # elif houseTotal > 21:
    #     return
    # elif totalCardsValue(house) == totalCardsValue(player) <= 21:
    #     return
    # else :
    #     BlackJack(house, player)

    # if houseTotal < playerTotal:
    #     if (playerTotal < 21):
    #         print('\nCongrats! You are the winner!')
    #     elif (playerTotal < houseTotal <= 21) or playerTotal > 21:
    #         print('\nsorry,House wins! You lose !')
    #     elif houseTotal == playerTotal:
    #         print("\nit's a Tie!")
    # elif houseTotal > 21:
    #     print('\nCongrats! You are the winner!')
    # elif (playerTotal < houseTotal <= 21) or playerTotal > 21:
    #     print('\nsorry,House wins! You lose !')
    # else:
    #     print("\nit's a Tie!")
