num1 = int(input("Enter the fist number: "))
num2 = int(input("Enter the second number bigger than first: "))
while num1<num2:
    if num1%3==0 and num1%8==0:
    
        print(f"{num1} this number is divisible by 3 and 8")
    num1 +=1