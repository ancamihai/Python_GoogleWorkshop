variabila= input("Adauga un nr: ")
# variabila=int(variabila) pt a vedea exceptia
lista=[1,2,3]
try:
    if variabila.isdigit():
        raise ValueError
    print(lista[3])
    print(a)
    variabila = int(variabila)

except ValueError:
    print("exceptie")
    if variabila.isdigit():
        variabila=int(variabila)
    a=None
except NameError:
    print("variabila nedefinita")
    a= None
except IndexError:
    print("Eroare de index")
    print(lista[3:4])
except Exception:
    print("clasa default")
else:
     print("Nu exista nicio exceptie")
finally:
    print("Se ruleaza oricum")
print(variabila,'variabila')
print(a,'a')