# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# s = "пара-ра-рам рам-пам-папам па-ра-па-дам"
s = input("Введите стих: ")

def ritm(str):
    str = str.split()
    maxCount = -1
    for i in str:
        count = 0
        for char in i:
            if char in "аоуыэеёиюя":
                count += 1
        if maxCount == -1:
            maxCount = count
        if count != maxCount:
            return "Пам парам"
    return "Парам пам-пам"

print(ritm(s))