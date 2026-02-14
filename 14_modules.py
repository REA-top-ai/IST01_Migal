# Task 1
import datetime
current_time = datetime.datetime.now()
print(current_time)

# Task 2
import random
random_list = [random.randint(1, 100) for i in range(101)]
random_number = random.choice(random_list)
print(random_number)

# Task 3
import matplotlib.pyplot as plt
import random
number_a = range(1, 13)
number_b = random.sample(range(1000), 12)
plt.plot(number_a, number_b)
plt.show()

# Task 4
employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

def programmers_bonus(employees):
    for employee in employees:
        if "программист" in employee[1]:
            bonus = employee[3] * 0.03
            print(f"{employee[0]} - премия: {bonus} руб.")

def gender_bonus(employees):
    for employee in employees:
        name_parts = employee[0].split()
        if len(name_parts) > 1:
            patronymic = name_parts[1]
            if patronymic.endswith("на"):
                print(f"{employee[0]} - премия к 8 марта: 2000 руб.")
            else:
                print(f"{employee[0]} - премия к 23 февраля: 2000 руб.")

def index_salary(employees):
    from datetime import datetime
    current_date = datetime.now()
    for employee in employees:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        years_worked = (current_date - hire_date).days / 365
        if years_worked > 10:
            indexation = employee[3] * 0.07
        else:
            indexation = employee[3] * 0.05
        print(f"{employee[0]} - индексация: {indexation} руб.")

def vacation_list(employees):
    from datetime import datetime
    current_date = datetime.now()
    vacation_employees = []
    for employee in employees:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        months_worked = (current_date - hire_date).days / 30
        if months_worked > 6:
            vacation_employees.append(employee[0])
    return vacation_employees

programmers_bonus(employees)
gender_bonus(employees)
index_salary(employees)
print(vacation_list(employees))

# Task 5
import random
secret_number = random.randint(1, 9)
winning_count = 0
for i in range(1, 1001):
    num_str = str(i)
    digit_sum = sum(int(digit) for digit in num_str)
    if digit_sum % secret_number == 0:
        print(i)
        winning_count += 1
        if winning_count == 5:
            break

# Extras
# Task 1
n = int(input("Введите количество попыток: "))
for i in range(n):
    result = random.choice(["Орел", "Решка"])
    print(result)

# Task 2
n = int(input("Введите количество попыток: "))
for i in range(n):
    result = random.randint(1, 6)
    print(result)

# Task 3
import random
import string
length = int(input("Введите длину пароля: "))
password = ''.join(random.choice(string.ascii_letters) for i in range(length))
print(password)
