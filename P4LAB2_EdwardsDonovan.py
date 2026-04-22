# Donovan Edwards
# Apr. 21st 2025
# P4LAB2
# Python script for displaying multiplication tables
running = True

while running:
    print("Enter an integer:", end=" ")
    base = int(input())

    print("")

    if base < 0:
        print("Program does not handle negative numbers")
    else:
        for i in range(12):
            multiple = i + 1
            product = base * multiple

            print(base, " * ", multiple, " = ", product)

    print("")

    print("Would you like to run the program again?", end=" ")
    response = input()

    running = response == "yes"
    print("")

print("Exiting program...")
