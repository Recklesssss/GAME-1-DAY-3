print("Welcome to Python Pizza Deliveries!")
size = input("what size do you want? S,M, or L")
add_pepperoni = input("Do You Want pepperoni? Y or N")
extra_cheese =input("Do You Want extra cheese? Y or N")

prize = 0

if size == "S":
    prize += 15
    if add_pepperoni == "Y":
        prize += 2
    if extra_cheese == "Y":
        prize += 1
elif size == "M":
    prize += 20
    if add_pepperoni == "Y":
        prize += 3
    if extra_cheese == "Y":
        prize += 1
else:
    prize += 25
    if add_pepperoni == "Y":
        prize += 3
    if extra_cheese == "Y":
        prize += 1
print(f"\nYour Total Price will be ${prize}")