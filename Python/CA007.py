##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/fahrenheit-celsius
## Problem #7
## Student: Michael Tocco
##
##
##
## This programming exercise is roughly the same as counting sums in loop, but it needs bit more calculations.
##
## fahrenheit and celsius
## Note: the problem Rounding explains the rounding algorithm which is used in this task.
##
## There are two widespread systems of measuring temperature - Celsius and Fahrenheit. First is quite popular in Europe and second is well in use in United States for example.
##
## By Celsius scale water freezes at 0 degrees and boils at 100 degrees. By Fahrenheit water freezes at 32 degrees and boils at 212 degrees. You may learn more from wikipedia on Fahrenheit. Use these two points for conversion of other temperatures.
##
## You are to write program to convert degrees of Fahrenheit to Celsius.
##
## Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
## Answer should contain exactly N results, rounded to nearest integer and separated by spaces.
##
## Example:
## data:
## 5 495 353 168 -39 22
## answer:
## 257 178 76 -39 -6
##


import math 
def main():
    userArray = []
    print()
    print()
    yesOrNo = input("Would you like proceed with the calculation? (enter[y , n]): ")
    if yesOrNo == "y":
        buildArray()
    else:
        print("Thank you, come again")




def buildArray():
    
    numberList = input("Please enter in " + \
                      "a list of numbers to connvert separated by a space: ")
    answer = ""
    contents = numberList.split(" ") #Splits the list by space
    listLen = len(contents) #determines length of list
    numberOfTemps = contents[0]
    
    
    for i in range(listLen):
        if i > 0:
            farInt = int(contents[i]) #converts string to int
            celInt = round(((farInt - 32)*5)/9) #performs Formula Conversion
            answer = answer + str(celInt) + " " #adds to full answer in code abby format
    print(answer)




main()
