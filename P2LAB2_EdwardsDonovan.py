# Donovan Edwards
# Apr. 9th 2025
# P2LAB2
# Python script that stores cars' MPG in a dictionary and tells how many gallon need to drive a distance

carsDict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110.0,
    "Silverado": 26.0,
}

# well i gotta leave the pun
carKeys = carsDict.keys()

print("Enter a vehicle to see it's MPG:", end=" ")
carName = input()

print("The", carName, "gets", carsDict[carName], "MPG")

print("How many miles will you drive the", carName, "?", end=" ")
desiredMiles = float(input())

neededGallons = desiredMiles / carsDict[carName]

print(
    f"{neededGallons:.2f}",
    "gallon(s) of gas are needed to drive the",
    carName,
    desiredMiles,
    "miles",
)
