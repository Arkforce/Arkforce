should_i_ask = True
while should_i_ask:
    print("Enter the 2 words here: ")
    str = input()
    if not str.startswith(" ") and str.count(" ") == 1:
        print("You have entered correctly ")
        should_i_ask = False 