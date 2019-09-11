###########################################################################
#                                                                         #
#         NOTE THAT THE PROBLEM SETS CAN BE FOUND ON CODE ABBEY           #
#                                                                         #
#                                                                         #
###########################################################################
######################## Code Abbey Problem 47 ############################
###########################################################################
#                                                                         #
# URL:                                                                    #
# https://www.codeabbey.com/index/task_view/caesar-shift-cipher           #
#                                                                         #
# Author: Michael Tocco                                                   #
# Date Completed: 09/09/19                                                #
#                                                                         #
# Cryptography is one of most interesting branches of programming.        #
# Studying its algorithms usually begins with the simple method.          #
# named after famous Roman emperor Julius Caesar who used it for          #
# communicating his military secrets.                                     #
#                                                                         #
# We will practice deciphering encrypted messages in this problem.        #
#                                                                         #
# The idea of the algorithm is simple.                                    #
# Each letter of the original text is substituted by another, by          #
# the following rule:                                                     #
#                                                                         #
# find the letter (which should be encrypted)                             #
# in the alphabet;move K positions further (down the alphabet);           #
# take the new letter from here; if "shifting" encountered the end        #
# of the algorithm, continue from its start. For example, if K = 3        #
# (shift value used by Caesar himself), then A becomes D, B becomes       #
# E, W becomes Z and Z becomes C and so on, according to the following    #
# table:                                                                  #
#                                                                         #
#                                                                         #
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z                     #
#                                                                         #
# | | | | | | | | | | | | | | | | | | | | | | | | | |                     #
# V V V V V V V V V V V V V V V V V V V V V V V V V V                     #
#                                                                         #
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C                     #
#                                                                         #
#                                                                         #
# So if the source message was VENI VIDI VICI then after encoding it      #
# becomes YHQL YLGL YLFL.                                                 #
#                                                                         #
# On the other hand encrypted message should be "shifted back" to         #
# decode it - or shifted by 26 - K which is the same.                     #
#                                                                         #
# So if we have encoded message HYHQ BRX EUXWXV, we can apply shift       #
# of 26 - K = 26 - 3 = 23 and find the original text to be EVEN YOU       #
# BRUTUS.                                                                 #
#                                                                         #
# Input data will contain two integers - the number of lines of encrypted #
# text and the value of K.The following lines will contain encrypted      #
# text, consisting of capital latin letters A ... Z, each line is         #
# terminated with a dot . which should not be decoded. Answer should      #
# contain the decrypted message (in a single line, no line splitting      #
# is needed).                                                             #
#                                                                         #
# Example:                                                                #
#                                                                         #
# input data:                                                             #
# 2 3                                                                     #
# YHQL YLGL YLFL.                                                         #
# HYHQ BRX EUXWXV.                                                        #
#                                                                         #
# answer:                                                                 #
# VENI VIDI VICI. EVEN YOU BRUTUS.                                        #
###########################################################################



def main():
    shift = 0
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
                ,"O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    answer = ""
    test2 = readFileIn()
    for i in test2:
        if test2.index(i) == 0:
            split = i.split(" ")
            shift = int(split[-1])
        elif test2.index(i) > 0:           
            shiftedAlpha = shiftAlphabet(alphabet, shift)
            charPosArray = getCharPosition(alphabet, shiftedAlpha, i)
            answer = answer + charPosArray+ " "           
    print(answer)
    

def readFileIn():
    fileObject = open("test1.txt", "r")
    fileText = fileObject.read()
    fileArray = fileText.split("\n")
    return(fileArray)


def shiftAlphabet(alpha, shiftNum):
    alphabet = alpha + alpha[:(26-shiftNum)]
    for i in range(26-shiftNum):
        alphabet.pop(0)
    return(alphabet)


def getCharPosition(alpha, shiftedAlpha, readLine):
    intermediate = readLine
    answer = ""
    for c in intermediate:
        for a in alpha:
            if c == a:
               answer = answer + shiftedAlpha[alpha.index(a)]
        if c == " ":
            answer = answer + " "
        if c == ".":
            answer = answer + "."
    return(answer)
   
main()















