""" dictionare sunt colectii de obiecte mutabile si ordonate(indexate). Nu permite elemente duplicat"""

# var_dict = {}
# var_dict_a = dict()

# var_dict = {'cheie_1': 'valoare_1'}
# print(var_dict)

# var_dict_1 = {1: 'a', 'a': 1, 'list': [1, '2', 'trei'], 'dict': {'dict_2': 4}}
# print(len(var_dict_1))
# print(var_dict_1['list'])

# var_dict = {'key_1': {'key_2': {'key_3': ['a', 1.1, [333, (23, )]]}, 'key_4': 10}, 'key_5': 'key_6'}
# print(var_dict['key_1']['key_2']['key_3'][2][1][0])

# var_dict_2 = {'key_1': 1, 'key_2': 2}
# var_dict_2['key_3'] = 3
# print(var_dict_2)
# var_dict_2['key_3'] = 4
# print(var_dict_2)

""" metode dictionare """
# clear
var = {'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4}
# print(var.clear())

# get
# print(var['key_5'])
# print(var.get('key_5', 10))

# items()
# print(var.items())

# keys()
# print(var.keys())

# values()
# print(var.values())

# pop()
# print(var.pop('key_1'))
# print(var)

# popitem()
# print(var.popitem())

# update()
# dict_2 = {'key_4': 10}
# var.update(dict_2)
# print(var)