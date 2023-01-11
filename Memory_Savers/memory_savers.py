"""Functia Lambda"""
# - se mai numesc si fctii anonime (fara def/ fara nume)
# pot avea oricate argumente dar doar o singura expresia. Expresia este concomitent evaluata si returnata

element = lambda x: x * 10  # unde x este argumentul si x * 10 este expresia

# def element_1(x):
#     return x * 10
#
# print(element(10))
# print(element_1(10))

# element_2 = lambda x, y: x + y
# print(element_2(11, 22))


"""FILTER"""
# program care sa returneze o lista cu nr pare din lista initiala

# Fct Filter intoarce un obiect al clasei filter (care este defapt un iterator) rezultat prin aplicarea
# unei functii fiecarui element dintr-un obiect iterabil (lista, string, tuplu ..)

list_1 = [1, 5, 4, 6, 8, 11, 3, 12]
# list_2 = list(filter(lambda x: (x % 2 == 0), list_1))
# print(list_2)
# print(type(list_2))
# print(list(list_2))

# ex cu for loop:
# lista_forloop = []
# for item in list_1:
#     if item % 2 == 0:
#         lista_forloop.append(item)
# print(lista_forloop)

# ex cu fct clasica:
# def filtrare(variabila):
#     if variabila % 2 == 0:
#         return True
#     else:
#         return False
#
# filtered = filter(filtrare, list_1)
# print(list(filtered))

"""MAP"""
# Program care sa dubleze fiecare element din lista folosind lambda si map:

# Fct Map intoarce un obiect al clasei map (care este defapt un iterator) rezultat prin aplicarea
# unei functii fiecarui element dintr-un obiect iterabil (lista, string, tuplu ..)

# list_3 = map(lambda x: x * 2, list_1)
# print(list(list_3))
#
# def dublare(elem):
#     return elem * 2
#
# mapare = map(dublare, list_1)
# print(list(mapare))


"""ZIP"""

# Fct zip preia parametrii iterabili (pot fi 0 sa mai multi) si returneaza obiect al clasei zip
# (care este defapt un iterator) sub forma de tupluri, formate din grupuri de elemente provenite din
# parametrii initiali.
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initale

list_with_int = [1, 2, 3, 4, 5]
list_with_strings = ['one', 'two', 'three', 'four', 'five']
# var = []
# var_1 = list()
# result = zip()
# print(tuple(result))

# result = zip(list_with_int, list_with_strings)
# print(list(result))

# list_with_decimals = [1.11, 'asdsadas', 3.33, 4.44, 5.55]
#
# result = zip(list_with_int, list_with_strings, list_with_decimals)
# print(list(result))
#
# print(dict(result))

"""UNZIP"""
# * cu zip

# result = zip(list_with_int, list_with_strings)
# # print(list(result))
# val_1, val_2 = zip(*list(result))
# # print('val_1 =', list(val_1))
# print('val_2 =', list(val_2))


"""COMPREHENSION LIST"""

var = 'comprehension'

#caz cu forloop:
# list_for_loop = []
# for elem in var:
#     list_for_loop.append(elem)
# print(list_for_loop)
#
# #caz cu lambda:
# list_lambda = list(map(lambda x: x, var))
# print(list_lambda)
#
# #caz cu comprehension:
# list_string = [elem for elem in var]
# print(list_string)

number_list = [x for x in range(20) if x % 2 == 0]
            #x - elem manipulat, for-ul, conditie

# number_list = []
# for x in range(20):
#     if x % 2 == 0:
#         number_list.append(x)

print(number_list)

number_list_2 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]

print(number_list_2)

number_list_3 = ['Par' if var % 2 == 0 else 'Impar' for var in range(10)]

print(number_list_3)

