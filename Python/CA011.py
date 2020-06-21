#Code Abbey 11

def main():

    file1 = open("test011.txt","r")
    file1.readline()
    array = remNewLines(file1.readlines())
    array = convArray(array)
    answer = ""
    for i in range(len(array)):
        num = str(multAndAdd(array[i]))
        answer = answer + solve011(num) + " "
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

def multAndAdd(array):
    return((int(array[0]) * int(array[1])) + int(array[2]))

def solve011(num):
    answer = 0
    for i in range(len(list(num))):
        answer += int(list(num)[i])
    return(str(answer))
    

main()
