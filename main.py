first=int(input('Введите первое число : '))
second=int(input('Введите второе число : '))
third=int(input('Введите третье число : '))
if first == second and first == third and second == third:
    print('Совпадают', 3, 'числа')
elif first == second or first == third or second == third:
    print('Совпадают', 2,'числа')
elif first != second or first != third or second != third:
    print('Совпадают', 0, 'чисел')


