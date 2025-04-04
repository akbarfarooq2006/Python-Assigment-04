def main():
    try:
        value = int(input('Enter the value which you to double '))
        if value > 100:
            raise ValueError('Value must be less than or equal to 100')
    except ValueError:
        print('\n⚠️ Invalid input. Please enter a positive integer less than or equal to 100.')
        return
    
    print(f'\nThe Double value of {value} is: ')
    while value < 100:
        print(value * 2)
        value *= 2
        


main()