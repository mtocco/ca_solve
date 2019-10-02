## Code Abbey
## Sum in Loop
##
## Problem #2 
##
## demo of summing an array
##
## Now our goal is to learn the loops - i.e. repeated actions. Let us find the sum of several numbers (more than two). It will be useful to do this in a loop. As shown in the picture above - you can create variable sum and add every value from the list to it. Perhaps "for" loop will suit nicely since the amount of numbers is known beforehand.
##
## If you have troubles, try Sums In Loop first - it is, probably, easier.
##
## Input data has the following format:
##
##    first line contains N - amount of values to sum;
##    second line contains N values themselves.
##
## Answer should contain a single value - the sum of N values.
##
## Example:
## input data:
## 8
## 10 20 30 40 5 6 7 8
##
## answer:
## 126

def main():
    
    print()
    print()
    yesOrNo = input("Would you like proceed with the calculation? (enter[y , n]): ")

    if yesOrNo == "y":
        buildArray()
    else:
        print("Thank you, come again")


def buildArray():

    arrayLength = int(input("Please enter in " + \
                                 "a desired length for your array: "))

    stringToArray = input("Please enter in " + \
                                 "a desired string of numbers " + \
                          "separated by a space: \n")

    listOfNumb = stringToArray.split(" ")
    
    userArray = [0] * arrayLength

    for i in range(arrayLength):
            intIndex = int(listOfNumb[i])
            userArray[i] = intIndex
    print(sum(userArray))
            

               
main()
