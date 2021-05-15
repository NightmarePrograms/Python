from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

coin = input("Enter your ISO(Example:EUR, USD) ")
def coins():
    if (coin == 'EUR'):
        EUR = 'eur'
    elif (coin == 'USD'):
        USD = 'usd'
    elif (coin == 'JPY'):
        JPY = 'jpy'
    elif (coin == 'HRK'):
        HRK = 'hrk'
    elif (coin == 'GBP'):
        GBP = 'gbp'
    elif (coin == 'KM'):
        KM = 'km'
    elif (coin == 'CAD'):
        CAD = 'cad'
    print("So your coin is " + coin)
money = input("Enter your money ")
def moneys():
    print(money)
    print("You have " + money + " " + coin)
spent = input("How much have you spent today ")
def spents():
    print(spent)
date = input("Enter the date(Example:4.6.2021) ")
def dates():
    print("Ok so the date is " + date)

coins()
moneys()
spents()
dates()

sheet["A1"] = "Coin"
sheet["B1"] = "Money"
sheet["C1"] = "Spent"
sheet["E1"] = "Date"

sheet["A2"] = coin
sheet["B2"] = money
sheet["C2"] = spent
sheet["E2"] = date

workbook.save(filename="Money.xlsx")

