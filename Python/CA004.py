##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/min-of-two
## Problem #4
## Student: Michael Tocco
##
## Minimum of Two
##
##
##
## Most programs should be able to make some choices and decisions. And we are going to practice conditional programming now.
## This is usually done by a kind of if ... else statements which may look like:
##
## IF some_condition THEN
##     do_something
## ELSE
##     do_other_thing
## ENDIF
##
## Depending on your programming language syntax could be different and else part is almost always optional. You can read more in wikipedia article on Conditional statements.
##
## Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.
##
## Input data will contain number of test-cases in the first line.
## Following lines will contain a pair of numbers to compare each.
## For Answer please enter the same amount of minimums separated by space,
##
## for example:
##
## data:
## 3
## 5 3
## 2 8
## 100 15
##
## answer:
## 3 2 15






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
    arrayPairs = int(input("Please enter in " + \
                                 "a desired number of pairs for your array: "))
    print("Enter/Paste your content. Ctrl-D to save it.")
    answer = ""
    contents = []
    for i in range(int(arrayPairs+1)):
        
            try:
                line = input().split(" ")
                if len(line) > 1:
                    intPair = [int(i) for i in line]
                    minimum = [i for i in intPair if i <= intPair[1]]
                    answer = answer + str(minimum[0]) + " "
                    contents.append(line)

                    
            
            
            except EOFError:
                break
            
    print(answer)          



main()
