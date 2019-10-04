

def main():
    file1 = open("test055.txt","r")
    file1 = file1.readlines()
    splText = (splitText(str(file1)))
    solve55(splText)

def splitText(text):
    splitText = text.split(" ")
    print(splitText)
    splitText.sort()
    return(splitText)

def solve55(array):
    counter = 0
    answer = ""
    for i in range(len(array)):
        if(i>0):
            if(array[i] == array[i-1]):
                counter = counter + 1
                if(counter < 2):
                    
                    answer = answer + str(array[i]) + " "
            else:
                counter = 0
    print(answer)

main()
