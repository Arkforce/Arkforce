given_text = input("Enter the phrase with dogs and cats")

number_of_dogs = given_text.count("dog")
number_of_cats = given_text.count("cat")
print(f"number of dogs {number_of_dogs}" )
print(f"number of cats {number_of_cats} ")
print(number_of_cats==number_of_dogs)