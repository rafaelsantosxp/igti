# Example_3
age = dict(Tulio=10, Angela=25, Francieli=20)
print(age.keys())
people = input("Type the of the person who you want know the age: ")
try:
    print(f"{people} is {age[people]} years old")
except KeyError:
    print(f"The name {people} not exists")
