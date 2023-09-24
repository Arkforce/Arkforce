str = input("Enter a string ")
vowels = "aeiouAEIOU"
for el in str:
    if el in vowels:
        print(el,end=" ")    