import math

""" Listele sunt colectii de obiecte si sunt mutabile si ordonate (indexabil). Permit elemente duplicate """

# var_list = list()
# var_list_ = []

""" ordonare """

# list_1 = [1, 2, 3, 4]
# list_2 = [2, 1, 3, 4]
# print(list_1 == list_2)
# print(list_1 is list_2)

""" pot contine mai multe tipuri de elemente"""

# list_var = [1, 2.5, 'Ana', False, None, int, len, math]
# print(list_var)

""" concatenare """

# print([1, 2] + [3, 4])

"""multiplicare"""

# print([1, 2] * 5)

"""lungimea unei list len()"""

# list_1 = [1, 2, 3, 4]
# print(len(list_1))

""" indexarea """
# list_idx = [1, 2.5, 'Ana', False, None]
# print(list_idx[4])
# list_idx[4] = True
# print(list_idx)

"""slicing"""
# list_idx = [1, 2.5, 'Ana', False, None]
# print(list_idx[-5::2])

"""copierea unei liste """
# list_3 = [1, 2.5, 'Ana', False, None]
# list_copy = list_3[:]
# list_copy[0] = 'AAA'
# print(list_3)
# print(list_copy)
# print(list_3 is list_copy)

# list_copy = list_3.copy()
# print(list_3)
# print(list_copy)
# print(list_3 is list_copy)

# list_copy = list_3
# print(list_copy)
# print(list_3 is list_copy)

""" operatori in si not in"""
# list_4 = [1, 2.5, 'Ana', False, None]
# print(3 in list_4)

""" liste intretesute """
# nested_list = ['a', [3, ['22', 16, None], ['mere', False]], [3.55], 0]
# print(nested_list[2][0])
# print(nested_list[1][2][0])

""" metode in liste """

# count
# m1 = ["1", 3, 4, "1", 3, 2, "1"]
# var = m1.count("1")
# print(var)

# min si max
# list_m2 = [45, 34.3, 2, 10*2, 88.88]
# var_min = min(list_m2)
# var_max = max(list_m2)
# print(var_min)
# print(var_max)

# del element
# list_m4 = [1, 2.5, 'Ana', False, None]
# del list_m4[-1]
# print(list_m4)
# list_m5 = ['ana', 'are', 'mere', 'si', 'pere']
# list_m5[1:2] = ['nu', 'are', 'fructele']
# print(list_m5)
# list_m5_1 = [1, 2, 3]
# list_m5_1[-2:-1] = [11, 22, 33]
# print(list_m5_1)

# append
# list_m6 = [1, 2.5, 'Ana', False, None]
# list_m6.append('ok')
# print(list_m6)

# extend
# list_m7 = [1, 2.5, 'Ana', False, None]
# # list_m7.extend(['ok', None])
# list_m7 += ['ok', None]
# print(list_m7)

# list_m7 = [1, 2.5, 'Ana', False, None]
# list_m7.insert(2, 11)
# print(list_m7)

# pop
# list_m9 = [1, 2.5, 'Ana', False, True]
# list_m9.pop()  # elimina intotdeaua ultimul element din lista
# list_m9.pop(1)  # elimina element specificat
# print(list_m9)

# remove
# list_m10 = [1, 2.5, 'Ana', False, True, 'Ana']
# list_m10.remove('Ana')
# print(list_m10)

#clear
# list_m11 = [1, 2.5, 'Ana', False, True, 'Ana']
# list_m11.clear()
# print(list_m11)

# reverse
# list_m12 = [1, 2.5, 'Ana', False, True, 'Ana']
# list_m12.reverse()
# print(list_m12)

# sort
# list_m13 = ['ana', 'are', 'mere', 'si', 'pere']
# # list_m13.sort()
# # print(list_m13)
# list_m13.sort(reverse=True)
# print(list_m13)
