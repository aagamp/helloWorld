unit = input("Is the given temperature is celcius or farenheit (C/F):")
temp = float(input("enter your body temperature"))

if unit == "C":
    temp = 1.8 * temp + 32
    print(f"The temperature of your body  is {temp} degree farenheit")

elif unit == "F":
    temp = 10 / 18 * (temp - 32)
    print(f"The temperature of your body is {temp} degree celcius")

else:
    print(f"The temperature unit of your body does not exist")