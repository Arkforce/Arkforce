def find_HCF(num1,num2):
    possible_hcf = num1
    while True:
        if num1 % possible_hcf==0 and num2 % possible_hcf==0:
            return possible_hcf
        possible_hcf -=1

print(find_HCF(32,48))
