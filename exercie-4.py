weight = input("what is your weight? ")
height = input("what is your height? ")

con_weight = int(weight)
con_height = float(height)

bmi = float(con_weight / (con_height ** 2))

print("Your BMI is: " + str(bmi))
if bmi < 18.5:
    print("You are under weight")
elif 18.5 <= bmi <= 25:
    print("you are normal weight")
elif 25 <= bmi <= 30:
    print("you are obese weight")
else:
    print("you are clinically obese weight")