from numpy import size


print('Welcome to Python Pizza Deliveries!')

# small_pizza = $15
# medium_pizza = $20
# large_pizza = $20

# pepperoni_for_small_pizza = + $2
# pepperoni_for_medium_or_large_pizza = + $3
# extra_cheese_for_any_size_pizza = + $1

size = input('What size pizza do you want? S, M or L ')
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is ${bill}.')

