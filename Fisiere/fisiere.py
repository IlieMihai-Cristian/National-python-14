import csv

# file = open('data.txt', 'r')
# r ->  CITESTE, NU ADAUGA (daca nu exista, da eroare)
# w ->  SCRIE IN FISIER (daca nu exista fisierul, Python il creaza) ->
#         rescrie(textul este sters si suprascris)
# a ->  SCRIE IN FISIER (daca nu exista fisierul, Python il creaza) ->
#         append(adauga text)

"""Cursul de Python de la Scoala Informala:"""

'mod 1'
# file = open('data.txt', 'r+')
# file.write('Astazi este luni')
# file.close()

# r+ -> CITESTS SI SCRIE IN FISISER (daca nu exista, da eroare)

'mod 2'
# file = open('data1.txt', 'w')
# try:
#     file.write('Astazi este luni')
# finally:
#     file.close()

'mod 3'

# with open('data2.txt', 'w') as file:
#     file.write('Astazi este luni')

# --------------------------

"""citire din fisier"""

# var1
# with open('data.txt', 'r') as file_read:
#     for line in file_read.readlines():
#         print(line)

#var2
# with open('data.txt', 'r') as file_read:
#     for line in list(file_read):
#         print(line)

#var3
# with open('data.txt', 'r') as file_read:
#     while True:
#         line = file_read.readline()
#         # print(line)
#         if not line:
#             break
#         print(line)

# --------------------------

"""fisiere tip CSV"""

# with open('fisier_csv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     print(rows)
#     print(type(rows))
    # for row in rows:
    #     print(row)

car_list = [
    ['Dacia', 'Logan', 2015, 90],
    ['Renault', 'Clio', 2017, 100]
]

#var 1
with open('fisier_csv.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows(car_list)

#var 2
# with open('fisier_csv.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for car in car_list:
#         csv_writer.writerow(car)
