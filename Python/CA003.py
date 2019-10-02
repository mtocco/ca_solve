##
##
## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/sums-in-loop
##
## Problem #3
## Student: Michael Tocco
##
## Summing two arrays
##
##
## If you already learned how to write program with a simple loop from Sum in Loop task, this new exercise will be just a simple modification.
##
## Now we are given several pairs of values and we want to calculate sum for each pair.
##
## Input data will contain the total count of pairs to process in the first line.
## The following lines will contain pairs themselves - one pair at each line.
## Answer should contain the results separated by spaces.
##
## Example:
##
## Data:
## 3
## 100 8
## 15 245
## 1945 54
##
## Answer:
## 108 260 1999

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
    for i in range(14):
        
            try:
                line = input().split(" ")
                if len(line) > 1:
                    intPair = [int(i) for i in line]
                    sumPair = sum(intPair)
                    answer = answer + str(sumPair) + " "
                    contents.append(line)
            
            
            except EOFError:
                break
            
    print(answer)          



main()
