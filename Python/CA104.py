##################################################################
#################### Code Abbey Problem 104 ######################
##################################################################
#
# URL:
# https://www.codeabbey.com/index/task_view/triangle-area
#
# Author: Michael Tocco
# Date Completed: 9/24/19
# Being able to calculate area of triangle is quite important since
# many more complex tasks are often easily reduced to this (and we
# will use it too later).
#
# One of the oldest known methods is Heron's Formula which takes as
# inputs the lengths of the triangle's sides.
#
# In this problem you however is to write a program which uses X and
# Y coordinates of the triangle's vertices instead. So you can use
# either this formula somehow or find another one.
# 
# Input data will contain the number of triangles to process.
# Next lines will contain 6 values each, in order X1 Y1 X2 Y2 X3 Y3,
# describing three vertices of a triangle.
# Answer should give areas of triangles separated by space
# (precision about 1e-7 is expected).
# 
# Example:
# data:
# 3
# 1 3 9 5 6 0
# 1 0 0 1 10000 10000
# 7886 5954 9953 2425 6250 2108
# 
# answer:
# 17 9999.5 6861563

import math

def main():
    file1 = open("test1.txt","r")
    file1.readline()
    array = remNewLines(file1.readlines())
    array = convArray(array)
    answer = ""
    for i in array:
        answer = answer + str(solve104(i)) + " " 
    print(answer)

def remNewLines(array):
    for i in range(len(array)):
        array[i] = array[i].replace("\n","")
    return(array)

def convArray(array):
    intermediate = []
    for i in array:      
        i = i.split(" ")
        for j in i:
            j = int(j)
        intermediate.append(i)
    return(intermediate)

def solve104(a):
    sideA = math.sqrt(((int(a[0]) - int(a[2]))*(int(a[0]) - int(a[2])))+((int(a[1]) - int(a[3]))*(int(a[1]) - int(a[3]))))
    sideB = math.sqrt(((int(a[0]) - int(a[4]))*(int(a[0]) - int(a[4])))+((int(a[1]) - int(a[5]))*(int(a[1]) - int(a[5]))))
    sideC = math.sqrt(((int(a[2]) - int(a[4]))*(int(a[2]) - int(a[4])))+((int(a[3]) - int(a[5]))*(int(a[3]) - int(a[5]))))
    s = (sideA + sideB + sideC)/2
    area = math.sqrt(s * (s-sideA) * (s-sideB) * (s-sideC))
    return(area)

main()
