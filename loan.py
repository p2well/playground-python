# Get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n"))  # $50,000
apr = float(input("What is the annual percentage rate?\n"))  # 3%
payment = float(input("What will your monthly payment be, in dollars?\n"))  # $1,000
months = int(input("How many months do you want to see results for?\n"))  # 24

monthly_rate = apr / 100 / 12

for i in range(months):
    # Calculate the interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment) < 0:
        print(f"The last payment is {money_owed}")
        print("You paid off the loan in", i+1, "months")
        break

    # Make payment
    money_owed = money_owed - payment

    print(f"Paid ${payment} of which ${interest_paid} was interest. Now I owe ${money_owed}.")
