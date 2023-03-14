
age = int(input('возраст: '))

if age < 18:
    print('НЕЛЬЗЯ')
    print('иди домой')
    print('быстрее')
elif (age > 18 and age <25):
    if age == 20:
        print('маме скажу')
    else:
        print('ну погоди ты')
elif age == 27:
    print('уже всё, не годен')
else:
    print('лан, проходи')


