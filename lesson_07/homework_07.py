# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
print("\n")
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a, b):
    return a + b

print(f'task 2: {sum_numbers(3, 4)}', end = "\n\n")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def  average_numbers(list_numbers):
    return sum(list_numbers) / len(list_numbers)

print(f'task 3: {average_numbers([110, 22, 33, 44, 550])}', end = "\n\n")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def list_reverse(list_original):
    new_list = list_original[::-1]
    return new_list

print(f'task 4: {list_reverse([1, 'Hello', 3, 'World', 5, '!'])}', end = "\n\n")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def max_word(list_words):
    return max(list_words, key=len)

print(f'task 5 - with max: {max_word(["Find", "the", "longest", "word", ":", "Hello", "World", "!"])}', end = "\n\n")

def long_word(list_words):
    longest_word = ""
    for word in list_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(f'task 5 - without max: {long_word(["Find", "the", "longest", "word", ":", "Hello", "World", "!"])}', end = "\n\n")

# task 6
"""  Написати функцію, яка приймає два рядки 
та повертає індекс першого входження другого рядка у перший рядок, 
якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    if index != -1:
        return index
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(f'task 6.1: {find_substring(str1, str2)}', end = "\n\n") # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f'task 6.2: {find_substring(str1, str2)}', end = "\n\n") # поверне -1

# task 7, 8, 9, 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def get_text_with_h():
    while True:
        text = input("Введіть якийсь текст з літерою 'h' або 'H': ")
        if "h" in text.lower():
            return text

result = get_text_with_h()
print(f'task 7 (HW_6.2): {result}', end = "\n\n")

# task 8
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record o the beginning of the given list
def new_record_0(list_of_tuples,name, surname, age, profession, City_location):
    list_of_tuples.insert(0, (name, surname, age, profession, City_location))
    return list_of_tuples

def get_required_input(text):
    while True:
        value = input(text).strip()
        if value:
            return value
        print("Це поле є обов'язковим.")

new_record_0(people_records, get_required_input("Given name: "), get_required_input("Surname: "), input("Age: "), input("Profession: "), input("City_location: "))
print(f'task 8 (HW_05.2.1): {people_records}', end = "\n\n")

# task 9
# Є list з даними
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

def list_vs_type(data_list, data_type): # data_type: str, int, bool, float
    new_list = []
    for item in data_list:
        if type(item) == data_type:
            new_list.append(item)
    return new_list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = list_vs_type(lst1, str)
print(f'task 9 (HW_6.3): {lst2}', end = "\n\n")

# task 10
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

def car_search(car_dict, search_data, car_limit = 5):
    if car_limit > len(car_dict):
        car_limit = len(car_dict)
    # розпакування кортежу:
    year, engine, price = search_data
    # пошук:
    car_found = {}
    for car_name, car_info in car_dict.items():
        if (car_info[1] >= year and
            car_info[2] >= engine and
            car_info[4] <= price):
            car_found[car_name] = (car_info[0], car_info[1], car_info[2], car_info[3], car_info[4])
    car_search_result = dict(list(car_found.items())[:car_limit]
    )
    return car_search_result

def car_sorted(car_dict, criteria_index = 4): # criteria_index: 0-4
    if criteria_index > 4:
        criteria_index = 4
    car_sort_result = dict(
        sorted(car_dict.items(), key=lambda item: item[1][criteria_index])
    )
    return car_sort_result

# пошук з дефолтним лімітом записів:
new_car_data = car_search(car_data, search_criteria)
print(f'task 10: Пошук 1 - дефолт ліміт записів 5: {new_car_data}')

# пошук з вказаним лімітом записів:
new_car_data = car_search(car_data, search_criteria,3)
print(f'task 10: Пошук 2 - вказаний ліміт записів: {new_car_data}', end = "\n\n")

# сортування з дефолтним критерієм ціна:
print(f'task 10: Сортування 1 - дефолтний критерій ціна:{car_sorted(new_car_data)}')

# сортування з вказаним критерієм:
print(f'task 10: Сортування 2 - вказаний критерій:{car_sorted(new_car_data, 1)}')
