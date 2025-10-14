# Donovan Edwards
# Oct. 14th 2025
# P1HW1
# Python script that prompts the user number values to do different calculations

print("-----Calculating Exponents-----", end="\n\n")
print("Enter an integer as the base value:", end=" ")
expoBase = int(input())
print("Enter an integer as the exponent:", end=" ")
expoExpo = int(input())

expoResult = expoBase ** expoExpo
print("\n\n", expoBase, "raised to the power of", expoExpo, "is", expoResult, "!!")

print("\n\n-----Addition and Subtraction-----", end="\n\n")
print("Enter a starting integer:", end=" ")
addsubStart = int(input())
print("Enter an integer to add:", end=" ")
addsubAdd = int(input())
print("Enter an integer to subtract:", end=" ")
addsubSub = int(input())

addsubResult = addsubStart + addsubAdd - addsubSub
print("\n\n", addsubStart, "+", addsubAdd, "-", addsubSub, "is equal to", addsubResult)
