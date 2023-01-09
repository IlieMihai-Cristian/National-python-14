# var = 20
# print(20/0)

"""raise exception"""
#
# var = 20
# if var > 5:
#     raise Exception('Aici este o eroare')

"""blocul try / except"""

# ex.:
# my_text = input('Introduceti un nr.: ')
# try:
#     value = int(my_text)
#     print(value)
# except ValueError:
#     print('Nu pot converti la int')
# except Exception as e:
#     print('intra pe exceptie', e)

# my_text = input('Introduceti un nr.: ')
# try:
#     value = int(my_text)
#     print(value)
#     print(variabila_nedefinita)
# except ValueError:
#     print('Nu pot converti la int')
# except NameError:
#     variabila_nedefinita = 100
#     print(f'nu am stiut ce valoare vrei asa ca am alocat valoarea {variabila_nedefinita}')
# except Exception as e:
#     print('intra pe exceptie', e)

# print(variabila_nedefinita)

"""else si finally"""

my_text = input('Introduceti un nr.: ')
try:
    value = int(my_text)
    print(value)
except ValueError:
    print('Nu pot converti la int')
except NameError:
    variabila_nedefinita = 100
    print(f'nu am stiut ce valoare vrei asa ca am alocat valoarea {variabila_nedefinita}')
except Exception as e:
    print('intra pe exceptie', e)
else:
    print('nu sunt exceptii')
finally:
    print('printeaza oricum')
