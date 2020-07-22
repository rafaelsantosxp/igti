list = []
print("lista vazia")
print(list)
print(type(list))

list = ["Python", "Linux", "Shell"]
print(list)
print(list[0])
print(list[2])

list = [["Python inside", "Shell inside"], 123, "Python outside"]
print(list)
print(list[0])
print(list[0][1])
print(list[1])

list = [1, 2, 3, 4]
print("lista numerica: ", list)
# add no final da lista
list.append(5)
print("lista numerica: ", list)
list.append("Python")
print("lista numerica: ", list)

list = []
list.append('Blue')
list.append('Red')
list.append('Yellow')
list.append('Green')
print(list)

list.insert(2, 'Black')
list.insert(0, 'Pink')
print(list)

list.extend(["White", "Gray"])
print(list)

list.remove(-1)
list.remove('Red')
print(list)
#pop remove o ultimo elemento

list.pop()
print(list)