## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/median-of-three
## Problem #41
## Student: Michael Tocco
##
## 
## 
## Median of Three
##
##
## You probably already solved the problem Minimum of Three - and it was
## not great puzzle for you? Since programmers should improve their logic
## (and not only skills in programming language), let us change the task to
## make it more tricky.
##
## You will be again given triplets of numbers, but now the middle of them
## should be chosen - i.e. not the largest and not the smallest one. Such number
## is called the Median (of the set, array etc).
##
## Be sure, this problem is not simply "another stupid exercise" - it is used
## as a part in powerful QuickSort algorithm, for example.
##
## Input data will contain in the first line the number of triplets to follow.
## Next lines will contain one triplet each.
## Answer should contain selected medians of triplets, separated by spaces.
##
## Example:
## data:
## 3
## 7 3 5
## 15 20 40
## 300 550 137
##
## answer:
## 5 20 300
## Note: if your program will have a lot of if-else-if-else statements, then you
## are probably doing something wrong. Simple solution should have no more
## than three of them.
##


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
                    intSet = [int(i) for i in line]
                    median = [i for i in intSet if i != min(intSet) and i != max(intSet)]                    

                    answer = answer + str(median).replace("[","").replace("]","") + " "
                    
            except EOFError:
                break
            
    print(answer)          



main()

## The result was correct - the author listed some notes as well:
##
## Author's Notes
## To select the middle of three elements A, B and C let us try to reorder them:
##
## if A > B swap A with B
## if B > C swap B with C
## if A > B swap A with B
## For swapping X and Y use the temporary variable T in three assignment,
## for example:
##
## T = X; X = Y; Y = T
##
## At the 2nd step the largest element of three would be moved to C.
## After 3rd step the smallest of the remaining two is moved to A.
## Therefore B contains the middle element.






