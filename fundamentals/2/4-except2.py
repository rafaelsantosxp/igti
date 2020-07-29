# Example_2

try:
    x = int(input("Type the first number"))
except ValueError:
    print("INPUT A INT VALUE!")
    exit(0)
try:
    y = int(input("Type the second number"))
except ValueError:
    print("INPUT A INT VALUE!")
    exit(0)
try:
    if x % y == 0:
        print (f"numerator {x} is divisible by denominator {y}.")
    else:
        print ("division is not entire")
except ZeroDivisionError:
    print("SHIT!")
