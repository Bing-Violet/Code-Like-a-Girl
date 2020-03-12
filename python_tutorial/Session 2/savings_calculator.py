money_start = input('Enter the money you have now:')

saving_years = input("Enter the years you're going to save:")

interest_rate = input('Enter the interest rate(%):')

money_result = float(money_start) * (1 + float(interest_rate)/100) ** int(saving_years)

print(money_result)