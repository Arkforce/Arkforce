weather = input("What is the current season: ").upper()
temp = int(input("What is the current temperature degree? "))
if weather == "SUMMER":
    if temp>=60 and temp <=80:
        print(f"The current temperatire is {temp}, you can take your baby out") 
    else: 
        print(f"The current temperatire is {temp}, you CANNOT take your baby out")
elif weather == "WINTER":
    if temp>-20:
        print(f"The current season is {weather.lower()} temperature is {temp}, you can take your baby out") 
else:
  print("You cant take your baby out")

