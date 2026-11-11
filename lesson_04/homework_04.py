adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f'task 01: {adwentures_of_tom_sawer}')

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f'task 02: {adwentures_of_tom_sawer}')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.

re — це стандартний модуль Python для роботи з регулярними виразами (regular expressions).
За допомогою re можна: 
- шукати текст за шаблоном;
- замінювати текст;
- розбивати текст на частини;
- перевіряти, чи відповідає рядок певному формату.

re.sub() - Замінює всі збіги шаблону на інший текст.
re.findall() - Знаходить усі збіги
re.search() - Шукає перший збіг у тексті.
re.split() - Розбиває рядок за шаблоном.
"""

import re
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
print(f'task 03 regex: {adwentures_of_tom_sawer}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_letter = re.findall(r'h', adwentures_of_tom_sawer)
h_count = len(h_letter)
print(f'task 04 regex: {h_count}')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
upper_count = 0
for i in adwentures_of_tom_sawer:
    if i.isupper():
        upper_count += 1
print(f'task 05: {upper_count}')

# or with regex:
upper_letter = re.findall(r'[A-Z]', adwentures_of_tom_sawer)
upper_count = len(upper_letter)
print(f'task 05 regex: {upper_count}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
print(f'task 06: {second_tom}')

# or with regex:
match_Tom = list(re.finditer(r'\bTom\b', adwentures_of_tom_sawer))
print(match_Tom)
print(f'task 06 regex: {match_Tom[1].start()}')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(f'task 07: {adwentures_of_tom_sawer_sentences}')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'task 08: {adwentures_of_tom_sawer_sentences[3].lower()}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(f'task 09: ТАК - з "By the time" починається речення "{sentence}"')
    else:
        print(f'task 09: НІ = з "By the time" НЕ починається речення "{sentence}"')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_list = last_sentence.split()
words_count = len(words_list)
print(f'task 10: {words_count}')