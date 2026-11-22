# Є ліст з числами, порахуйте суму усіх ПАРНИХ чисел в цьому лісті

import random

numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

even_sum = sum(item for item in numbers if item % 2 == 0)
print(f'Сума усіх парних чисел у списку: {even_sum}')