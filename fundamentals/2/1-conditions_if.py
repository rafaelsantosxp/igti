# Example_1
num: float = float(input("Type a number :"))
if num % 2 == 0:
    print("This number is even. \n")
else:
    print("This number is odd. \n")

# Example_2
num = 15
if num < 15:
    print("This number is lower than 15. \n")
else:
    print("This number is higher or equal 15. \n")

# Example_3
x = int(input('input a valor to x'))
y = int(input('input a valor to y'))
if x > y:
    print('O X:(%2d) is bigger than  Y:(%2d)' % (x, y))
else:
    print('O X:(%2d) is less than  Y:(%2d)' % (x, y))
