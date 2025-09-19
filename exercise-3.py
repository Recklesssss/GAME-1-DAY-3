print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Your rollercoaster fee is going to be 5$")
    elif age <= 18:
        print("Your rollercoaster fee is going to be 7$")
    else:
        print("Your rollercoaster fee is going to be 12$")
else:
    print("Sorry, you are too young to ride the rollercoaster!")