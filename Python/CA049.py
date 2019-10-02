##################################################################
#################### Code Abbey Problem 049 ######################
##################################################################
#
# URL:
# https://www.codeabbey.com/index/task_view/rock-paper-scissors
#
# Author: Michael Tocco
# There is a game which is of special importance in the Computer
# Science because it though simple itself, could be used
# for creating very cunning Artificial Intelligence algorithms
# to play against human (or each other) with predicting the
# opponent's behavior.
# 
# This ancient game is played between two participants who
# simultaneously cast one of three figures by their fingers
# - Rock, Paper or Scissors.
# 
# If both cast the same figure, the round is considered a draw.
# Otherwise the following rules are applied:
#     
# Rock beats Scissors (by blunting them)
# Scissors beat Paper (by cutting it)
# Paper beats Rock (by covering it)
# 
# Often the game is played on the staircase. Player who wins the
# round advances one step. One who reaches the end of the staircase
# first is the winner.
# 
# You will be given several records of the played games. You are to
# tell for each of them who of players won.
# 
# Input data will contain the number of matches played in the first
# line.
# Then the matches description is written in separate lines.
# Each line contain several pairs of letters, like PR (first casts
# Paper, second casts Rock), or SS (both cast Scissors), separated
# with spaces.
# Answer should for each of matches specify whether first player
# wins (by value 1) or second (by value 2). There would be no draws.
#
# Example:
# input data:
# 3
# SS PR
# PR RS PS PP SP
# PS RR PS RP
#
# answer:
# 1 1 2

def main():
    file1 = open("test1.txt","r")
    file1.readline()
    answer = ""
    array = remNewLines(file1.readlines())
    for i in array:
        answer = answer + solve49(i.split(" ")) + " "
    print(answer)

def remNewLines(array):
    for i in range(len(array)):
        array[i] = array[i].replace("\n","")
    return(array)

def solve49(array):
    scoreA = 0
    scoreB = 0
    equals = False
    test = array
    for i in test:
        if(i[0] == i[1]):
            equals = True
        if(equals == False):
            if(i[0] == "S" and i[1] == "P"):
                scoreA += 1
            elif(i[0] == "P" and i[1] == "R"):
                scoreA += 1
            elif(i[0] == "R" and i[1] == "S"):
                scoreA += 1
            else:
                scoreB +=1
        equals = False

    if(scoreA > scoreB):
        return("1")
    else:
        return("2")

    
    
main()
