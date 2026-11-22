# Є list з даними
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []  # рядки
lst3 = []  # числа
lst4 = []  # bool
for item in lst1:
    if isinstance(item, str):
        lst2.append(item)
    elif isinstance(item, int) and not isinstance(item, bool):
        lst3.append(item)
    elif isinstance(item, bool):
        lst4.append(item)
    else:
        print(f'Змінні типу string, integer, boolean відсутні у списку.')
print(lst2)
print(lst3)
print(lst4)

# через type():
lst2 = []  # рядки
lst3 = []  # числа
lst4 = []  # bool
for item in lst1:
    if type(item) == str:
        lst2.append(item)
    elif type(item) == int:
        lst3.append(item)
    elif type(item) == bool:
        lst4.append(item)

print(lst2)
print(lst3)
print(lst4)