class Calculator:

    def __init__(self):
        self.operator_1 = self.validate_float(input('Alegeti primul numar: '))
        self.semn = self.validate_semn(input('Alege semnul: '))
        self.operator_2 = self.validate_float(input('Alegeti al doilea numar: '))
        if self.operator_2 == 0 and self.semn == '/':
            self.operator_2 = self.validate_zero_division()

    def validate_semn(self, semn):
        lista = ['+', '-', '*', '/']
        while semn not in lista:
            semn = input('Introduceti din nou un semn: ')
        return self.semn

    def validate_float(self, operator):
        while not operator.isdigit():
            operator = input('Numarul este incorect! Alege din nou numarul: ')
        return float(operator)

    def validate_zero_division(self):
        while self.operator_2 == 0:
            self.operator_2 = self.validate_float(input('Reintroduceti un numar diferit de 0: '))
        return self.operator_2

    def adunare(self):
        return self.operator_1 + self.operator_2

    def scadere(self):
        return self.operator_1 - self.operator_2

    def inmultire(self):
        return self.operator_1 * self.operator_2

    def impartire(self):
        # # if self.operator_2 != 0:
        # #     return self.operator_1 / self.operator_2
        # # else:
        # #     while self.operator_2 == 0:
        # #         print('Impartirea la 0 nu este posibila!')
        # #         self.operator_2 = float(input('Reintroduceti un numar diferit de 0: '))
        # while self.operator_2 == 0:
        #     self.operator_2 = float(input('Reintroduceti un numar diferit de 0: '))
        return self.operator_1 / self.operator_2

    def __str__(self):
        if self.semn == '+':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}'
        elif self.semn == '-':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}'
        elif self.semn == '*':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}'
        elif self.semn == '/':
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.impartire()}'
        else:
            return f'Operatia nu exista!'


obj_calculator = Calculator()
print(obj_calculator)


# object_name = obj_calculator
# class_name = Calculator
# proprerty = self.operator_1, self.operator_2, semn
# activity = adunare, scadere, inmultire, impartire

