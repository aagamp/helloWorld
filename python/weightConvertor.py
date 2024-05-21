# python weight convertor

weight = float(input("Enter your weight"))
unit = input("Kilogram or Pound ? (K or L)")

if unit == "K":
    weight = weight * 2.205
    
    unit = "Lbs"
    print (f"Your weight is : {weight} {unit}")
elif unit == "L":
    unit = "Kgs"
    print (f"Your weight is : {weight} {unit}")
else:
    print(f"{unit} was not valid")

    print (f"Your weight is : {weight} ")





