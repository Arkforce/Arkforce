def find_average(numbers):
    numbers.sort()
    sum = 0
    for num in numbers:
        sum += num

    avg = sum/len(numbers)
    return avg

list = [1,3,4,5,6,7,76,5,4,4]
print(f"The average of {list} is {find_average(list)}")

