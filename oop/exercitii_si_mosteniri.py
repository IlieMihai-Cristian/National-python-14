
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


class Example:
    __counter = 0

    def __init__(self, val=1):
        if val % 2 != 0:
            self.a = 1
            Example.a = 5
        else:
            self.b = 2


object_1 = Example()
# print(object_1.a)
# print(object_1.b)

# try:
#     print(object_1.a)
# except AttributeError:
#     pass
# try:
#     print(object_1.b)
# except AttributeError:
#     pass

# print(hasattr(object_1, 'a'))
# print(hasattr(object_1, 'b'))

print(object_1.__dict__)
print(Example.__dict__)