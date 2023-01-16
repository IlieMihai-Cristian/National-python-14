""" Definitia generala a functiilor"""

# def nume_functie(parametru/parametrii):
#     set instructiuni

# .ex:

# def my_function():
#     var = 'Rezultat'
#     return var  # parametru de iesire
#
# func = my_function()
# print(func)

"""Namespace"""

# def my_function_2():
#     var_2 = 10
#     return var_2
#
# out = my_function_2()
# print(out)

"""Parametrii si Argumentele functiilor"""

# def func(nume, cantitate, device, culoare): # nume = valoare
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device} de culoare {culoare}'
#     return result

# info = func('Mihai', 10)
# info_1 = func('Ion', 20, 'monitoare')
# print(info)
# print(info_1)

""" Argumente keyword """
# info = func('Mihai', device='monitoare', culoare='rosu', cantitate=10) # argument pozitional, urmat de keyword
# print(info)

""" Parametrii Default (standard) """
# def func_2(nume='Radu', cantitate=100, device='ceasuri'):
#     result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
#     return result
#
# print(func_2())
# print(func_2('Ion', 50))
# print(func_2(device='monitoare'))
# print(func_2('Alina', device='monitoare'))

# -----------------------------

# CAZ 1: parametrii pozitionali: def func(a, b, c)
# 1. argumente pozitionale func(10, 20, 30) -> conteaza atat ordinea cat si nr.argumente = nr.parametrii
# 2. argumente keyword func(c=10, a=20, b=30) -> nu conteaza ordinea ci doar nr.argumente = nr.parametrii
# 3. argumente mixte func(10, c=20, b=30) -> conteaza ca intotdeauna arg pozitionale sa fie inainte de cele keyword
#                                            nr.argumente = nr.parametrii

# CAZ 2: parametrii default: def func(a=1, b=3, c=7)

# 1. argumente pozitionale func(10, 20, 30) -> conteaza ordinea si ca nr. argumente <= nr.parametrii
# (daca sunt mai putine argumente, dupa ultimul arg. furnizat restul preiau valorile default ale param.
# Daca sunt mai multe argumente -> eroare)

# 2. argumente keyword func(c=10, a=20, b=30) -> nu conteaza ordinea ci doar ca nr. argumente <= nr.parametrii
# # (daca sunt mai putine argumente, dupa ultimul arg. furnizat restul preiau valorile default ale param.
# # Daca sunt mai multe argumente -> eroare)

# 3. argumente mixte func(10, c=20, b=30) -> conteaza ca intotdeauna arg pozitionale sa fie inainte de cele keyword
# #                                            nr.argumente = nr.parametrii

# CAZ 3: parametrii mix def func(a, b=3, c=7)

""" return """

# ex.:

# def calc(x):
#     if x < 0:
#         return
#     if x > 10:
#         return
#     print(x)
#
# # rezultat = calc(-2)
# # print(rezultat)
# rezultat = calc(5)
# print(rezultat)

"""ANOTARI"""

# def calcul(a: int =0, b: int=0, c: int=0):
#     return a + b + c
#
# print(calcul())
# print(calcul(10))
# print(calcul('10', '20', '30'))

# def calcul(a: int =0, b: int=0, c: int=0) -> int:
#     return a + b + c

# def calcul(a: int =0, b: int=0, c: int=0, d: int=2) -> int:
#     """
#
#     :param d:
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     return a + b + c


"""args"""  # ARGS vine de la arguments

# def suma(a, b=0, *args):
#     # print(type(args))
#     total = 0
#     initial = a + b
#     for elem in args:
#         total = total + elem
#     return total + initial
#
# var = suma(1, 2, 3, 4, 5, 6, 7, 10)
# print(var)


"""kwargs"""  # KWARGS vine de la keyword arguments

def suma(a, b=0, *args, **kwargs):
    # print(type(kwargs))
    total = 0
    initial = a + b
    for elem in args:
        total = total + elem
    for key, value in kwargs.items():
        total = total + value
    return total + initial

# var = suma(1, 2, 3, 4, 5, c=6, d=7, e=10)
# print(var)

# result = suma(1, 2, 3, c=7, d=8, e=9)  # arg 3 -> args este tuplu cu 1 element
# print(result)
# result = suma(1, 2, c=7, d=8, e=9)  # (args nu preia elemente)
# print(result)
# result = suma(1, 2, 3, c=7, d=8, e=9, 4, 5, 6)
# print(result)
# def suma(a, b=0, *args, **kwargs):
# result = suma(1, 2, 3, c=7, d=8, e=9, f=4, g=5, a=6)
# print(result)

"""recursivitate"""

def test_func(nr):
    if nr > 100:
        return 101
    else:
        print(f'Nr este acum {nr}')
        return test_func(nr+10)


val = test_func(3)
print(val)
