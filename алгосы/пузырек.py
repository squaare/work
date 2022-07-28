n = 6
mas = [5,7,4,3,8,2]
m = 0
for run in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            m += 1
            mas[i],mas[i+1] = mas[i+1],mas[i]

print(mas)
print(m)
