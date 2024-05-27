# input statements
salary = float(input("What is your current salary? "))
numDependents = float(input("How many dependents do you have? "))

# calculate taxes here
stateTax = round((salary * 0.065),2)
federalTax = round((salary * 0.28),2)
dependentDeduction = round((salary * (0.025 * numDependents)),2)
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: " + str(stateTax))
print("Federal Tax: " + str(federalTax))
print("Dependents: " + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
