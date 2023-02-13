"""Max este o pisica mare care doarme toata ziua"""
# object_name = Max (numele obiectului) -> substantiv
# class_name = Pisica (numele clasei) -> substantiv
# property = marime_pisica (proprietate sau atribut) -> adjectiv/adverb
# activity = doarme -> verb

"""O masina Dacia, merge repede"""
# object_name = Dacia
# class_name = masina
# proprerty = repede
# activity = merge

"""Catelul Dino are 4 picioare si latra tare"""
# object_name = Dino
# class_name = Catelul
# proprerty = 4 picioare, tare
# activity = latra


"""transpunere"""

# class Dog:  # FirstDogClass
#
#     def __init__(self):
#         pass
#
# obj_1 = Dog()
# print(type(obj_1))


"""Varianta procedurala a stivei"""
# stak_list = []
#
#
# def push(val):
#     stak_list.append(val)
#
# push(1)
# push(2)
# push(3)
#
# print(stak_list)
#
# def pop():
#     valoare = stak_list[-1]
#     del stak_list[-1]
#     return valoare
#
# print(pop())
# print(pop())
# print(pop())
#
# print(stak_list)

"""Varianta oop a stivei"""


# class Stack:
#
#     def __init__(self):
#         # self.stack_list = []
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#         print(self.__stack_list)
#
#     def pop(self):
#         valoare = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return valoare
#
# obj_stiva = Stack()
# obj_stiva.push(1)
# obj_stiva.push(2)
# obj_stiva.push(3)
#
# print(obj_stiva.pop())
# print(obj_stiva.pop())
# print(obj_stiva.pop())

"""variabila scoasa din metoda si trecuta in init"""


class Stack:

    def __init__(self, *val1):
        # self.stack_list = []
        self.__stack_list = []
        # print(val1)
        self.valoare1 = val1

    def push(self):
        for element in self.valoare1:
            self.__stack_list.append(element)
        # print(self.valoare1)
        print(self.__stack_list)

    def pop(self):
        valoare = self.__stack_list[-1]
        del self.__stack_list[-1]
        return valoare


# obj_stiva = Stack(1)
# obj_stiva.push()
# obj_stiva.valoare1 = 2
# obj_stiva.push()
# obj_stiva.valoare1 = 3
# obj_stiva.push()
#
# print(obj_stiva.pop())
# print(obj_stiva.pop())
# print(obj_stiva.pop())

obj_stiva = Stack(1, 2, 3)

obj_stiva.push()
print(obj_stiva.pop())
print(obj_stiva.pop())
print(obj_stiva.pop())