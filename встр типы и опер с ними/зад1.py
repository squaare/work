top5 = 'Первые 5 мест на соревах: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'

# нужно так: Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!

# найти границы нужного текста
start = top5.find('1')
end = top5.find('4')
print(start, end)

win = top5[26:56]
win = win.upper()
# или по умному:
# top3 = top5[start: end]
# result = 'Поздравляем {} с успехом!' .format(top3.upper())
# print(result)

top3 = 'Поздравляем {} с успехом!' .format(win)
print(top3)
