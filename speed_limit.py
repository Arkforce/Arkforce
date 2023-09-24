driver_speed = int(input("Enter your speed: ?"))
state = input("Enter your state code: ").upper()
if state == "IN":
    speed_limit = 70
    if driver_speed <= speed_limit:
        print("You are driving safe!")
    elif driver_speed>(speed_limit*1.1):
        print("150 $ Fine") 
    else:
        print("YELLOW WARNING!") 
else:
    speed_limit = 55
    if driver_speed <= speed_limit:
        print("You are driving safe!")
    elif driver_speed>(speed_limit*1.1):
        print("100 $ Fine") 
    else:
        print("CITATION!")            