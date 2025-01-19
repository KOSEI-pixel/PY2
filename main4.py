height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))

BMI=weight/(height/100)**2

print("Your BMI is: ")

if BMI<18.5:
    print(" you are skinny, so Underweight")
elif 18.5<=BMI<25:
    print(" you are healthy, so Normal weight")
elif 25<=BMI<30:
    print(" you are overweight, so Overweight")
else:
    print("you are obese,commparing u to a normal person the person is a twig")1    