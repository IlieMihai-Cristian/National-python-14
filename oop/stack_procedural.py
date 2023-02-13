stack_list = []


def push(val):
    stack_list.append(val)

push(1)
push(2)
push(3)

print(stack_list)


def pop():
    valoare = stack_list[-1]
    del stack_list[-1]
    return valoare

print(pop())
print(pop())
print(pop())

print(stack_list)