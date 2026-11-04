# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ") # end is an optional parameter of print() function that specifies what should be printed after the output
    print("world!") # Python uses indentation to define code blocks (such as inside if, for, while, def, etc.). The second line is indented by 4 spaces, but there is no preceding statement that starts a block.

# correct code:
print("Hello", end = " ")
print("world!") # extra indentation is removed

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
print(f"{hello} {world}!")

# correct code:
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!") # indentation required for if statement is added

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print()

#correct code:
for letter in "Hello world!":
    print(letter) # missing variable added

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = x

# resolved task:
apples = 2
banana = 4 * apples
print(banana)

# task 05 == виправте назви змінних
1_storona = 1
?torona_2 = 2
сторона_3 = 3
$torona_4 = 4

# correct variables:
storona_1 = 1 # variable names cannot begin with a digit.
storona_2 = 2 # python variable may contain: letters (a-z, A-Z), digits (0-9) (except first character), underscore
сторона_3 = 3 # python 3 supports Unicode characters in identifiers, including Cyrillic letters
storona_4 = 4 # python variable may contain: letters (a-z, A-Z), digits (0-9) (except first character), underscore

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = ? + ? + ? + ?
print()

# resolved task:
storona_1 = 1
storona_2 = 2
сторона_3 = 3
storona_4 = 4
perimetery = storona_1 + storona_2 + сторона_3 + storona_4
print(f"Perimeter: {perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
# resolved task:
apple = 4
pear = apple + 5
plum = apple - 2
trees = apple + pear + plum
print(f"All the trees in the garden: {trees}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# resolved task:
morning_t = 5
afternoon_t = morning_t - 10
evening_t = afternoon_t + 4
print(f"Evening temperature: {evening_t}")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
# resolved task:
boys = 24
girls = boys / 2
drama_club = boys + girls
today_sick_member = 1
today_skip_member = 2
today_present_members = int(drama_club - today_sick_member - today_skip_member)
print(f"Today {today_present_members} drama club members are present at rehearsal")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
# resolved task:
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
total_price = book_1 + book_2 + book_3
print(f"Total price (one copy of each book): {total_price:.2f}")



