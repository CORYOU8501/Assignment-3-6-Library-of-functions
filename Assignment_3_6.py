
def functionOne():
    print("My Student ID is coryou8501")


def functionTwo():
    firstNumber = int(input("Please enter a number: "))
    secondNumber = int(input("Please enter a number: "))
    sumValue = firstNumber + secondNumber
    print(f"The sum of {firstNumber} and {secondNumber} is {sumValue}.")
    return sumValue


def functionThree(sumValue):
    if sumValue > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 8501


def main():
    functionOne()  # Calls the first function to display my student ID.
    sumValue = functionTwo()  # Gets the sum of the two numbers entered.
    studentNumber = functionThree(sumValue)  # Checks the sum and gets my ID number.
    print(f"functionThree returned the value of {studentNumber}.")  # Displays the returned ID number.


if __name__ == "__main__":
    main()
