from re import sub


class Person:
    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age 

    def get_name(self):
        return self.__name  

    def set_name(self, new_value):
        self.__name = new_value
        


    def get_role_info(self):
        return f'Person with a name {self.__name}'

class Student(Person):
    def __init__(self, name, age, student_id) -> None:
        super().__init__(name, age)
        self.__student_id = student_id 
        self.__grades = []

    def add_grades(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            return "Error: grade must be in area from 0 to 100"

    def avg_grade(self):
        return sum(self.__grades) / len(self.__grades)
    
    def get_role_info(self):
        return f'Student {self.__name}, ID:{self.__student_id}, average grade: {self.avg_grade()}'


class Teacher(Person):
    def __init__(self, name, age, subject) -> None:
        super().__init__(name, age)
        self.__subject = subject
        self.__salary = 0

    def set_salary(self, amount):
        assert(amount > 0) 
        "Error: salary must be a positive integer."
    
    def get_role_info(self):
        return f'Teacher {self.__name} teaches a {self.__subject}, his salary is {self.__salary}'


p1 = Person("roma", 18)
        
print(p1.get_name())
