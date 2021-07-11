import csv
import sys

def readFile():
    try:
        file = open("money.txt", "r")
        try:
            line = float(file.readline())
            return line
        except FileNotFoundError:
            print(f'money: {0} $')
            return 0
        except OSError:
            return 0
        finally:
            file.close()
    except OSError :
        return 0

def writeFile(Balance):
    try:
        with open("money.txt", "w", newline="") as file:
            file.write(str(Balance))
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print(type(e), e)
