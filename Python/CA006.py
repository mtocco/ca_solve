##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/rounding
## Problem #6
## Student: Michael Tocco
##
##
##
## When program deals with numbers which have fraction part we sometimes want
## to round such values to whole integer. We'll need this for programming some
## later problems (to make answers simpler, for example), so let us have the
## following dedicated exercise to learn this trick.
##
## There are several pairs of numbers. For each pair you are to divide first
## by second and return the result, rounded to the nearest integer.
##
## In cases, when result cÍontains exactly 0.5 as a fraction part, value
## should be rounded up (i.e. by adding another 0.5). Note that for negative values "greater" means "closer to zero". Refer to the Wikipedia page on Rounding for more thorough explanations.
##
## In any further problems, when rounding is mentioned - just the
## same rounding algorithm is supposed (unless other is explicitly specified).
##
## Input data will give a number of test-cases in the first line.
## Next lines will contain one test-case (i.e. the pair of numbers) each.
## Answer should contain division-and-rounding results for each pair,
## separated with spaces
##
## Example:
## input data:
## 3
## 12 8
## 11 -3
## 400 5
##
## answer:
## 2 -4 80


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
        print(math.sqrt(4))




def buildArray():
    
    arrayPairs = int(input("Please enter in " + \
                                 "a desired number of pairs for your array: "))
    print("Enter/Paste your content. Ctrl-D to save it.")
    answer = ""
    contents = []
    for i in range(int(arrayPairs+1)):
        
            try:
                line = input().split(" ")
                if len(line) > 1:
                    intPair = [int(i) for i in line] #List comprehension for string to int
                    quotient = round(intPair[0] / intPair[1]) #rounds the quotient
                    answer = answer + str(quotient) + " " #preps for output
                    contents.append(answer) #appends to answer
                
            except EOFError:
                break
            
    print(answer) 


main()
