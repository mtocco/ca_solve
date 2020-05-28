def readFileIn():
    fileObject = open("test.txt", "r")
    fileText = fileObject.read()
    fileArray = fileText.split("\n")
    return(fileArray)

def getScoreX(code, candidate):
    score = 0
    for i in range(len(code)):
        if code[i] == candidate[i]:
            score += 1
    return(score)

def getScoreY(code, candidate):
    score = 0
    for i in range(len(code)):
        for j in range(len(candidate)):
            if code[i] == candidate[j] and code[j] != candidate[j]:
                score += 1
    return(score)

def main():
    answer = ""
    f = readFileIn()
    candidates = (f[1].split(" "))
    code = list((f[0].split(" ")[0]))
    for i in range(len(candidates)):
        answer = answer + (str(getScoreX(code, list(candidates[i]))) + "-" +
             str(getScoreY(code, list(candidates[i]))) + " " )

    print(answer)

main()
