# input weight
weight = float(input('Enter your weight in kg: '))
# input height
height = float(input('Enter your height in m: '))

BMI = round(weight/(height**2)) # calculate BMI

if BMI < 18.5:
    print(f'Your BMI is {BMI}, you are underweight.')
elif BMI < 25:
    print(f'Your BMI is {BMI}, you have a normal weight.')
elif BMI < 30:
    print(f' Your BMI is {BMI}, you are overweight.')
elif BMI < 35:
    print(f'Your BMI is {BMI}, you are obese.')
else:
    print(f' Your BMI is {BMI}, you are clinically obese.') 

