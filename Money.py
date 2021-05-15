from openpyxl import Workbook
import pandas as pd
import numpy
import os
os.system("close")

workbook = Workbook()
sheet = workbook.active

coin = input("Enter your coin(Example:Euro) ")
def coins():
    if coin == 'Euro':
        Euros = 'euro'
    elif coin == 'Dollars':
        Dollars = 'dollars'
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
df1 = pd.DataFrame({"D":[money]}, 
                    index =["D1"])
df2 = pd.DataFrame({"D":[spent]}, 
                    index =["D1"])
df1.subtract(df2)
sheet["A1"] = "Coin"
sheet["B1"] = "Money"
sheet["C1"] = "Spent"
sheet["D1"] = "Total"
sheet["E1"] = "Date"

sheet["A2"] = coin
sheet["B2"] = money
sheet["C2"] = spent
sheet["E2"] = date

workbook.save(filename="Money.xlsx")

