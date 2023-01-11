# 1

num_calls = 0


def exercitiu(x):
    global num_calls
    num_calls = 3
    print(num_calls, '7')
    num_calls += 1
    return x * x


print(num_calls, '12')
print(exercitiu(4))
print(num_calls, '14')

# 2

# x = 1
# def f():
#  return x

# print(x)
# print(f())

# 3

x = [1, 2, "hello", "cinci", ["another", "list"]]
print(len(x[3]))

# 4

# a = (1,2,3)
# a[1]=4
# print(x)

# 5

b = [1, 2, 3]
c = [4, 5]
print(b + c * 3)

# 6

a = [1, 2, 3, 4]
print(a[-1:])

# 7

d = [0, 1, [2]]
d[2][0] = 3
d[2].append(4)
# d[2]=2
print(d)

# 8

def exercitiu1(i):
    for i in range(i):
        return i


f = exercitiu1(3)
print(f)

# 9

g = range(10)
y = [x * x for x in g if x % 2 == 0]
print(y)

# 10

def make_account():
    return {'balance': 0}


def deposit(account, ammount):
    account['balance'] += ammount
    return account['balance']


a = make_account()
print(deposit(a, 10))
