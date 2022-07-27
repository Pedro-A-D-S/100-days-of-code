# len(4832) generates an error because the en function doesn't work with numbers

num_char = len(input('What\'s your name?\n')) 
new_num_char = str(num_char) # converting integer to string
print('Your name has ' + new_num_char + ' characters.')

print(type(num_char))

a = str(123)
a = float(123)
print(type(a))

print(70 + float('100.5')) # print the sum
print(str(70) + str(100)) # print the concatenated strings


