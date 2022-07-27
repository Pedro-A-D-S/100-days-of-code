# inpute message
ageInYears = input('What is your current age? ')

timeLeftInYears = 90 - int(ageInYears) # time remaining

timeLeftInDays = timeLeftInYears * 365 # time in days
timeLeftInWeeks = timeLeftInYears * 52 # time in years
timeLeftInMonths = timeLeftInYears * 12 # time in months

# output message
print(f'You have {timeLeftInDays} days, {timeLeftInWeeks} weeks and {timeLeftInMonths} months left.')