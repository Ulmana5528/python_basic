print("Привіт, мене звати Джарвіс! Як вас звати?")
h1 = input()
print("Вітаю Вас пане", h1)
print("Як ваші справи пане ",h1 ,"???")
h2 = input()
print("Зрозуміло")
print("По граемо в гру???")
h3 = input().lower()
if h3 == 'так':
    h3 = 'Так'
    print("Тоді загадайте перше число")
    a1 = int(input())
    print("Дуже добре")
    print("Тепер загадайте друге число")
    a2 = int(input())
    a3 = a1 + a2
    print("Чудово")
    print("Результат гри ", a3)
elif h3 == 'ні':
    print('ні')
else:
    pass
print("Добре, дякую. Гарного дня")


print("    /\     |    |    /\    |||||  || || ^ //|")
print("   /  \    |    |   /  \   |   || || ||  //||")
print("  /____\   |____|  /    \  |||||  || || // ||")
print(" /      \  |    | /______\ |      || ||//  ||")
print("/        \ |    | |      | |      || |//   ||")
