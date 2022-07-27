name = input('введите имя: ')
fam = input('введите фамилию: ')
age = int(input('введите возраст: '))
wet = int(input('введите вес: '))

if age<40 :
    if wet>50 and wet<120:
        print(name, fam,',',age,'год',',', 'вес',wet, ' - состояние хорошее')
    else:
        print(name, fam, ',', age, 'год',',', 'вес', wet, ' - следует заняться собой')

else:
    if wet > 50 and wet < 120:
        print(name, fam, ',', age, 'год', 'вес', wet, ' - состояние хорошее')
    else:
        print(name, fam, ',', age, 'год', 'вес', wet, ' - следует обратиться к врачу')