# Donovan Edwards
# Nov. 4th 2025
# P2HW2
# Python script for calculating stats relating to grades for modules

gradeList = []

print("Enter grade for Module 1:", end=" ")
gradeList.append(float(input()))
print("Enter grade for Module 2:", end=" ")
gradeList.append(float(input()))
print("Enter grade for Module 3:", end=" ")
gradeList.append(float(input()))
print("Enter grade for Module 4:", end=" ")
gradeList.append(float(input()))
print("Enter grade for Module 5:", end=" ")
gradeList.append(float(input()))
print("Enter grade for Module 6:", end=" ")
gradeList.append(float(input()))

lowestGrade = min(gradeList)
highestGrade = max(gradeList)
sumOfGrades = sum(gradeList)
avgOfGrades = sumOfGrades / len(gradeList)

print("-------------------Results-------------------", end="\n")
print(f"Lowest Grade:          {lowestGrade:.1f}", end="\n")
print(f"Highest Grade:         {highestGrade:.1f}", end="\n")
print(f"Sum of Grades:         {sumOfGrades:.1f}", end="\n")
print(f"Average:               {avgOfGrades:.2f}", end="\n")
print("---------------------------------------------", end="\n")