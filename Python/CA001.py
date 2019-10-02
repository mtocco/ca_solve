




print("_______________________________________________________________________________")
print("This program calculates the Sum of two numbers")
print()
print("This is my answer to problem 1 on CodeAbbey.com")
print("_______________________________________________________________________________")
print()
print()


def main():
    yesOrNo = input("Would you like to proceed with the calculation?: [y , n]")

    if yesOrNo == "y":
        a = float(input("please enter a number: "))
        b = float(input("please enter a second number: "))
        
        calculateSum(a, b)

    else:
        print("Thank you come again")




def calculateSum(a, b):
    firstNum = a
    secondNum = b

    print(firstNum + secondNum)

    
    
main()
