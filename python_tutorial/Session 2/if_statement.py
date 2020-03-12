#if statement demo
year = 2020

year_of_birth = input("Enter your year of birth:")

age = year - int(year_of_birth)

if age > 20:
	print('Congratulations! You are an adult!')
else:
	print("You're still young.")