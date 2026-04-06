# Donovan Edwards
# Nov. 4th 2025
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
sumOfGrades = sum(grades)
avg = (sumOfGrades / len(grades))

print("-------------------Results-------------------", end="\n")
print(f"Lowest Grade:          {low:.1f}", end="\n")
print(f"Highest Grade:         {high:.1f}", end="\n")
print(f"Sum of Grades:         {sumOfGrades:.1f}", end="\n")
print(f"Average:               {avg:.2f}", end="\n")
print("---------------------------------------------", end="\n")

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
else:
    print('Your grade is: F')