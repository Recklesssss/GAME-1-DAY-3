from sympy.physics.units import second

year = int(input("which year do you want to check?"))

first_condition = year % 4 == 0
second_condition = year % 100 == 0
third_condition = year % 400 == 0

if first_condition == True and second_condition == False:
    print(" it leap year")
elif first_condition == True and third_condition == True:
    print(" it leap year")
else:
    print(f"{year}, is not a leap year")