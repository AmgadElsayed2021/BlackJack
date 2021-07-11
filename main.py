import random

import db

suits = ['\u2660', '\u2661', '\u2662', '\u2663']
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


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


def displayTotalPoints(house, player):
    # printPlayerCards(player)
    printDealerCards(house)
    print('YOUR POINTS:\t', totalCardsValue(player))
    print('DEALER POINTS:\t', totalCardsValue(house), "\n")


def BetWinOrLose(player, house, BetAmount):
    StartingBalance = db.readFile()
    if totalCardsValue(house) < totalCardsValue(player) <= 21 or totalCardsValue(house) > 21:
        Earnings = float(BetAmount) * 1.5
        Earnings = round(Earnings, 2)
        print("Congratulations! You won the Game\n")
        print("you have earned:\t", Earnings)
        Balance = StartingBalance + Earnings
    elif totalCardsValue(player) < totalCardsValue(house) <= 21 or totalCardsValue(player) > 21:
        print("Sorry! House won the Game\n")
        print("you have lost:\t", BetAmount)
        Balance = int(StartingBalance) - float(BetAmount)
        Balance = round(Balance, 2)
    else:
        print("It's a Tie!\n")
        Balance = StartingBalance
    print("Your Balance:\t\t", round(Balance, 2))
    db.writeFile(Balance)


# lets make the code shorter
def BlackJack(house, player):
    # displayTotalPoints(house, player)
    if totalCardsValue(player) == 21:
        print('\nBlack Jack! You are the winner!')
    elif totalCardsValue(house) == 21:
        print("\nDealer got a black Jack . sorry you lost")


def hitLoop(deck, player):
    if totalCardsValue(player) < 21 :
        choice = input('Hit or Stand? (hit/stand):')
        print()
        while choice.lower() == "hit":
            dealTheCards(deck, player)
            printPlayerCards(player)
            if totalCardsValue(player) >= 21:
                return
            choice = input('Hit or Stand? (hit/stand):')
            print()

def stand(deck, house, player):
    while totalCardsValue(house) < 17 and totalCardsValue(player) < 21 \
            and totalCardsValue(house < totalCardsValue(player)):
        dealTheCards(deck, house)


def GetBetAmount(StartingBalance):
    while True:
        try:
            BetAmount = float(input('\nBet amount:\t'))
        except ValueError:
            print("Enter a valid number ")
            continue
        if BetAmount < 5:
            print("Enter a positive number greater than or equals 5$")
        elif BetAmount > StartingBalance:
            print("You don't have enough Balance")
        elif BetAmount >= 1000:
            print("Maximum bet is 1000$")

        else:
            return BetAmount

def GameStart(deck , house , player):
    for i in range(2):
        dealTheCards(deck, house)
        dealTheCards(deck, player)
    if totalCardsValue(player) < 21 and totalCardsValue(house) < 21:
        print('\nDealer Show Card:\n', house[0], '\n')
        printPlayerCards(player)
    else:
        printDealerCards(house)
        printPlayerCards(player)
        BlackJack(house, player)
def CheckBalance(Balance):
    while True:
        try:
            if Balance < 5:
                print("You don't have enough balance to start the game")
                choice = input("would you like to buy more chips . enter (yes) to buy")
                while choice.lower() == "yes":
                    AddBalance = float(input("How much money would you like to add:"))
                    Balance += AddBalance
                    db.writeFile(Balance)
                    choice = input("Do you want to add again (yes / no)")
                continue
        except ValueError:
            print("Enter a valid number ")
            continue
        else:
            return Balance

def main():
    house = []
    player = []
    print('Black Jack!\nBlack jack payout is 3:2\n')
    StartingBalance = db.readFile()

    print(f'money: {StartingBalance} $')
    StartingBalance = CheckBalance(StartingBalance)

    if StartingBalance >= 5:
        playGame = str(input("\nwould you like to start the game (yes/no)"))
        while playGame.lower() == "yes":
            house.clear()
            player.clear()
            StartingBalance = db.readFile()
            BetAmount = GetBetAmount(StartingBalance)
            deck = shuffleDeck()
            GameStart(deck , house, player)
            hitLoop(deck, player)
            stand(deck, house, player)
            BlackJack(house, player)
            displayTotalPoints(house, player)
            BetWinOrLose(player, house, BetAmount)
            CheckBalance(StartingBalance)

            playGame = str(input("\nwould you like to play another game (yes/no)"))

        print("\nBye!")

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
#         print('\n sorry,House wins! You lose !')
#     elif houseTotal == playerTotal:
#         print("\nit's a Tie!")
# elif houseTotal > 21:
#     print('\nCongrats! You are the winner!')
# elif (playerTotal < houseTotal <= 21) or playerTotal > 21:
#     print('\n sorry,House wins! You lose !')
# else:
#     print("\nit's a Tie!")
