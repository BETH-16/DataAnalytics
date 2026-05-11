savings = float(input("Enter your savings: "))
interest_rate = float(input("Enter interest rate (%): "))

years = 72 / interest_rate
doubled = savings * 2

print("Your current savings is " + str(savings))
print("At a " + str(interest_rate) + "% interest rate, your savings account will be")
print("worth " + format(doubled, ".2f") + " in " + format(years, ".1f") + " years")
# input() always gives a string, so we must convert to numbers
# wrong input (like letters) will crash the program
# dividing by 0 (interest rate = 0) will cause an error
# no checks for correct input from user