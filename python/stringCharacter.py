#name = input("Enter your full name : ")
#phone_number = input("Enter your phone number : ")


#result = len(name)

#result = name.find("A")
#result = name.rfind("i")
#name = name.capitalize()



#name = name.isalpha()
#name = name.isdigit()


#name = name.lower()

#name = name.upper()

#result = name.isdigit()

#phone_number = phone_number.count("-")
#phone_number = phone_number.replace("-","")





#print(phone_number)

#(help(str))

# validate user input exercise

username = input("Enter a username :")



if len(username) > 12:

    print("Your username cannot be more than 12 charaacter")
elif not username.find(" ") == -1:
    print("Your username cannot contain space")

elif not username.isalpha():
    print("Your username cannot contain numbers")




else:
    print(f"Welcome {username}")




