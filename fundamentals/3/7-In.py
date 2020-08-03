# Example_in

list_one = [1, 2, 3, 4, 5]
list_two = [4, 5, 6, 7, 8]

for i in list_one:
    if i in list_two:
        print(f"{i} is common in lists")
    else:
        print(f"{i} is not common in lists")
