


def main():
    
    x = getData().split(" ")
    print(x)
    
    for (i) in x[::2]:
        i = int(i)
        
        print(i)

def getData():
    f = open("test1.txt", "r")
    f.readline()
    return(f.read().replace("\n"," "))
    

#def solve35(x):
    

    

    
main()


    

