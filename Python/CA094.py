
def main():
    answer = ""
    test = getFile()
    test = removeJunk(test)
    for i in test:      
        answer += str(solve94(i)) + " "
    print(answer)    
    
def solve94(array):
    total = 0
    for i in array:
        total += int(i)*int(i)
    return(total)

def getFile():
    f = open("test094.txt", "r")
    f.readline()
    return(f.readlines())

def removeJunk(array):
    array = [i.replace("\n","") for i in array]
    array = [i.split(" ") for i in array]
    return(array)

main()
