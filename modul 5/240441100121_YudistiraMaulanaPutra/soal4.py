def isPolindrom(word):
    return word == word[::-1]  
wordInput = str(input("Insert word: "))
if  isPolindrom(wordInput):
    print(f"{wordInput} is palindrom.")
else:
    print(f"{wordInput} not palindrom.")