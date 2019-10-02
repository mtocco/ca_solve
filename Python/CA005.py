##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/min-of-three
## Problem #5
## Student: Michael Tocco
##
## Minimum of Three
##
##
##
## To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. one if ... else statement could be (and should be) nested inside other to solve this problem.
##
## Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.
##
## Input data will contain in the first line the number of triplets to follow.
## Next lines will contain one triplet each.
## Answer should contain selected minimums of triplets, separated by spaces.
##
## Example:
## data:
## 3
## 7 3 5
## 15 20 40
## 300 550 137
##
## answer:
## 3 15 137


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
                                 "a desired number of sets to analyze"))
    print("Enter/Paste your content. Ctrl-D to save it.")
    answer = ""
    contents = []
     
    for i in range(int(arrayPairs+1)):       
            try:
                line = input().split(" ")
                if len(line) > 1:
                    intPair = [int(i) for i in line]
                    minimum = [i for i in intPair if i <= intPair[1] and i <= intPair[2]]
                    answer = answer + str(minimum[0]) + " "
                    contents.append(line)
                    
            except EOFError:
                break
            
    print(answer)          



main()
