# input weight
weight = input('Enter your weight in kg: ')
# input height
height = input('Enter your height in m: ')

weight = float(weight) # convert weight to float
height = float(height) # convert height to float

BMI = weight/(height**2) # calculate BMI
BMI = int(BMI) # convert BMI to int

print('Your BMI is: ', BMI) # output BMI