# Welcoming message
print('Welcome to the Love Calculator!')

# input both names
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

# lower the capital letters
name1 = name1.lower()
name2 = name2.lower()

# combine both names into a single string
both_names = name1 + name2

# counting letters of true
times_t = both_names.count('t') 
print(f'T occours {times_t} times.')
times_r = both_names.count('r') 
print(f'R occours {times_r} times.')
times_u = both_names.count('u') 
print(f'U occours {times_u} times.')
times_e = both_names.count('e') 
print(f'E occours {times_e} times.')

# times that these letters occurs in both names
total_true = times_t + times_r + times_u + times_e
print(f'Total = {total_true}')

# counting letter of love
times_l = both_names.count('l') 
print(f'L occours {times_l} times.')
times_o = both_names.count('o') 
print(f'0 occours {times_o} times.')
times_v = both_names.count('v') 
print(f'V occours {times_v} times.')
times_e = both_names.count('e') 
print(f'E occours {times_e} times.')

# times that these letters occurs in both names
total_love = times_l + times_o + times_v + times_e
print(f'Total = {total_love}')

# converting both totals to strings
total_true = str(total_true)
total_love = str(total_love)

# concatenating strings
love_score = total_true + total_love
# converting to integer
love_score = int(love_score)

# if - elif statements
if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif (love_score >= 40) and (love_score <= 50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')