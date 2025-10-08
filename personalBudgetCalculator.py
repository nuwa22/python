userName = input("Enter your name: ")
monthlyIncome = float(input("Enter your monthly income: "))
expensesCategories = int(input("Enter number of expense categories: "))
expensesList = []

# Input expense categories and amounts
for i in range(expensesCategories):
    category = input(f"Enter name of category {i + 1}: ")
    amount = float(input(f"Enter amount for {category}(in Rs): "))
    tuple = (category, amount)
    expensesList.append(tuple)

dictforSummary = {}

# Calculate total expenses and savings
totalExpenses = 0
for item in expensesList:
    amount = item[1]
    totalExpenses += amount

savings = monthlyIncome - totalExpenses

# add dict for summary
dictforSummary["Name"] = userName
dictforSummary["Monthly Income (in Rs)"] = monthlyIncome
dictforSummary["Total Expenses (in Rs)"] = totalExpenses
dictforSummary["Savings (in Rs)"] = savings

print("\n")
print(f"Welcome, {userName}! Let's calculate your monthly budget.\n....................................................")
print(f"=== Budget Summary for {userName} ===")

print("Monthly Income (in Rs):", dictforSummary["Monthly Income (in Rs)"])
print("Total Expenses (in Rs):", dictforSummary["Total Expenses (in Rs)"])
print("\n")

print("Expense Breakdown:")
for item in expensesList:
    print(f"- {item[0]}: Rs {item[1]} ({(item[1]/monthlyIncome)*100:.2f}%)")
print("\n")

print("Financial Status:")
if savings > 0:
    print(f"Great! You have a surplus of Rs {savings:.2f} this month.({savings/monthlyIncome*100:.2f}%)")
elif savings < 0:
    print(f"Alert! You have a deficit of Rs {-savings:.2f} this month.({-savings/monthlyIncome*100:.2f}%)")
else:
    print("You have balanced your budget exactly this month.(0.00%)")
print("\n")

print("Budget Tip: Track Your Expenses Weekly")
print("\n")

print("Budget Analysis Stored:")
print(f"Name: {dictforSummary['Name']}")
print(f"Monthly Income (in Rs): {dictforSummary['Monthly Income (in Rs)']}")
print(f"Total Expenses (in Rs): {dictforSummary['Total Expenses (in Rs)']}")
print(f"Savings (in Rs): {dictforSummary['Savings (in Rs)']}")
print("Thank you for using the Personal Budget Calculator!")

