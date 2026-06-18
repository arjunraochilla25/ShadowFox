height = eval(input("Enter height in meters: "))
weight = eval(input("Enter weight in kg: "))
bmi = weight / (height ** 2)
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
