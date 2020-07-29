# Example_7
x = float(input('Type the first number'))
y = float(input('Type the second number'))

print('Type 1 to ADD')
print('Type 2 to SUBTRACT')
print('Type 3 to MULTIPLY')
print('Type 4 to SPLIT')
choice = int(input('Which one?'))

if choice == 1:
    print(x + y)
elif choice == 2:
    print(x - y)
elif choice == 3:
    print(x * y)
elif choice == 4:
    print(x / y)
else:
    print('Your choice not exists')