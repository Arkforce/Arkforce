def ispalydrome(word):
    reversed = word[::-1]
    return reversed == word
word = input("Enter a word").lower()
print(ispalydrome(word))