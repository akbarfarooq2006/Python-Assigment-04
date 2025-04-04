def main():
    
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor 
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder),"\n")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print("\n⚠️ An error occurred:", str(e))
        print("⚠️ Please make sure you entered valid integers.\n")
    