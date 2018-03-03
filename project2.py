# aliya tyshkabayeva
import re
# reading the given txt file as a string
def readFile(filename):
    file = open(filename)
    s = file.read()
    return s
        
        
# here we are working with the inputList 
# we are going line by line and creating a dictionary of languages, so that
# later we can store in those LanguageDictionaries our frequency triagrams
def inputList(filename):
    file = open(filename)
    languageDict = {}
    for line in file:
        splitList = []
        l = line.split()
        if l[0] not in languageDict:
            languageDict[l[0]] = [l[1]]
        if l[0] in languageDict:
            languageDict[l[0]] += [l[1]]
    return languageDict

# here we are removing the punctuations and cleaning the string
# so that later we can use it in triagramCalc
def cleanTheString(s):
    return re.sub('[^a-zA-Z]+', ' ', s.lower())


# here we are creating dictionaries of triagrams frequencies for the given txt file 
def triagramCalc(mainString): 
    dict1 = {}
    for i in range(0, len(mainString) -2):
        tri = mainString[i:i+3]
        if tri in dict1:
            dict1[tri] += 1
        else:
            dict1[tri] = 1
    return dict1 


# here we are storing our triagrams into language dictionaries
def createTriagram(languageDict):
    dictOfDict = {}
    for lang in languageDict.keys():
        newListFromLang = languageDict[lang]
        langString = ""
        for file in newListFromLang:
            stringy = readFile(file)
            langString += cleanTheString(stringy)
        dictOfDict[lang] = (triagramCalc(langString))                    
        normalizeTri(dictOfDict[lang])
    return dictOfDict


# function to normalize the triagrams
def normalizeTri(dictTri):
    counter = 0
    for each in dictTri:
        total = dictTri[each]
        counter += total
    for each in dictTri:
        dictTri[each] /= counter
    return dictTri

# calculating cosine numberator of two dictionaries           
def cosineN(dict1, dict2):
    total = 0
    for each in dict1:
        if each in dict2:
            total += dict2[each]*dict1[each]   
    return total

# calculating cosine denominator of two dictionaries           
def cosineD(dict1, dict2):
    total1 = 0
    total2 = 0
    for value in dict1.values():
        total1 +=value*value
    for value in dict2.values():
        total2 +=value*value
    return math.sqrt(total1) * math.sqrt(total2)

# calculating cosine similarity of two dictionaries
def cosineSim(dict1, dict2):
    return cosineN(dict1, dict2)/cosineD(dict1, dict2)
    

def main():
    #print(cleanTheString(readFile("english1.txt")))
    #print(triagramCalc(cleanTheString(readFile("english1.txt"))))
    print(createTriagram(inputList("FirstFileProject.txt")))
    
main()
    
    
#def compareTriagrams(languageDict):
 #   for key in languageDict:
  #      if key == "Unknown":
            #create a txt file and then go through each dictionary in languageDictionary
            #and compare the unknown dictionary of triagram frequencies to all other 
            #triagram frequencies and store them next to their fileNames in ascending order
         #   for triagram in key:
                #calculate the cosine similarity
                
        


#{french: {"tri" :2 .... }, english: {"eng": 23 .... }}

#    
                
