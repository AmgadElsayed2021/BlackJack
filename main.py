import db
import win
import cards
import BalanceCheck as Bc
import game as g

def main():
    house = []
    player = []
    print('Black Jack!\nBlack jack payout is 3:2\n')
    StartingBalance = db.readFile()
    print(f'money: {StartingBalance} $')
    StartingBalance = Bc.CheckBalance()

    if StartingBalance >= 5:
        playGame = str(input("\nwould you like to start the game (yes/no)"))
        while playGame.lower() == "yes":
            house.clear()
            player.clear()
            # StartingBalance = db.readFile()
            BetAmount = Bc.GetBetAmount()
            deck = cards.shuffleDeck()
            g.GameStart(deck , house, player)
            g.hitLoop(deck, player)
            g.stand(deck, house, player)
            win.BlackJack(house, player)
            cards.displayTotalPoints(house, player)
            win.BetWinOrLose(player, house, BetAmount)
            Bc.CheckBalance()

            playGame = str(input("\nwould you like to play another game (yes/no)"))
        print("\nBye!")

if __name__ == "__main__":
    main()