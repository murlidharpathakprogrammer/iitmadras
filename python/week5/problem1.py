# Problem 1: Write a Python code using functions which calculates the number of upper case letters, lower case letters, total number of characters and number of words
def upper(s):
    upper = 0
    for char in s:
        if(char.isupper()):
            upper+=1
    return (upper)

def lower(s):
    lower = 0
    for char in s:
        if(char.islower()):
            lower+=1
    return (lower)

def characters(s):
    chars = 0
    for char in s:
        chars+=1
    return (chars)

def words(s):
    words = 1
    for char in s:
        if(char==' '):
            words+=1
    return words

sentence = input('Enter the sentence: ')

uLetters = upper(sentence)
print(f'\nTotal number of upper case characters: {uLetters}')

lLetters = lower(sentence)
print(f'\nTotal number of lower case characters: {lLetters}')

numOfChars = characters(sentence)
print(f'\nTotal number of characters: {numOfChars}')

numOfWords = words(sentence)
print(f'\nTotal number of words: {numOfWords}')