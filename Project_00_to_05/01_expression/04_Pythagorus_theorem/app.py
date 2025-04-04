import math 
try:
    perpendicular = int(input('Enter the number of pendicular: '))
    base = int(input('Enter the base number: '))
    hypotenous= math.sqrt(base**2 + perpendicular**2)
    print('Hypotenuse:', hypotenous)
except ValueError:
    print("invalid input")







