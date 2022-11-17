variabila1 = 1
variabila2 = 2
mesaj = 'variabila 1 e mai mica'
mesaj1= None #declar variabila fara valoare in ea
if  variabila1 == variabila2 and (mesaj1 := "egalitate"): # atribuire in if
   mesaj = mesaj1
elif variabila1 > variabila2:
  mesaj = 'variabila 1 e mai mare'
# mesaj = 'egalitate' if variabila1 == variabila2 else "variabila 1 e mai mica"
print(mesaj1)
