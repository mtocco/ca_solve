####################################################################
####################################################################
# Problem #19                                                      #
# Matching Brackets                                                #
# Student: Michael Tocco                                           #
# URL: https://www.codeabbey.com/index/task_view/matching-brackets #
####################################################################
####################################################################
#                                                                  #
#                                                                  #
# We are given strings containing brackets of 4 types - round (),  #
# square [], curly {} and angle <> ones. The goal is to check,     #
# whether brackets are in correct sequence. I.e. any opening       #
# bracket should have closing bracket of the same type somewhere   #
# further by the string,                                           #
# and bracket pairs should not overlap, though they could          #
# be nested:                                                       #
#                                                                  #
# (a+[b*c] - {d/3})  - here square and curly brackets are nested   #
# in the round ones                                                #
# (a+[b*c) - 17]     - here square brackets overlap with round     #
# ones which does not make sense                                   #
#                                                                  #
# Input data will contain number of testcases in the first line.   #
# Then specified number of lines will follow each containing a     #
# test-case in form of a character sequence. Answer should contain #
# 1 (if bracket order is correct) or 0 (if incorrect) for each of  #
# test-cases, separated by spaces.                                 #
#                                                                  #
# Example:                                                         #
#                                                                  #
# input data:                                                      #
# 4                                                                #
# (a+[b*c]-{d/3})                                                  #
# (a + [b * c) - 17]                                               #
# (((a * x) + [b] * y) + c                                         #
# auf(zlo)men [gy<psy>] four{s}                                    #
#                                                                  #
# answer:                                                          #
# 1 0 0 1                                                          #
####################################################################


def main():
    file1 = open("test1.txt","r")
    file1.readline()
    array = file1.readlines()
    answer = ""
    for i in array:
        answer = answer + testBalance(i) + " "
        testBalance(i)
    print(answer)
    
def testBalance(statement):
    stack = ["good"]
    for i in range(len(statement)):
        if(statement[i] == "(" or statement[i] == "["
           or statement[i] == "{" or statement[i] == "<"):
            stack.append(statement[i])
        if(statement[i] == ")" and stack[-1] == "good"):
            return("0")
        if(statement[i] == "]" and stack[-1] == "good"):
            return("0")
        if(statement[i] == "}" and stack[-1] == "good"):
            return("0")
        if(statement[i] == ">" and stack[-1] == "good"):
            return("0")        
        if(statement[i] == ")" and stack[-1] == "("):
            stack.pop()
        if(statement[i] == "]" and stack[-1] == "["):
            stack.pop()
        if(statement[i] == "}" and stack[-1] == "{"):
            stack.pop()
        if(statement[i] == ">" and stack[-1] == "<"):
            stack.pop()
            
    if(stack[-1] != "good"):
        return("0")
    else:
        return("1")
main()





