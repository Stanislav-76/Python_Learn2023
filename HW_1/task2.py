# Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число: "))
print(f'Сумма цифр = {n//100 + n%100//10 + n%10}')