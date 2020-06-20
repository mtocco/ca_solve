import math

def main():
    file1 = open("test128.txt","r")
    file1.readline()
    array = remNewLines(file1.readlines())
    array = convArray(array)
    answer = ""
    for i in array:
        answer = answer + str(solve128(i)) + " "
        
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

def solve128(a):
    return(int(math.factorial(int(a[0]))/
               (math.factorial(int(a[1]))*
                math.factorial(int(a[0])-int(a[1])))))
 
main()
