def vstavka(list1):
    for i in range(1, len(list1)):
        per = list1[i]
        j = i - 1
        while j >= 0 and per < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j+1] = per
    return list1

list1 = [5, 9, 1, 7, 4, 3]
print("было так: ", list1)

print("отсортировали так: ", vstavka(list1))