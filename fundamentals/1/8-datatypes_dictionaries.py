# Needs key : value
# Not ordenate
dictionary1 = {}
print(dictionary1)
print(type(dictionary1))

dictionary2 = {1 : 'Python', 2: 'Shell', 3: 'Linux' }
print(dictionary2)

dictionary3 = {"Chave": "Valor", 1: [1, 2 ,3, 4]}
print(dictionary3)

dictionary3 = dict({"Chave": "Valor", 1: [1, 2 ,3, 4]})
print(dictionary3)

dictionary4 = {1: 'Python',2: 'Shell', 'BR': {'ve': 'verde', 'az': 'azul', 'am':'amarelo'}}
print(dictionary4)
del dictionary4[1]
print(dictionary4)

dictionary4.popitem() # delete string with inside key:value
dictionary4.pop() # delete key:value
dictionary4.clear()