dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 
                'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries',
                'Pears', 'Tomatoes', 'Celery', 'Potatoes']

# creating lists inside lists

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes',
          'Peaches', 'Cherries', 'Pears']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

# instead of creating the full dirty dozen list, it's possible to do:

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][3])