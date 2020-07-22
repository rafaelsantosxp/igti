conjunto1 = set([1, 2, 3])
conjunto2 = set([3, 4 ,5])

print(" A ", conjunto1," - "," B ", conjunto2)

inters = conjunto1.intersection(conjunto2)

united = conjunto1.union(conjunto2)

differ = conjunto1.difference(conjunto2)

symmet =  conjunto1.symmetric_difference(conjunto2)

print("intersection = ", inters)
print("union = ", united)
print("difference = ", differ)
print("symmetric = ", symmet)