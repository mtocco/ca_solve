


def main():
    f = open("test1.txt", "r")
    x = f.readline().split(" ")
    ar = []
    for i in range(int(x[0])):
        ar.append(i+1)
    counter = 0                       		    
    while (len(ar) > 1): 
        if (counter == (int(x[1])-1)):
                ar.pop(0)
        else:
            ar.append(ar[0])
            ar.pop(0)
        counter = ((counter+1)%int(x[1]))
    print(str(ar) + " Counter = " + str(counter)
           )

main()


    
