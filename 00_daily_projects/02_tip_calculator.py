print('Welcome to the tip calculator!')

bill = input('What was the total bill? ')

percentage = input('What percentage tip would you like to give? 10, 12 or 15? ')

numberPeople = input('How many people to split the bill? ')

percentage = int(percentage)
bill = bill[1:]
bill = float(bill)
numberPeople = int(numberPeople)

payment = (bill + (bill * (percentage / 100))) / numberPeople
payment = round(payment, 2)

print(f'Each person should pay ${payment}.')