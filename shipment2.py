big_package = int(input("Enter the amount of big packages: "))
small_package = int(input("Enter the amount of small packages: "))
limit = int(input("Enter the total KG of shipment "))



total_big = limit//5
total_small = limit - total_big*5

if total_big*5+small_package<=limit:
    print("just send them all")
else:    

    print(f"you can ship {total_big} of big packages")
    print(f"you can ship {total_small} of small packages")