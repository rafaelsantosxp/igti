# Example_1
try:
    x = input("Type name of file: ")
    archive = open(x, 'r')
except FileNotFoundError:
    print("File not found, bitch!")
    exit(0)
for lines in archive:
    print(lines.rstrip())
archive.close()

print("End of code")
