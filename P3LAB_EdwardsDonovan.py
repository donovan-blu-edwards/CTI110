# Donovan Edwards
# Nov. 4th 2025
# P3LAB
# Python script for calculating money amount as change
# curse floating point numbers forever

inputtedMoney = int(float(input("Enter amount of money as a float: $")) * 100)

dollarCount = int(inputtedMoney // 100)
if dollarCount > 0:
    inputtedMoney -= (100 * dollarCount)
    print(dollarCount, "Dollars")

quarterCount = int(inputtedMoney // 25)
if quarterCount > 0:
    inputtedMoney -= (25 * quarterCount)
    print(quarterCount, "Quarters")

dimeCount = int(inputtedMoney // 10)
if dimeCount > 0:
    inputtedMoney -= (10 * dimeCount)
    print(dimeCount, "Dimes")

nickelCount = int(inputtedMoney // 5)
if nickelCount > 0:
    inputtedMoney -= (5 * nickelCount)
    print(nickelCount, "Nickels")

pennyCount = int(inputtedMoney // 1)
if pennyCount > 0:
    print(pennyCount, "Pennies")