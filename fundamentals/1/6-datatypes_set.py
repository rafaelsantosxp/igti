conjunto1 = tuple("Python")
print(conjunto1)
conjunto1 = set("Python")
print(conjunto1)

conjunto2 = set(["Python", "Shell", "Python"])
print(conjunto2)
conjunto2 = tuple(["Python", "Shell", "Python"])
print(conjunto2)

conjunto3 = set([1])
print(conjunto3)
conjunto3.add(3)
conjunto3.add(4)
conjunto3.add(4)
conjunto3.add((4, 6, 7)) # ( ) -> indicate tuple
conjunto3.update([4, 8, 9]) # [ ] -> indicate list

print(conjunto3)

conjunto4 = set(["Python", "Shell", "For"])
print("Loop For apresenta e verifica qual String é igual a Python :")
for i in conjunto4:
    print(i)
    print("Python" in i)


conjunto5 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print("Mostrando conjunto = ", conjunto5)

conjunto5.remove(2)
print("Mostrando conjunto com remove = ", conjunto5)

conjunto5.pop()
print("Mostrando conjunto com pop = ", conjunto5)

conjunto5.discard(3)
print("Mostrando conjunto com discard = ", conjunto5)

conjunto5.clear()
print("Mostrando conjunto com clear = ", conjunto5)