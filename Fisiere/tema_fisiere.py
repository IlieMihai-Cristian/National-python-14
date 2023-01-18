import csv

# with open('categorii.txt', 'a') as file:
#     while True:
#         categorie = input('Introduceti o categorie de task-uri. Tastati enter pentru a incheia: ')
#         if categorie == '':
#             break
#         else:
#             file.write(categorie + '\n')  # (f'{categorie}\n')

# def category_instance():
#     while True:
#         with open('categorii.txt', 'a') as file:
#             file.write(input('Introduceti o categorie de task-uri. Tastati enter pentru a incheia: '))
#         next_category = input('Introduceti alta categorie? (Y/N): ')
#         if next_category.lower() == 'n':
#             break
#     return True
#
# category_instance()


with open('taskuri.csv', 'a') as file:
    while True:
        tasks = input('Introduceti un task. Tastati enter pentru a incheia: ')
        if tasks == '':
            break
        end_date = input('Introduceti o data limita: ')
        if end_date == '':
            break
        responsible = input('Introduceti o persoana responsabila: ')
        if responsible == '':
            break
        category = input('Introduceti o categorie: ')
        if category == '':
            break
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow([tasks, end_date, responsible, category])
        next_task = input('Introduceti un alt task? (Y/N): ')
        if next_task.lower() == 'n':
            break

