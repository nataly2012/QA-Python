# Пишем функцию, которая выводим второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов



def func (*args):
    s = set(args)
    m = sorted(s)

    return (m[1])


print (func(4,6,4,3,8,3,4,2))

