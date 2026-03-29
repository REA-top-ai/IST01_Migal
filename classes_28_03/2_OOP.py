from abc import ABC, abstractmethod

# task 1
class AbstractEmployee(ABC):
    new_id = 1
    
    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    # task 2
    @abstractmethod
    def say_id(self):
        pass

# task 3
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"My username is {self.username} and my role is {self.role}")

# task 4
class Employee(AbstractEmployee):
    def __init__(self, name=None):
        super().__init__()
        # task 5
        self._id = self.id
        # task 6
        self.__id = self.id
        self._name = name

    # task 7
    def say_id(self):
        print(f"My id is {self.id}")

    # task 8
    def get_name(self):
        return self._name

    # task 9
    def set_name(self, name):
        self._name = name

    # task 10
    def del_name(self):
        del self._name

# task 11
class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        # task 12
        User.__init__(self, self.id, "Admin")

    # task 13
    def say_id(self):
        super().say_id()
        print("I am an Admin")

# task 14
class Manager(Admin):
    # task 15
    def say_id(self):
        super().say_id()
        print("I am in charge")

# task 16
e1 = Employee()
e2 = Employee()
# task 17
e3 = Admin()
# task 18
e4 = Manager()

# task 19
e1.say_id()
e2.say_id()
e3.say_id()
e4.say_id()

# task 20
e3.say_user_info()

# task 21
meeting = [e1, e2, e3, e4]
# task 22
for emp in meeting:
    emp.say_id()

# task 23
class Meeting:
    def __init__(self):
        self.attendees = []

    # task 24
    def __add__(self, employee):
        self.attendees.append(employee)
        return self

    # task 25
    def __len__(self):
        return len(self.attendees)

# task 26
m1 = Meeting()
# task 27
m1 = m1 + e1
m1 = m1 + e2
m1 = m1 + e3

# task 28
print(len(m1))

# task 29
print(dir(e1))
