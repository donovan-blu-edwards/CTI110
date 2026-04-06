# Donovan Edwards
# Nov. 4th 2025
# P3HW2
# This program prompts the user about information about their employment and hours work to display stats and pay

employeeName = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

overTimeHours = 0 if hoursWorked <= 40 else (hoursWorked - 40)
overTimePay = (overTimeHours * payRate) * 1.5

regHourPay = ((hoursWorked - overTimeHours) * payRate)
grossPay = overTimePay + regHourPay

print("-----------------------------------------------")

print("Employee Name: ", employeeName, end="\n\n")

print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}Gross Pay")
print(f"{hoursWorked:<20.1f}{payRate:<20.2f}{overTimeHours:<20.1f}{overTimePay:<20.2f}${regHourPay:<19.2f}${grossPay:.2f}")