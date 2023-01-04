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
def func_2(nume='Radu', cantitate=100, device='ceasuri'):
    result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
    return result

print(func_2())
print(func_2('Ion', 50))
print(func_2(device='monitoare'))
print(func_2('Alina', device='monitoare'))