# input names and tell who's going to pay the bill
import random

names_string = input('Give me everybody\'s names separated by a comma. ')

names = names_string.split(',')

person = random.randint(0, len(names) - 1)

print(f'{names[person]} is going to buy the meal today!')
