# Example_in

buy_list = ['detergent', 'soap', 'popcorn']
item = input("Type a item: ")
if item not in buy_list:
    print(f'Error, {item} not in buy list')
else:
    print(f'Can buy {item}, this shit in your buy list')
