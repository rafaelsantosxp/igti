# Example_while

x = 1
while x <= 6:
    print(x)
    x += 1
print(
    "End of code"
)

# Example_while

x = 1
while x <= 6:
    print(x)
    if x == 3:
        break
    x += 1

# Example_while

x = 1
while x <= 6:
    x += 1
    if x == 3:
        continue
    print(x)
