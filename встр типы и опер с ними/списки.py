friends = ['Max', 'Leo', 'Kate']

print(friends)

print(len(friends)) # сколько элементов в списке

friends.append('Ron') # добавление элемента в список

print(friends)

print(len(friends))

print(friends.pop()) # вывод последнего элемента и удаление

print(friends)

friends.clear() # удаление всего списка
print(friends)

friends = ['Max', 'Leo', 'Kate']

friends.remove('Leo') # удаление элемента списка
print(friends)

del friends[1] # удаление элемента по номеру в списке
print(friends)