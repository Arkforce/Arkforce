big_package = 5
small_package = 1
limit = int(input("Enter the total KG of shipment "))
total_big = limit//big_package
total_small = limit - (total_big*big_package)

print(f"you can ship {total_big} of big packages")
print(f"you can ship {total_small} of small packages")