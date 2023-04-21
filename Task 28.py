a = int(input("Введите первое число "))
b = int(input("Введите второе число "))


def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(a, b))