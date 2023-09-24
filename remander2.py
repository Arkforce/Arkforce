num=int(input("Enter your birthday in 5 format"))

digit5 = num%10
digit4 = num//10%10
digit3 = num//10//10%10
digit2 = num//10//10//10%10
digit1 = num//10//10//10//10%10
print(digit5,digit4,digit3,digit2,digit1)