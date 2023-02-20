
# class Example:
#
#     def __init__(self, val=5):
#         self.first = val
#
#     def set_second(self, valoare):
#         self.second = valoare
#         return self.second
#
#
# obj_1 = Example()
# obj_1.set_second(4)
# print(obj_1.__dir__())
# # print(obj_1.__first)
# # print(obj_1._Example__first)
# print(obj_1.__dict__)
#
#
# # print(obj_1)
# # print(obj_1.set_second(4))
# # print(obj_1.__dict__)
#
# # obj_2 = Example(2)
# # print(obj_2)
# # print(obj_2.__dict__)
# # obj_2.third = 5
# # print(obj_2.__dict__)


# class Example:
#
#     __counter = 0
#
#     def __init__(self, val=5):
#         self.__first = val
#         Example.__counter += 1
#         # self.__counter += 1
#
#
# object_1 = Example()
# object_2 = Example(2)
# object_3 = Example(4)
#
# print(object_1.__dict__, object_1._Example__counter)
# print(object_2.__dict__, object_2._Example__counter)
# print(object_3.__dict__, object_3._Example__counter)


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#             Example.a = 5
#         else:
#             self.b = 2
#
#
# object_1 = Example()
# # print(object_1.a)
# # print(object_1.b)
#
# # try:
# #     print(object_1.a)
# # except AttributeError:
# #     pass
# # try:
# #     print(object_1.b)
# # except AttributeError:
# #     pass
#
# print(hasattr(object_1, 'a'))
# print(hasattr(object_1, 'b'))
#
# print(object_1.__dict__)
# print(Example.__dict__)

# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
# object_1 = Example()
# print(object_1.a)
# print(getattr(object_1, 'a'))


# class Example:
#
#     def __init__(self, val):
#         self.val = val
#
# ob1 = Example(4)
# ob2 = Example(2)
# ob3 = ob1
# ob3.val += 1
#
# # print(ob1 is ob2)  #False
# # print(ob2 is ob3)  #False
# # print(ob3 is ob1)  #True
# #
# # print(ob1.val)
# # print(ob3.val)
#
# a = 10
# b = 20
# d = 10
# e = [11, 10, 33]
# c = a
# c += 1
# # print(c is a)
# # print(hex(id(a)))
# # # print(c)
# # print(a is e[1])
#
# la = [1, 2, 4]
# lb = [4, 6, 8]
# lc = la
# lc.append(3)
#
# # print(la is lc)
#
#
# ta = (1, 2, 4)
# tb = (4, 6, 8)
# tc = ta
# tc += (5, )
#
# print(ta is tc)



"""Mosteniri"""

# class Vehicule:
#     pass
#
# class Masini(Vehicule):
#     pass
#
# class MasiniDeTeren(Masini):
#     pass
#
# print(issubclass(MasiniDeTeren, Vehicule))
# print(issubclass(Vehicule, MasiniDeTeren))


"""verificam cu isinstance"""

# class Vehicule:
#     pass
#
# class Masini(Vehicule):
#     pass
#
# class MasiniDeTeren(Masini):
#     pass
#
# vehicul_1 = Vehicule()
# masina_1 = Masini()
# masina_de_teren_1 = MasiniDeTeren()
#
# print(isinstance(masina_1, MasiniDeTeren))


"""rescriere de metode"""

# class SuperClasa:
#
#     def __init__(self, name="Mihai"):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#     # pass
#     # def __init__(self, aaa="Cristian"):
#     #     # SuperClasa.__init__(self, name)
#     #     # super(SuperClasa, self).__init__(name)
#     #     super().__init__(name=aaa)
#     #     # self.name = name
#
#     def __str__(self):
#         return f'Print {self.name}'
#
#
# object_1 = SubClasa()
# print(object_1)

"""parametrii ai clasei"""

# class SuperClasa:
#
#     super_variabila = 'super'
#     sub_variabila = 'sub_parinte'
#     def __init__(self, name="Mihai"):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#
#     sub_variabila = 'sub'
#     super_variabila = 'super_copil'
#     def __init__(self, aaa="Cristian"):
#         super().__init__(name=aaa)
#
#     def __str__(self):
#         return f'Print {self.name}'
#
#
# object_1 = SubClasa()
# print(object_1.sub_variabila)
# print(object_1.super_variabila)


"""mai adaugam o clasa"""

class SuperClasa:

    super_variabila = 'super'
    sub_variabila = 'sub_parinte'

    def __init__(self, qwe="Mihai"):
        self.qwe = qwe
        self.var_init = 20

    def __str__(self):
        return f'Numele meu este {self.qwe}'


class Mijloc:

    def __init__(self, gigel):
        # pass
        self.gigel = gigel
        # self.var_init = 20

    variabila_mijloc = 3
    super_variabila = 'mijloc'


class SubClasa(SuperClasa, Mijloc):

    sub_variabila = 'sub'
    super_variabila = 'super_copil'

    def __init__(self, www):
        super(SuperClasa, self).__init__(qwe=www)
        # self.name = aaa
        # self.var_init = 12


    def __str__(self):
        return f'Print {self.qwe}'


# object_1 = SubClasa()
# print(object_1)

object_2 = SubClasa('George')
print(object_2)
