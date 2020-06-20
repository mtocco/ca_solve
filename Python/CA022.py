# John and Mary founded J&M publishing house and bought
# two old printers to equip it.
# 
# Now they have their first commercial deal -
# to print a document consisting of N pages.
#
# It appears that printers work at different speed.
# One produces a page in X seconds and other does it in Y seconds.
#
# So now company founders are curious about
# minimum time they can spend on printing the whole
# document with two printers.
# 
# Input data contains number of test cases
# in the first line.
# Then test-cases will follow, each
# in separate line.
# Each testcase contains three integer values - X Y N
# , where N will not exceed 1,000,000,000.
# Answer should contain minumum printing times
# for each of testcases, separated by spaces.
#
# Example:
# input data:
# 2
# 1 1 5
# 3 5 4
# 
# answer:
# 3 9

def readFileIn():
    fileObject = open("test1.txt", "r")
    fileText = fileObject.read()
    fileArray = fileText.split("\n")
    return(fileArray)

def solve22(a):
    x = int(a[0])
    y = int(a[1])
    printerA = 0
    printerB = 0
    for i in range(int(a[2])):
        if (i == (int(a[2])-1)):
            if y > x:
                return(x)
            else:
                return(y)           
        if y > x:
            printerA += 1
            x += int(a[0])
        else:
            printerB += 1
            y += int(a[1])


def main():
    data = readFileIn()
    answer = ""
    for i in range(len(data[1:])):
        answer = answer + str(solve22(data[i+1].split(" "))) + " "
    print(answer)

main()
