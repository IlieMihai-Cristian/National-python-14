
""" siruri de caractere sunt tipuri de date imutabile, indexabile"""

# var = ''
# var = str()
# print(type(var))

""" concatenare """

# print('pro' + 'gram' + 'are')

# var_1 = 'pro'
# var_2 = 'gram'
# var_3 = 'are'
#
# print(var_1 + var_2 + var_3)

""" multiplicare """

# multip = 4
# print(multip * var_1)
# print(id(-4 * var_1))
# print(id(''))

""" transformarea in string str() """

# print(43.5, type(43.5))
# print("43.5", type("43.5"))
# print(43.5, type(str(43.5)))

""" lungimea unui string len() """

# var = 'programare '
# print(len(var))

""" operatori in si not in """

# var = 'programare'
# print('gr' in var)
# print('gr' not in var)

""" indexarea """

# var = 'programare'
#       #0123456789
#
# # print(len(var))
# # print(var[len(var) - 1])
# print(var[-3])

""" slicing """

# var = 'programare'  # [val:val:val] -> [start:stop:pas]
# print(var[1:4])  # rog
# print(var[:4])  # prog
# print(var[1:])  # rogamare
# print(var[-4:-2:2])  # ma
# print(var[1::2])  # var[1::2] == var[1:100:2]


""" interpolarea variabilelor in stringuri """

# var_1 = 'Python'
# var_2 = 'Scoala'
# var_3 = 'IT'
# # caz 1
# print('Grupa de ' + var_1 + ' de la ' + var_2 + ' Informala de ' + var_3 + '!')
# # caz 2 cu format
#     # cu acolade goale
# print('Grupa de {} de la {} Informala de {}!'.format(var_1, var_2, var_3))
#     # cu index in acolade
# print('Grupa de {0} de la {1} Informala de {2}!'.format(var_1, var_2, var_3))
#     # cu denumire cu alocade
# print('Grupa de {str_1} de la {str_2} Informala de {str_3}!'.format(str_1='Python', str_2='Scoala', str_3='IT'))
# # caz 3 cu f'string -> Python 3.6
# print(f'Grupa de {var_1} de la {var_2} Informala de {var_3}!')

""" metode folosite ptr string-uri """
#
# var_1 = 'programare'
# print(var_1.capitalize())  # face primul caracter upper
#
# var_2 = 'programare'
# print(var_2.upper())  # face tot stringul upper
#
# var_3 = 'PROGRAMARE'
# print(var_2.lower())  # face tot stringul lower
#
# var_4 = 'Ana banana'
# print(var_4.count('na'))  # numara de cate ori un anumit substring se regaseste in string

# var_5 = 'Metode folosite pentru stringuri'
# print(var_5.find('folosite'))  # returneaza indexul primei echivalente gasite
# print(var_5.find('zzzz'))  # returneaza -1
# print(var_5.index('folosite'))  # returneaza indexul primei echivalente gasite
# print(var_5.index('zzzz'))  # returneaza eroare

# var_6 = ['Ana', 'are', 'mere', '!']
# print(' '.join(var_6))
#
# var_7 = 'Ana are mere !'
# print(var_7.split(' '))
# var_8 = ' programare '
# print(var_8.lstrip())
# print(var_8.rstrip())
# print(var_8.strip())
# lstrip / rstrip / strip

# var_9 = 'Ana are mere'
# print(var_9.replace(' mere', ''))
