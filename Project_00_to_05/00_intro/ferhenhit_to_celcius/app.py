try:
    fahrenhit = int(input("Enter the value of Fahrenheit: "))
    celsius = (fahrenhit - 32) * 5/9
    print("The value of Celsius is: ", round(celsius, 2))
except ValueError:
    print("Invalid input. Please enter a number.")