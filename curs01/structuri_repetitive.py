# while True:
#    print("Set instructiuni")
#    break

# variabila1 = 1
# variabila2 = 3
# while variabila1 < variabila2:
#    print(variabila2,'rand 7')
#   variabila1 += 1
# else:
#    print(variabila2, 'rand 10')
lista = ['cumparaturi','citit']
# for i, v in enumerate("Ana are mere"):
#   print(i,v)
for i, v in enumerate(lista):
  print(i,v)

for i in range(3, 10, 3):
    print(i)

dictionar ={"carte1":1 , "carte2":2, "carte3": 3}
for i in dictionar:
    print(i)
for i in dictionar.values():
    print(i)
for i in dictionar.items():
    print(i)
# for i,v in dictionar.items():
    # print(i,v)
for i in dictionar.items(): # desparte tuplu
    index, value=i
    print(index,value)