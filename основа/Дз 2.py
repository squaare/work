
while True:
    n = int(input('введи число: '))
    if n > 0 and n < 10:
        print(n**2)
        break
    else:
        print('другое число давай пиши: ')