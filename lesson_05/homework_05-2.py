# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

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
people_records.insert(0, ('GivenName', 'FamilyName', 101, 'Engineer', 'Lviv'))

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
def swap_elements(test_list, a, b):
    if len(test_list) > max(a, b):
        origin_a = test_list[a]
        origin_b = test_list[b]
        test_list[a] = origin_b
        test_list[b] = origin_a
    return test_list

print(swap_elements(people_records, 1, 5))

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
def age_test(test_list, test_index, test_age):
    if len(test_list) > test_index:
        age = test_list[test_index][2]
        return age >= test_age
    return False

if (age_test(people_records, 6, 30) and
    age_test(people_records, 10, 30) and
    age_test(people_records, 13, 30)):
    print('All people in modified list with records indexes 6, 10, 13 have age >= 30')
else:
    print('Not all people in modified list with records indexes 6, 10, 13 have age >= 30')