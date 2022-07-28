print('Welcome to the leap year calculator!')
year = int(input('Enter the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The {year} is a leap year')
        else:
            print(f'the {year} is not a leap year.')
    else:
        print(f'the {year} is a leap year.')
else:
    print(f'the {year} is not a leap year.')