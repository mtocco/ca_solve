##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/triangles
## Problem #9
## Student: Michael Tocco
##
## 
## Triangles
##
##
## Triangle is an object built of three line segments (sides of triangle),
## connected by ends. Wiki on triangles provides more detailed explanation.
## If we have three line segments with lengths A B C - we either can built
## a triangle with them
##
## (for example with 3 4 5 or 3 4 7 - though this is with zero area)
## or we found it impossible
##
## (for example 1 2 4).
##
## You are given several triplets of values representing lengths of the sides
## of triangles. You should tell from which triplets it is possible to build
## triangle and for which it is not.
##
## Input data: First line will contain number of triplets.
## Other lines will contain triplets themselves (each in separate line).
## Answer: You should output 1 or 0 for each triplet
## (1 if triangle could be built and 0 otherwise).
##
## Example:
##    
## data:
## 2
## 3 4 5
## 1 2 4
##
## answer:
## 1 0



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
                toggle = 1
                if len(line) > 1:
                    intPair = [int(i) for i in line]
                    if int(line[0]) + int(line[1]) < int(line[2]) or \
                       int(line[0]) + int(line[2]) < int(line[1]) or \
                       int(line[1]) + int(line[2]) < int(line[0]):
                        toggle = 0
                        answer = (answer + str(toggle) + " ")
                    else:
                        answer = (answer + str(toggle) + " ")

                    
            except EOFError:
                break
            
    print(answer)          



main()
