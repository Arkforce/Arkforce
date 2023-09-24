num = 876
last_digit = num%10
first_two_digits = num//10
first_digit = first_two_digits//10
middle_digit = first_two_digits%10
output=last_digit*middle_digit*first_digit
print(output) 