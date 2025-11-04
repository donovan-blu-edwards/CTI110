# Donovan Edwards
# Oct. 14th 2025
# P1HW2
# Python script for calculating expenses based on a travel plan

print("This program calculates and displays travel expenses", end=" ")

print("\n\nEnter budget:", end=" ")
totalBudget = int(input())

print("\n\nEnter your travel destination:", end=" ")
location = input()

print("\n\nHow much do you think you will spend on gas?", end=" ")
costGas = int(input())

print("\n\nApproximately, how much will you need for accomodation/hotel?", end=" ")
costLodging = int(input())

print("\n\nLast, how much do you need for food?", end=" ")
costFood = int(input())

remainingBudget = totalBudget - costGas - costLodging - costFood # Kind of redundant because you could just do the calculation on the print call but whateverr

print("------------Travel Expenses------------", end="\n")
print("Location:", location, end="\n")
print("Initial Budget:", totalBudget, end="\n\n")

print("Fuel:", costGas, end="\n")
print("Accomodation:", costLodging, end="\n")
print("Food:", costFood, end="\n\n")
print("Remaining Balance:", remainingBudget)