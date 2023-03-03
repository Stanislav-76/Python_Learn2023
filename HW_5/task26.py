# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a, b = int(input()), int(input())


def pow(a, b):
    if b == 1:
        return a
    return pow(a, b-1)*a


print(pow(a, b))

# Вариант 2


def pow2(a, b):
    if b == 1:
        return a
    if b % 2:
        return a*pow(a*a, b//2)
    return pow(a*a, b//2)


print(pow2(a, b))
