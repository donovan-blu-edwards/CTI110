# Donovan Edwards
# Apr. 9th 2025
# P2HW1
# Python script for calculating expenses based on a travel plan

print("This program calculates and displays travel expenses", end=" ")

print("\n\nEnter budget:", end=" ")
totalBudget = float(input())

print("\n\nEnter your travel destination:", end=" ")
location = input()

print("\n\nHow much do you think you will spend on gas?", end=" ")
costGas = float(input())

print("\n\nApproximately, how much will you need for accomodation/hotel?", end=" ")
costLodging = float(input())

print("\n\nLast, how much do you need for food?", end=" ")
costFood = float(input())

remainingBudget = totalBudget - costGas - costLodging - costFood

print("------------Travel Expenses------------", end="\n")
print("Location:              ", location, end="\n")
print(f"Initial Budget:         ${totalBudget:.2f}", end="\n")
print(f"Fuel:                   ${costGas:.2f}", end="\n")
print(f"Accomodation:           ${costLodging:.2f}", end="\n")
print(f"Food:                   ${costFood:.2f}", end="\n")
print("---------------------------------------", end="\n\n")
print(f"Remaining Balance:      ${remainingBudget:.2f}")
