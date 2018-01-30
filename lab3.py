# Aliya Tyshkanbayeva
# lab 3

def readWords(filename):
    wordList = []
    file = open(filename)
    for word in file:
        wordList.append(word.rstrip())
    file.close()
    return wordList



# funcion to print palindromes from wordList
def printPalindromes(wordList):
    for i in range(0, len(wordList)):
        if(isPalindrome(wordList[i]) == True):
            print(wordList[i])
    return False
                   

# a function to check if the string is a palindrome
# runs a loop from 0 to the half the length of the string, check 
# the first character to the last one, second to second last and etc
def isPalindrome(word):
    palindromic = True
    for i in range(0, len(word)//2):
        if word[len(word)-i-1] != word[i]:
            palindromic = False
    return palindromic
            
        


def main():
    printPalindromes(readWords("words.txt"))
    # test cases for the function to check if the word is palindromic
    print(isPalindrome("ala"))
    print(isPalindrome("bebeb"))
    print(isPalindrome("bebebe"))
    print(isPalindrome("calapse"))
    print(isPalindrome("basics"))
    print(isPalindrome("stats"))
    print(isPalindrome("did"))
        


main()

