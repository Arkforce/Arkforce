user_input = int(input("Enter the number: "))
for numbers in range(1,user_input+1):
    if numbers%2==0:
        print(numbers,end=", ")