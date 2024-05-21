number = []

for i in range(5):
    a = int(input(f"Enter the {i+1}th number: "))
    number.append(a)

max = 0

for i in range(5):
    if(max < number[i]):
        max = number[i]

print(f'The maximum number is {max}')