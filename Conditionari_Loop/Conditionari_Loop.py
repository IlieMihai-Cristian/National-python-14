""" Declaratie IF """

# if expresie:
    # instructiune (set de instructiuni sau declaratii)

# ex:

# first_number = 10
# second_number = 20

# if first_number > second_number:
#     print('se respecta conditia')

# if expresie:
    # instructiune_1
    # instructiune_2



    # instructiune

# ex2
first_number = 10
second_number = 20
lista_ex = ['rosu', 'galben', 'albastru']

# if 'galben' in lista_ex:
#     print('expresia este adevarata')  # 1  a
#     if first_number > second_number:
#         print('a intrat pe primul if din interior expresie')
#     print('mesaj 1')  # 2
#     if first_number <= second_number:
#         print('a intrat pe al doilea if din expresie')  # 3
#         print('mesaj 2')  # 4  b
#     print('mesaj 3')  # 5  c
# print('mesaj 4')  # 6  d


""" conditiile else si elif """

# if expresie:
    # instr
# else:
    # instr

var_nr = 40

# if var_nr >= 50:
#     print('nr. este cel putin mai mare sau egal cu 50')
# else:
#     print('nr. este mic decat 50')
# print(f'Acesta este numarul ales: {var_nr}')


# val = 20
# # expresie = True
# if expresie is True:
#     val = 10
# # print(val)
#
# # [], (), {}, '', 0, None
# print(None == True)

#ex4

# nume = "Ion"
# if nume == "Vlad":
#     print('Vlad')
# elif nume == "George":
#     print('George')
# elif nume == 'Radu':
#     print("Radu")
# else:
#     if 'o' in nume:
#         print('ceva a gasit')
#     else:
#         print('numele nu este validat')

# lista_ex_1 = [1, 2, 3]
#
# if 1 in lista_ex_1:
#     print(1)
# else:
#     if 2 in lista_ex_1:
#         print(2)
#     else:
#         print(3)


# nume_utilizator = input('Va rugam introduceti varsta dvs.:')
#
# if not str(nume_utilizator).isdigit():
#     print('Nu ati introdus corect varsta. Mai incercati')
# elif str(nume_utilizator).isdigit():
#     if int(nume_utilizator) < 18:
#         print('Ne pare rau. Nu ai varsta necesara pentru scoala de soferi')
#     elif 18 <= int(nume_utilizator) < 65:
#         print('Felicitari esti eligibil ptr permis')
#     else:
#         print('Esti bosorog')

""" operator ternar """
# ex:5

var = 'cuvant'

# if 'uv' in var:
#     valoare = 10
# else:
#     valoare = 20
#
# valoare = 10 if 'uv' in var else 20

# nume = 'Radu'
# if nume == "Vlad":
#     print('Vlad')
# elif nume == "George":
#     print('George')
# elif nume == 'Radu':
#     pass
# else:
#     print('aaaa')
#

"""FOR LOOP"""
# for-ul este folosit pentru a parcurge un element iterabil --> iteratia este finita

# for <variabila temporara> in <iterabil>:
    # instructiune

# list_ex = ['unu', 'doi', 'trei']
#
# for x in list_ex:
#     print(x)

var_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4}

# for x in var_dict:
#     print(x)
# for x in var_dict.keys():
#     print(x)

# for x in var_dict:
#     print(var_dict[x])
# for x in var_dict.values():
#     print(x)

# for key, value in var_dict.items():
#     print(f'Cheie: {key} --> valoare: {value}')

# for x in []:
#     print(x)

""" FOR enumarate"""
list_ex = ['unu', 'doi', 'trei']

# for idx, elem in enumerate(list_ex, start=100):
#     print(idx, ':', elem)

""" FOR cu range """
# for item in range(-100, 101, 10):
#     print(item)

""" FOR cu break si continue"""

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     if animal.startswith('m'):
#         continue
#     print(animal)

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     if animal.startswith('m'):
#         break
#     print(animal)
#
# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     if animal.startswith('m'):
#         pass
#     print(animal)

# for animal in ['urs', 'maimuta', 'melc', 'vulpe', 'marmota']:
#     print(animal)
#     break
# else:
#     print('ok')

"""WHILE LOOP"""
# while este folosit pentru repetarea instructiunilor --> ATENTIE iteratia poate fi repetata la nesfarsit
# nr = 0
# while nr > 0:
#     nr -= 1
#     print(nr)

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         break
#     print(nr)

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         continue
#     print(nr)

# nr = 5
# while nr > 0:
#     nr -= 1
#     print(nr)
# else:
#     print('final')

nr = 5
while nr > 0:
    nr -= 1
    if nr == 1:
        break
    print(nr)
else:
    print('final')