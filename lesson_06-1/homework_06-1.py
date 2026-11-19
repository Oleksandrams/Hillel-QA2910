# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

text = input("Введіть якийсь текст: ")
set_from_string = set(text) # only unique characters are left in set
print(set_from_string)
if (len(set_from_string) > 10):
    print(f'унікальних символів в строці "{text}" > 10: ', True)
else:
    print(f'унікальних символів в строці "{text}" > 10: ', False)

# with 2 inputs:

input_1 = input("Введіть якийсь текст: ")
input_2 = int(input("Введіть якесь ціле число: "))
result = len(set(input_1)) > input_2
print(f'унікальних символів в строці "{input_1}" > {input_2}: {result}')
