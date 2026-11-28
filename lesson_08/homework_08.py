class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def show_info(self):
        print(f'Given name: {self.first_name}, Family name: {self.last_name}, Age: {self.age}, Average grade: {self.average_grade}')

# Створення об'єкта student
student1 = Student("Ivan", "Ivanyshyn", 25, 89)
student2 = Student("Maria", "Kit", 28, 92)

print("Student info:")
student1.show_info()
student2.show_info()

student1.change_average_grade(100)
student2.change_average_grade(100)

print("\nUpdated Student info:")
student1.show_info()
student2.show_info()