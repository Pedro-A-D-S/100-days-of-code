# elif statement:

print('Welcome to the rollercoaster!')
height = int(input('Enter your height in cm: '))

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('Enter your age: '))
    if age < 12:
        print('Please pay $5.')
    elif age <= 18:
        print('Please pay $7.')
    elif age < 22:
        print('Please pay $9.')
    else:
        print('Please pay $12.')
else:
    print('You can\'t ride the rollercoaster!') 