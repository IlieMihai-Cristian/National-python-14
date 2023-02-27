#
# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     # def change_name(self, new_name):
#     #     self.name = new_name
#     #     # return self.name
#
#     # @staticmethod
#     # def speak():
#     #     return 'Ham ham ham'
#
#     @property
#     def nume(self):
#         return self.__name
#
#     @nume.setter
#     def nume(self, nume_schimbat):
#         self.__name = nume_schimbat
#
#     @nume.deleter
#     def nume(self):
#         del self.__name
#
#     def __str__(self):
#         return self.__name
#
#
# caine = Dog('Rex')
# print(caine.nume)
# print(caine.__dict__, 'inainte')
# caine.nume = 'Max'
# print(caine.nume)
# print(caine.__dict__, 'dupa')
# del caine.nume
# print(caine.__dict__, 'dupa del')
# print(caine.nume)
#
# # print(caine.__dict__)
# # print(caine._Dog__name)
# # print(caine.legs_no)
# # print(Dog.legs_no)
# # print(caine.change_name('Max'))
# # print(Dog.speak())
# # print(caine.speak())


"""decoratori custom"""

# # def functie_2():
# #     return 'Buna dimineata'
#
#
# def decorator_simplu(parametru):
#     print(f'Apelam functia {parametru.__name__}')
#     return parametru
#
#
# @decorator_simplu
# def functie_simpla():
#     return 'Buna seara!'
#
#
# @decorator_simplu
# def functie_2():
#     return 'Buna dimineata'
#
#
# print(functie_simpla())
# print(functie_2())


#---------------------------------------------------


# def decorator_depozit(functia_noastra):  # param. functia_noastra preia denumirea functiei pe care urmeaza sa o decoreze
#     def ambalaj(carte):  # param. carte preia si trateaza parametrul din definitia functiei decorate
#         return f'Ambalare produs din {functia_noastra.__name__} ce contine titlul {carte}'
#     return ambalaj
#
#
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume
#
#
# print(impachetare_carti('Moara cu noroc'))


# #---------------------------------------------------
#
#
# def decorator_depozit(material):  # param. material preia parametrul decoratorului ce urmeaza a fi aplicat (hartie)
#     def ambalaj(functia_noastra):  # param. functia_noastra preia denumirea functiei pe care urmeaza sa o decoreze
#         def ambalaj_interior(carte):  # param. carte preia si trateaza parametrul din definitia functiei decorate
#             return f'Ambalare produs din {functia_noastra.__name__} cu ambalaj din material {material} ce contine cartea cu titlul {carte}'
#         return ambalaj_interior
#     return ambalaj
#
#
# @decorator_depozit('hartie')
# def impachetare_carti(nume):
#     return nume
#
#
# print(impachetare_carti('Moara cu noroc'))


#---------------------------------------------------


# def decorator_depozit(material):  # param. material preia parametrul decoratorului ce urmeaza a fi aplicat (hartie)
#     def ambalaj(functia_noastra):  # param. functia_noastra preia denumirea functiei pe care urmeaza sa o decoreze
#         def ambalaj_interior(*carte):  # param. carte preia si trateaza parametrul din definitia functiei decorate
#             return f'Ambalare produs din {functia_noastra.__name__} cu ambalaj din material {material} ce contine cartea cu titlul: {", ".join(carte)}'
#         return ambalaj_interior
#     return ambalaj
#
#
# @decorator_depozit('hartie')
# def impachetare_carti(*nume):
#     return nume
#
#
# print(impachetare_carti('Moara cu noroc', 'Ion'))


# #---------------------------------------------------
#
# def decorator(functie):
#     def functie_upper(paramateru):
#         return paramateru.upper()
#     return functie_upper
#
#
# @decorator
# def functie(propozitie):
#     return propozitie
#
#
# print(functie('Ana are mere'))


#---------------------------------------------------

# def decorator(simbol):
#     def adaugare_simbol(functie):
#         def functie_upper(parametru):
#             if simbol == parametru[-1]:
#                 return parametru.upper()
#             else:
#                 return parametru.upper() + simbol
#         return functie_upper
#     return adaugare_simbol
#
#
# @decorator('.')
# def functie(propozitie):
#     return propozitie
#
#
# print(functie('Ana are mere.'))


#---------------------------------------------------

import time
def execution_time(function_name):
    def wrapper(param):
        start = time.time()
        function_name(param)
        end = time.time()
        return f'Execution time: {end - start} and result is {function_name(param)}'
    return wrapper


@execution_time
def addition(number):
    initial_number = 0
    for i in range(number):
        initial_number += i
    return initial_number


print(addition(10000))

