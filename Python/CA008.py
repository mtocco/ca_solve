##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/arithmetic-progression
## Problem #8
## Student: Michael Tocco
##
##
## When we speak about arithmetic progression (or arithmetic sequence) we mean
## a series of numbers with a special property - each value is followed by
## the other, greater by predefined amount (step).
##
## I.e. difference of (K+1)-th and K-th values is a constant.
## Here are examples of sequences
##
## 1 2 3 4 5 6 7 ...
## 4 6 8 10 12 14 16...
## 10 13 16 19 22 25 28...
##
## Since so, arithmetic sequence is completely defined by the first member
## (A) and the increment value - step size -
## (B). First few members could be expressed as
##
## A + (A + B) + (A + 2B) + (A + 3B) + ...
##
## You are to calculate the sum of first members of arithmetic sequence.
## Wikipedia page on arithmetic progression could be of significant help to
## one who meets them for the first time.
##
## Input data: first line contains the number of test-cases.
## Other lines contain test-cases in form of triplets of values A B N where
## A is the first value of the sequence, B is the step size and N is the
## number of first values which should be accounted.
##
## Answer: you are to output results (sums of N first members) for each sequence,
## separated by spaces.
##
## Example:
## data:
## 2
##
## answer:
## 21 30
##
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
    
    arrayPairs = int(input("Please enter in " + \
                                 "a desired number of sets to analyze"))
    print("Enter/Paste your content. Ctrl-D to save it.")
    answer = ""
    contents = []
    c = 0
    for i in range(int(arrayPairs+1)):       
            try:
                line = input().split(" ")
                if len(line) > 1:
                    c = 0
                    solution = 0
                    a = int(line[0])
                    b = int(line[1])
                    for i in range(int(line[2])):
                        solution = solution + (a + (b*c))
                        c = c + 1
                    answer = (answer + str(solution) + " ") #adds to full answer in code abbey format
                       

                    

                    
            except EOFError:
                break

    print(answer)




main()
