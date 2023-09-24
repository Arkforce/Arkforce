num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = num1 + num2

if result <10:
    print("Sum of these number equals to 10")
elif result >10 and result < 20:
    print ("Sum of these numbers is 20")
else:
    print(f"The sum is {result}")


