dictionar = {"cheie": "valoare", "cheie1" : "3" }
print(dictionar)
print(dictionar["cheie1"])
# print(dictionar["cheie2"])
dictionar["cheie2"]=5
print(dictionar.get("cheie2",5))
dictionar.update({"cheie2": 6, "cheie3": 6})
print(dictionar)
print(dictionar.keys())
print(dictionar.values())