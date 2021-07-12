import db
def GetBetAmount():
    while True:
        try:
            Balance = db.readFile()
            BetAmount = float(input('\nBet amount:\t'))
        except ValueError:
            print("Enter a valid number ")
            continue
        if BetAmount < 5:
            print("Enter a positive number greater than or equals 5$")
        elif BetAmount > Balance:
            print("You don't have enough Balance")
            CheckBetVsBalance(BetAmount)
        elif BetAmount >= 1000:
            print("Maximum bet is 1000$")

        else:
            return BetAmount

def CheckBalance():
    while True:
        try:
            Balance = db.readFile()
            if Balance < 5 :
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

def CheckBetVsBalance(BetAmount):
    StartingBalance = db.readFile()
    while True:
        try:
            if BetAmount > StartingBalance:
                print("Your Bet is greater than your Balance")
                choice = input("would you like to buy more chips . enter (yes) to buy")
                while choice.lower() == "yes":
                    AddBalance = float(input("How much money would you like to add:"))
                    StartingBalance += AddBalance
                    db.writeFile(StartingBalance)
                    choice = input("Do you want to add again (yes / no)")

        except ValueError:
            print("Enter a valid number ")
            continue
        else:
            return StartingBalance
