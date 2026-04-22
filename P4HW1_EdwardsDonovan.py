# Donovan Edwards
# Apr. 21st 2026
# P4HW1
# Python script for calculating stats relating to grades for modules

scoreList = []

print("How many scores do you want to enter?", end=" ")
scoreCount = int(input())

while len(scoreList) < scoreCount:
    i = len(scoreList)
    scoreNum = i + 1
    print("Enter score for score #", scoreNum, ": ", end=" ")
    thisScore = float(input())

    if thisScore < 0 or thisScore > 100:
        print("INVALID Score entered !!!")
        print("Score must be between 0 and 100")
    else:
        scoreList.append(thisScore)

lowestGrade = min(scoreList)
highestGrade = max(scoreList)

modifiedGrades = scoreList.copy()
modifiedGrades.remove(lowestGrade)
sumOfGrades = sum(modifiedGrades)
avgOfGrades = sumOfGrades / len(modifiedGrades)

letterGrades = ["A", "B", "C", "D", "F"]
letterGrade = "A"
for i in range(5):
    criteria = 100 - (i + 1) * 10
    letterGrade = letterGrades[i]
    if avgOfGrades >= criteria:
        break

print("-------------------Results-------------------", end="\n")
print(f"Lowest Grade:          {lowestGrade:.1f}", end="\n")
print(f"Modified List:         {modifiedGrades}", end="\n")
print(f"Scores Average:        {avgOfGrades:.2f}", end="\n")
print(f"Grade:                 {letterGrade}", end="\n")
print("---------------------------------------------", end="\n")
