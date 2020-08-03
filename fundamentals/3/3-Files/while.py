file_name = 'poem.txt'
poem = open(file_name)
list_lines = []
lines = poem.readline().rstrip()
number_lines = 0
while lines != 'fim':
    number_lines = number_lines + 1
    list_lines.append(lines)
    lines = poem.readline().rstrip()
for i in list_lines:
    print(i)
print(number_lines)

