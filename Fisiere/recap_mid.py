# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
#
#
# print(exercitiu(4))

# a. 9
# b. 16  #correct
# c. 4
# d. error

# ----------------------------------------

# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())

# a. error
# b. 1
# c. 1
#    1   #correct
# d. 0
#    1

# ----------------------------------------

# x = [111, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))

# a. TypeError: object of type 'int' has no len()
# b. 5  #correct
# c. 0
# d. 2

# print(len(x[4]))
# print(len(x[4][0]))
# print(len(x[0]))
# print(len(x[4][2]))

# ----------------------------------------
#
# x = (1, 2, 3)
# x[1] = 4

# a. x = (1, 1, 3)
# b. x = (1, 4, 3)
# c. x = [1, 2, 3]
# d.TypeError # correct

# ----------------------------------------

# a = [1, 2, 3]
# b = [4, 5]
#
# print(a + b * 3)

# a. [1, 2, 3, 4, 5]
# b. [1, 2, 3, 12, 15]
# c. error
# d. [1, 2, 3, 4, 5, 4, 5, 4, 5] #correct

# ----------------------------------------

# x = [1, 2, 3, 4]
# print(x[-1:])

# a. [1, 2, 3]
# b. [4]         # correct
# c. [1, 2, 3, 4]
# d. [3, 2, 1]

# ----------------------------------------

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

# a. [0, 1, 3]
# b. [0, 1, [2]]
# c. [0, 1, 2]     #correct
# d. error

# ----------------------------------------

# def exercitiu(i):
#     for i in range(i):
#         print(i)
#
# x = exercitiu(3)
# print(x)

# a. error
# b. 0 1 2
# c. 3
# d. 0 # correct

# ----------------------------------------

# a = range(10)
# y = [x*x for x in a if x % 2 == 0]
# print(y)

# a. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b. [2, 4, 6, 8]
# c. [0, 4, 16, 36, 64] # correct
# d. [0, 2, 16, 36, 64]

# y = [x*x for x in a if x % 2 == 0]

# ----------------------------------------

# def make_account():
#     return {'balance': 0}
#
# def deposit(account, amount):
#     # account['balance'] += amount
#     account['balance'] = account['balance'] + amount
#     return account['balance']
#
# a = make_account()
# print(deposit(a, 10))

# a. error
# b. 0
# c. 10
# d. None


# ----------------------------------------
# try:
#     a = b
#     print('a')
# except Exception as e:
#     pass
#     print(e)
# else:
#     print('c')
# finally:
#     print('d')

# a. a b c d
# b. a b c
# c. a c d
# d. error

# print('foo' + 2)
# cannot concatenate 'str' and 'int' objects

# print(list("limbajul python"))
# print(['python'])
# a. ['python']
# b. ‘p’, ‘y’, ‘t’, ‘’, ‘o’, ‘n’
# c. error
# d. [‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’]

# print([x for x in 'python'])

def f(a, list=[]):
    for i in range(a):
        list.append(i*i)
    print(list)

f(3)
f(2, [1, 2, 3])
f(2)

# a. [0, 1, 4] [1, 2, 3, 0, 1] [0, 1, 4, 0, 1] # correct
# b. [0, 1, 4] [1, 2, 3, 0, 1] [0, 1]
# c. error
# d. [0, 1, 4]
