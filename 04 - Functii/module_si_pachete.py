# from exemplu_fisier_ptr_module import model_func, model_var
# print(model_func(1, 2, 3, 4, 5, c=6, d=7, e=10))
# print(model_var)
import sys
import os
import datetime

# from exemplu_fisier_ptr_module import model_func as functie_apelata
# print(functie_apelata(1, 2, 3, 4, 5, c=6, d=7, e=10), 'print 2')

# from exemplu_fisier_ptr_module import *
# print(model_func(1, 2, 3, 4, 5, c=6, d=7, e=10), 'print 3')

# import exemplu_fisier_ptr_module as mod
# print(exemplu_fisier_ptr_module.model_func(1, 2, 3, 4, 5, c=6, d=7, e=10), 'print 4')

# print(mod.__file__)

# from exemplu_fisier_ptr_module import model_var
# print(dir(model_var))
# print(model_var.__doc__)
# # print(dir(model_func))

# ------------------------------------

# print(sys.path)
# sys.path.insert(0, '/home/mihai/PycharmProjects/National-python-14')
# sys.path.append('/home/mihai/PycharmProjects/National-python-14')
# print(sys.path, 1)
#
# from Conditionari_Loop.exemplu_fisier_ptr_pachete import model_func_pachete
# print(model_func_pachete(1, 2, 3, 4, 5, c=6, d=7, e=10), 'print aaaa')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
# print(sys.path)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

from Conditionari_Loop.exemplu_fisier_ptr_pachete import model_func_pachete as model_2
print(model_2(1, 2, 3, 4, 5, c=6, d=7, e=10), 'print aaaa')

