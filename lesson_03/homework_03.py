#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n'
)
print(alice_in_wonderland, end = "\n")

alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat."
I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

print(alice_in_wonderland, end = "\n\n")


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_Sea = 436402
Azov_Sea = 37800
Square_Sea = Black_Sea + Azov_Sea
print(f'task 04: Площа Чорного і Азовського морів разом становить  {Square_Sea} км2', end = "\n\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
warehouse_all = 375291
warehouse_1 = warehouse_all - 222950
warehouse_3 = warehouse_all - 250449
warehouse_2 = warehouse_all - warehouse_1 - warehouse_3
print(f'task 05: На складах мережі супермаркетів розміщена наступна кількість товарів:\n'
      f'склад 1: {warehouse_1}\n'
      f'склад 2: {warehouse_2}\n'
      f'склад 3: {warehouse_3}\n')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_month_payment = 1179
total_months = 18
total_payment = one_month_payment * total_months
print(f'task 06: Вартість комп’ютера становить: {total_payment} грн.\n')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f'task 07: Остача від діленя чисел:\n a: {8019 % 8}, b: {9907 % 9}, c: {2789 % 5}, d: {7248 % 6}, e: {7128 % 5}, f: {19224 % 9}\n')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_big_price = 274
pizza_big_number = 4
pizza_medium_price = 218
pizza_medium_number = 2
juice_price = 35
juice_number = 4
cake_price = 350
cake_number = 1
bottle_water_price = 21
bottle_water_number = 3
pizza_payment = (pizza_big_price * pizza_big_number) + (pizza_medium_price * pizza_medium_number)
juice_payment = juice_price * juice_number
cake_payment = cake_price * cake_number
bottle_water_payment = bottle_water_price * bottle_water_number
total_price = pizza_payment + juice_payment + cake_payment + bottle_water_payment
print(f'task 08: Іринці потрібно мати {total_price} грн.\n')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_all = 232
photo_page = 8
page_1 = photo_all // photo_page
page_2 = photo_all % photo_page
if page_2 != 0:
    page = page_1 + 1
else:
    page = page_1
print(f'task 09: {page}\n')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance_km_total = 1600
car_fuel_km_100_liters = 9
tank_capacity_liters = 48

expected_fuel_liters = distance_km_total / 100 * car_fuel_km_100_liters

# якщо вважати що бак автомобіля на початок подорожі путсий або майже пустий, то:
refuel_stops_1 = expected_fuel_liters // tank_capacity_liters
refuel_stops_2 = expected_fuel_liters % tank_capacity_liters
if refuel_stops_2 > 0:
    refuel_stops = refuel_stops_1 + 1
else:
    refuel_stops = refuel_stops_1
print(f'task 10: \n'
      f'Для подорожі знадобиться {expected_fuel_liters} літрів бензину. \n'
      f'Потрібно буде заправитись {int(refuel_stops)} рази/ів до повного бака \n'
      f'(за умови що на початок подорожі бак був неповний).\n')





