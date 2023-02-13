class Calculator:

    def __init__(self):
        self.operator_1 = input('Alegeti primul numar: ')
        self.semn = input('Alege semnul: ')
        self.operator_2 = input('Alegeti al doilea numar: ')

    def adunare(self):
        return self.operator_1 + self.operator_2

    def __str__(self):
        return f'{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}'

obj_calculator = Calculator()
print(obj_calculator)