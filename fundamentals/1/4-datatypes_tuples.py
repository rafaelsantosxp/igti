# Easy tuple
tuple1 = ('Python', 'Shell')
print (tuple1)

list1 = [1, 2, 3, 4, 5]
print(type(list1))
print (tuple(list1))
print(type(tuple(list1)))

LAST_TAG = '0.1.5'
print(tuple(LAST_TAG))
RELEASE = (LAST_TAG[0])
FEATURE = (LAST_TAG[2])
HOTFIX  = (LAST_TAG[4])
print(RELEASE)
print(FEATURE)
print(HOTFIX)
