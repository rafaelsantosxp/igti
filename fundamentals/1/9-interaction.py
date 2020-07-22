num = float (input("Type a number: "))
print("Typed number is :", num)

# raise to exponent]
base = float(input("enter with the base number : "))
exponent = float(input("enter with exponent number : "))
result = base**exponent
print(str(base), "^", str(exponent), "=", result)

print(" %1.2f ^%1.3f = %1.4f  " %(base, exponent, result))