

def main():
    answer = ""
    file1 = open("test058.txt","r")
    file1.readline()
    file1 = file1.readline()
    file1 = file1.split(" ")
    file1 = [int(i) for i in file1]
    for i in file1:
        answer = answer + solve58(i) + " "
    print(answer) 


def solve58(cardVal):
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return((str(ranks[int(cardVal%13)]) + "-of-"  + str(suits[int(cardVal/13)])))
    
main()
