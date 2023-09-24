list_of_nums = []
for i in range(7):
    num = input("Enter an integer number: ")
    while not num.isnumeric() or num.startswith("0"):
        num = input("Try again! Enter a correct integer number: ")
    num=int(num)
    list_of_nums.append(num)
print(list_of_nums)    
second_high = min(list_of_nums)
for element in list_of_nums:
    if element>second_high and element< max(list_of_nums):
        second_high=element
print(f"the second high is {second_high}")