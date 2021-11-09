# x = 5
# y = x
# print(x, y)
# x += 1
# print(x, y)

# T = (1, 2, 3, 4, 5)
# print(T[0])
# a, b, *C = T
# print(a, b, C, sep=' : ')
# print(type(C))
# print(T)
# print(*T)
# print(*T, sep=' : ', end='!\n')


def hello(name, surname):
    print(name, surname, end='!!!\n')


id_user_777 = 'Andrei', 'Pervyi'
hello('Andrei', 'Pervyi')
hello(*id_user_777)
