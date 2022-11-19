lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_ascendent = lista_initiala.copy()
lista_ascendent.sort()
lista_descendent = lista_ascendent.copy()
lista_descendent.reverse()
print("Lista initiala:")
print(lista_initiala)
print("Lista in ordine ascendenta:")
print(lista_ascendent)
print("Lista in ordine descendenta:")
print(lista_descendent)
# Afisarea numerelor pare din lista - metoda1: folosind lista ordonata ascendent si SLICE
print("Elementele pare din lista, obtinute folosind metoda1:")
print(lista_ascendent[1::2])
# Afisarea numerelor pare din lista - metoda2: folosind lista intiala, SLICE si concatenari
print("Elementele pare din lista, obtinute folosind metoda2:")
print(lista_initiala[1:4:2]+lista_initiala[6:8]+lista_initiala[9:])
# Afisarea numerelor impare din lista - metoda1: folosind lista ordonata ascendent si SLICE
print("Elementele impare din lista, obtinute folosind metoda1:")
print(lista_ascendent[0::2])
# Afisarea numerelor impare din lista - metoda2: folosind lista initiala, SLICE si concatenari
print("Elementele impare din lista, obtinute folosind metoda2:")
print(lista_initiala[0:5:2]+lista_initiala[5:9:3])
# Afisarea elementelor multipli ai lui 3 - metoda1: folosind lista ordonata ascendent si SLICE
print("Elementele multipli ai lui 3, obtinute folosind metoda1:")
print(lista_ascendent[2::3])
# Afisarea elementelor multipli ai lui 3 - metoda2: folosind lista initiala, SLICE si concatenari
print("Elementele multipli ai lui 3, obtinute folosind metoda2:")
print(lista_initiala[2:5:2]+lista_initiala[9:])
# Lista initiala nu a fost modificata.
print("Lista initiala nu a fost modificata dupa toate aceste operatii:")
print(lista_initiala)
