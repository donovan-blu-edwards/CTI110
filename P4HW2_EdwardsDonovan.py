# Donovan Edwards
# Apr. 21st 2026
# P4HW2
# This program prompts the user about information about multiple employee's hours and pay rates to display stats

employeeCount = 0
totalRegularPay = 0.0
totalOvertimePay = 0.0
totalPay = 0.0

while True:
    employeeName = input('Enter employee\'s name or type "Done" to terminate: ')

    if employeeName == "Done":
        break

    employeeCount += 1

    hoursWorked = float(input(f"How many hours did {employeeName} work? "))
    payRate = float(input(f"What is {employeeName}'s pay rate? "))

    overTimeHours = 0 if hoursWorked <= 40 else (hoursWorked - 40)
    overTimePay = (overTimeHours * payRate) * 1.5
    totalOvertimePay += overTimePay

    regHourPay = (hoursWorked - overTimeHours) * payRate
    totalRegularPay += regHourPay
    grossPay = overTimePay + regHourPay
    totalPay += grossPay

    print("")
    print("Employee Name: ", employeeName, end="\n\n")

    print(
        f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}Gross Pay"
    )

    print(
        "-------------------------------------------------------------------------------------------------------------"
    )

    print(
        f"{hoursWorked:<20.1f}{payRate:<20.2f}{overTimeHours:<20.1f}{overTimePay:<20.2f}${regHourPay:<19.2f}${grossPay:.2f}",
        end="\n\n",
    )

print("")

print("Total number of employees entered: ", employeeCount)
print(f"Total amount paid for overtime: ${totalOvertimePay:.2f}")
print(f"Total amount paid for regular hours: ${totalRegularPay:.2f}")
print(f"Total amount paid in gross: ${totalPay:.2f}")
