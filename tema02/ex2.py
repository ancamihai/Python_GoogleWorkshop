def function2(n: int):
    if n == 0:
        return [0,0,0]
    elif (n % 2 == 0):
        total_sum = n + function2(n-1)[0]
        even_sum = n + function2(n-1)[1]
        uneven_sum = function2(n-1)[2]
        list = [total_sum, even_sum, uneven_sum]
        return list
    else:
        total_sum = n + function2(n - 1)[0]
        even_sum = function2(n - 1)[1]
        uneven_sum = n + function2(n - 1)[2]
        list = [total_sum, even_sum, uneven_sum]
        return list


number = 9
list = function2(number)
print(f"The given number: {number}")
print(f"The sum of all elements in the interval [0, the number]: {list[0]} ")
print(f"The sum of all even elements in the interval [0, the number]: {list[1]} ")
print(f"The sum of all uneven elements in the interval [0, the number]: {list[2]} ")
