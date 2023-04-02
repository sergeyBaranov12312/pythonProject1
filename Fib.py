a = 1
b = 1
mas = []
for i in range(100):
    if i<=1:
        mas.append(i)
    if i == 99:
        break
    if i > 1:
        mas.append(mas[i-2]+mas[i-1])


print(mas)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …