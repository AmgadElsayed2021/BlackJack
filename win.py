import db
import cards

def BetWinOrLose(player, house, BetAmount):
    StartingBalance = db.readFile()
    if cards.totalCardsValue(house) < cards.totalCardsValue(player) <= 21 or cards.totalCardsValue(house) > 21:
        Earnings = float(BetAmount) * 1.5
        Earnings = round(Earnings, 2)
        print("Congratulations! You won the Game\n")
        print("you have earned:\t", Earnings)
        Balance = StartingBalance + Earnings
    elif cards.totalCardsValue(player) < cards.totalCardsValue(house) <= 21 or cards.totalCardsValue(player) > 21:
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
    if cards.totalCardsValue(player) == 21:
        print('\nBlack Jack! You are the winner!')
    elif cards.totalCardsValue(house) == 21:
        print("\nDealer got a black Jack . sorry you lost")
