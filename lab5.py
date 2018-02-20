# Aliya 

def readFilesAsString(filename):
    file = open(filename)
    s = file.read()
    return s

def cleanString(str):
    e = ""
    for i in range(0, len(str) - 1, 1):
        if str[i].isdigit():
            e += str[i]
    return e

def numbersCount(stringy):
    numbers = {'0': 0, '1': 0 , '2': 0, '3': 0, '4': 0, '5': 0,
               '6': 0, '7': 0, '8': 0, '9': 0}
    for i in range(0, len(stringy) -1, 1):
        if stringy[i] in numbers.keys():
            numbers[stringy[i]] +=1
    return numbers
   

def main():
    s = readFilesAsString("numbers.txt")
    c = cleanString(s)
    print(c)
    d = numbersCount(c)
    print(d)
    
main()