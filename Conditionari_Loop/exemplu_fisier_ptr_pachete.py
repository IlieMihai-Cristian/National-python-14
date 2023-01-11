def model_func_pachete(a, b=0, *args, **kwargs):
    # print(type(kwargs))
    total = 0
    initial = a + b
    for elem in args:
        total = total + elem
    for key, value in kwargs.items():
        total = total + value
    return total + initial

model_var_pachete = 'exemplu string pachete'