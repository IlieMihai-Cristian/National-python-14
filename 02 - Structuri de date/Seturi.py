# listele cu [], tuplurile cu (), seturile cu {} si dictionarele cu {}

""" Seturile sunt colectii de obiecte imutabile si neordonate (deci neindexabil). Nu permit elemente duplicate """

# var_set = set()
# var_set = {"1", 3, 4, "1", 3, 2, "1"}
# print(var_set)

# set('abc')
# print(set('abca'))
# print({'abc'})


""" pot contine mai multe tipuri de elemente"""

# set_var = {1, 2.5, 'Ana', False, None, int, len, (2, 3, 4)}
# print(set_var)
# set_var_2 = {1, 2.5, 'Ana', False, None, int, len, [2, 3, 4]}
# print(set_var_2)

"""lungimea unui set len()"""  # la fel ca la tupluri , liste

"""copierea unei liste """

""" operatori in si not in"""
# list_4 = [1, 2.5, 'Ana', False, None]
# print(3 in list_4)

""" liste intretesute """
# nested_list = ['a', [3, ['22', 16, None], ['mere', False]], [3.55], 0]
# print(nested_list[2][0])
# print(nested_list[1][2][0])

"""operatii cu seturi"""

# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}
# var_list = ['b', 2]
# UNION
# print(var_set_1 | var_set_2)
# print(var_set_1 | var_list)
# print(var_set_1.union(var_list))

# INTERSECTION
# print(var_set_1.intersection(var_list))
# print(var_set_1 & set(var_list))

# DIFFERENCE
# print(var_set_1 - var_set_2)
# print(var_set_1.difference(var_set_2))

# SYMMETRIC_DIFFERENCE
# print(var_set_1 ^ var_set_2)
# print(var_set_1.symmetric_difference(var_set_2))

"""Metode cu seturi"""
var_set_1 = {'a', 'b', 'c'}
var_set_2 = {'a', 'e', 'f'}

# update
# var_set_1.update(var_set_2)
# print(var_set_1)

# add
# var_set_1.add('d')
# print(var_set_1)

# remove
# var_set_1.remove('x')
# print(var_set_1)

# discard
# var_set_1.discard('x')
# print(var_set_1)

# pop
# var_set_1.pop()
# print(var_set_1)

var_a = (1, 2, 3, 4, 2, 2, 1, 5)
print(tuple(set(var_a)))