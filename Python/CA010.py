#Code Abbey 10

def main():

    file1 = open("test010.txt","r")
    file1.readline()
    array = remNewLines(file1.readlines())
    array = convArray(array)
    answer = ""
    for i in array:
        answer = answer + solve010(i) + " "
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

def solve010(array):
    m = solveM(int(array[0]),int(array[1]),int(array[2]),int(array[3]))
    b = solveB(int(array[0]),int(array[1]),m)
    return("(" + str(m) + " " + str(b)+")")


def solveM(x1, y1, x2, y2):
    return(int((y2-y1)/(x2 - x1)))

def solveB(x1 ,y1, m):
    return(int(y1 -(x1*m)))


main()
