# Example_4

height = int(input("Enter with your height"))
if (height < 150) or (height > 185):
    print("You cannot play")
else:
    print("You can play")

# Example_5

num = float(input('Enter with numerator'))
den = float(input('Enter with denominator'))
answer = float(input('Enter with the answer'))
result = num / den
bigger = abs(result)

if abs((answer - result)/bigger) <= 0.1:
    print('Correct answer')
else:
    print(f'Your answer {answer} is WRONG! The correct is {result}')

# Example_6
x = float(input('Type the first number'))
y = float(input('Type the second number'))

print('Type 1 to ADD')
print('Type 2 to SUBTRACT')
print('Type 3 to MULTIPLY')
print('Type 4 to SPLIT')
choice = int(input('Which one?'))

if choice == 1:
    print(x + y)
else:
    if choice == 2:
        print(x - y)
    else:
        if choice == 3:
            print(x * y)
        else:
            if choice == 4:
                print(x / y)
            else:
                print('Your choice not exists')