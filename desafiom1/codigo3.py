def funcao_4(lista_numerica=[1,1]):
    print("valor passado", lista_numerica)
    a = lista_numerica[0]
    b = lista_numerica[-1]
    print(a, b)
    if (a == b):
        return True
    else:
        return False
print (funcao_4())        
