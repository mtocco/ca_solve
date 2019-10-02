def main():
    contents = readFile()
    calcCheckSum(contents)
    

def readFile():
    file = open("/Users/appleuprising/Google Drive/School/CompSci/Code Abbey/CA027/test1.txt","r")
    if file.mode =='r':
        contents = file.read()
        contents = contents.split()[1:]
    return(contents)
