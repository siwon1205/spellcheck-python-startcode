# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    #PRINT MAIN MENU
    loop = True
    while loop:
        print("1: Spell Check a Word(LinearSearch)")
        print("2: Spell Check a word(BinarySearch)")
        print("3: Spell Check Alice in Wonderland(LinearSearch)")
        print("4: Spell Check Alice in Wonderland(Binary Search)")
        print("5: Exit")

        #MENU SELECTION
        select = input ("Enter Selection (1-5): ")
        #SELECTION RESULTS
        if select == "1":
            checkWordLinear(dictionary)

        elif select == "2":
            checkWordBinary(dictionary)

        elif select == "3":
            checkAliceLinear(aliceWords)

        elif select == "4":
            checkAliceBinary(aliceWords)

        elif select == "5":
            print ("EXIT")
            loop = False
    
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()
#1
def checkWordLinear(dictionary):
    print("Spell check a word")
    word = input("Please enter a word: ")
    result = LinearSearch(dictionary, word.lower())
    if(result == -1):
        print("word not found in the dictionary")
    else:
        print("word found at", result)

#2
def checkWordBinary(dictionary):
    print("SPell check a word")
    word2 = input("Please enter a word: ")
    result = BinarySearch(dictionary, word2.lower())
    if result != -1:
        print("word found at", str(result))
    else:
        print("word not found")

#3
def checkAliceLinear(aliceWords):
    print("Spell check Alice In Wonderland: ")  
    word3 = input("Please enter a word: ")
    result = LinearSearch(aliceWords, word3.lower())
    if(result == -1):
        print("word not found")
    else:
        print("word found at", result)

#4
def checkAliceBinary(aliceWords):
    print("Spell check Alice In Wonderland")
    word4 = input("Please enter a word: ")
    result = BinarySearch(aliceWords, word4.lower())
    if result != -1:
        print("word found at", str(result))
    else:
        print("word not found")


def LinearSearch(list, item):
    for i in range(len(list)):
        if (list[i] == item):
            return i
    return -1

def BinarySearch(list, item):
  low = 0
  high = len(list) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2
    if list[mid] < item:
      low = mid + 1
    elif list[mid] > item:
      high = mid - 1
    else:
      return mid
  return - 1

# Call main() to begin program
main()