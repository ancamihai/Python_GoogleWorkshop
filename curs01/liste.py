# lista = []
# print(type(lista))
# lista.append(3)
# lista.append(4)
# lista.append(3)
# lista.append("string")
# print(len(lista))
lista = [3, 4, 4, [1, '2', "element"], "string"]
print(lista[4:5])  # fara elementul cu indexul 5
print(lista[5:6])
print(lista[0:6])
print(lista[0:3])
print(lista[1:])
print(lista[:4])
print(lista[3][2][6]) # slicing se poate face si pt string, fiecare element poate fi accesat printr-un index
