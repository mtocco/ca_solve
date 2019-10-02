## Code Abbey
## Website: http://www.codeabbey.com/index/task_view/pythagorean-triples
## Problem #57
## Student: Michael Tocco
##
##
## https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
##
## As we know, the Pythagorean Theorem tells us about the simple equation:
##
## a^2 + b^2 = c^2
## There really exist such triples a, b, c of integer numbers, which satisfy
## this equation. This is not self-evident fact, moreover there are no such
## triples for any other powers except 2 - this is the famous Fermat Theorem
## which could not be solved for more than 350 years.
##
## However, for the power of 2 there are countless amount of such triples.
## One of them 3, 4, 5, for example.
##
## Nevertheless, it is not always easy to find a triple satisfying some specific
## conditions:
##
## In this problem you need to write a program which for given value of
## s = a + b + c will find the only triple which satisfies the equation.
##
## For example, given sum of 12 the only 3, 4, 5 triple fits, for sum 30
## the only 5, 12, 13 etc.
##
## Input data will contain the number of test-cases in the first line.
## Other lines will contain a single value each - the sum for which triple
## should be found.
## Answer should contain the values of c^2 for each triple found (it is
## equal to a^2 + b^2 of course), separated with spaces.
##
## Note: the real values of s would be large enough, about 10e+7 - so the
## simplest solutions could be inefficient.
##
## Example:
## input data:
## 2
## 12
## 30
##
## answer:
## 25 169


def main():
    userArray = []
    print()
    print()
    yesOrNo = input("Would you like proceed with the calculation? (enter[y , n]): ")
    if yesOrNo == "y":
        buildArray()
    else:
        print("Thank you, come again")

## https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples


def buildArray():
    arrayPairs = int(input("Please enter in " + \
                                 "a desired number of sets to analyze"))
    print("Enter/Paste your content. Ctrl-D to save it.")
    answer = ""
    contents = []
    for i in range(int(arrayPairs+1)):
        
        try:
            line = int(input())
            userInt = line
            a = 0
            b = 0
            c = 0
            while a + b + c != line:
                aStart = 1
                bStart = 3
                a = ((aStart * bStart) + aStart)
                b = bStart
                c = a + 1

                                    
            
        


            print(line)
            
        except EOFError:
            break


    
main()
            


