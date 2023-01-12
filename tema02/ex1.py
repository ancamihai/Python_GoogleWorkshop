def function1(*args, **kwargs):
    suma = 0
    for i in args:
        if (isinstance(i, int)) or (isinstance(i, float)):
            suma += i
    return suma


print(function1(1, 5, -3, "abc", [12, 56, "cad"]))
print(function1())
print(function1(2, 4, "abc", param_1=2))
