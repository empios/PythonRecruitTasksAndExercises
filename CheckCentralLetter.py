def central(word):
    wordLength = len(word)
    if wordLength%2 != 0:
        wordList = list(word)
        middleChar = wordList[int(len(wordList)/2)]
        print(middleChar)
    else:
        print("''")
    
central("ewa")
central("adam")