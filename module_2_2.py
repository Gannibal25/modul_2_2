first = int(input('Введите число:'))
second = int(input('Введите число:'))
third = int(input('Введите число:'))

if first==second==third:
    print(3)
elif  first==second and second==first or third==first:
    print(2)
else:
    print(0)


